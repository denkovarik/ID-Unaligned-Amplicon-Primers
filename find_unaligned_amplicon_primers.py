###############################################################################
# File: find_unaligned_amplicon_primers.py
# Purpose: To find the primers responsible for the unaligned amplicons
#
# Description:
# This program parses the results from the Bowtie2 software for the unaligned 
# amplicons. It will then attempt to determine the primers responsible.
#
# Author: Dennis Kovarik
###############################################################################

import pysam, sys
from classes.Primer import Primer
from classes.Reverse_Primer import Reverse_Primer
from classes.Forward_Primer import Forward_Primer
from classes.Sequence import Sequence
from classes.Amplicon import Amplicon
from utils import *
from progress.spinner import Spinner


# Parse the command line arguments
args = parse_cmd_args(sys.argv)
# Dictionary of counts 
counts =    {
                "total" : 0,
                "total_unique" : 0,
                "fp_total" : 0,
                "rp_total" : 0,
                "unique_fp" : 0,
                "unique_rp" : 0,
                "count"     : 0,
            }
# Read in the Primers
primers = read_primers(args['--primers_path'])
# Dictionary to hold unique sequences
unique_unaligned_seqs = {} 
# Read Bowtie2 Results .bam file
samfile = pysam.AlignmentFile(args['--bowtie2_rslt_path'], "rb")
with Spinner("Matching Primers to Unique Unaligned Amplicons... ") as spinner:
    for read in samfile.fetch(until_eof=True):
        # Read unaligned sequences
        if read.is_unmapped: 
            seq = Sequence(read.get_forward_sequence())
            # Group by unique sequence
            if seq not in unique_unaligned_seqs.keys():
                # Find primers for sequence
                fP = seq.primer_binary_srch(primers['forward_primers'])
                rP = seq.primer_binary_srch(primers['reverse_primers'])
                counts = update_counts(counts, fP, rP, True)                
                unique_unaligned_seqs[seq] = Amplicon(seq, fP=fP, rP=rP)
            else:
                fP = unique_unaligned_seqs[seq].fP
                rP = unique_unaligned_seqs[seq].rP
                counts = update_counts(counts, fP, rP, False)
                unique_unaligned_seqs[seq].count += 1
            if counts['count'] % 5000 == 0:
                spinner.next()
            counts['count'] += 1
print_counts(counts)
samfile.close()
