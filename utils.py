import sys
import pandas as pd
from classes.Primer import Primer
from classes.Reverse_Primer import Reverse_Primer
from classes.Forward_Primer import Forward_Primer
from classes.Sequence import Sequence


def parse_cmd_args(cmd_args):
    """
    Parses the command line agrs and returns a dictionary of arguments.

    :param cmd_args: A list of arguements from the command line
    :return: A dictionary of arguments
    """
    args =  {
                "--primers_path"        : "given/input_given/primers.xlsx",
                "--bowtie2_rslt_path"   : "given/input_given/input.bam",
                "--output_NS_pairs"     : "my_output/output_NS_pairs.xlsx",
                "--output_NS_list"      : "my_output/output_NS_list.xlsx",
                "--heat_map"            : "my_output/output_NS_pairs_log10.svg",
            }
    if len(cmd_args) % 2 != 1:
        print("Invalid number of command line arguments.")
        print_usage()
        exit()
    # Parse the command line arguments
    for i in range(1, len(cmd_args), +2):
        if cmd_args[i] == "--bowtie2_rslt_path":
            args[cmd_args[i]] = cmd_args[i+1] 
        elif cmd_args[i] == "--primers_path":
            args[cmd_args[i]] = cmd_args[i+1] 
        elif cmd_args[i] == "--output_NS_pairs":
            args[cmd_args[i]] = cmd_args[i+1] 
        elif cmd_args[i] == "--output_NS_list":
            args[cmd_args[i]] = cmd_args[i+1] 
        elif cmd_args[i] == "--heat_map":
            args[cmd_args[i]] = cmd_args[i+1] 
    return args


def print_counts(counts):
    """
    Prints results of the counts for the number of primers matched to sequences.

    :param counts: Dictionary of counts
    """
    print("Number of Total Unaligned Amplicons: " + str(counts['total']))
    print("\tTotal Number of forward primers matched to all unaligned sequences: " \
                            + str(counts['fp_total']) \
                            + "  (%.2f" % (float(counts['fp_total']) / counts['total'] * 100) + "%)")
    print("\tTotal number of reverse primers matched to all unaligned sequences: " \
                            + str(counts['rp_total']) \
                            + "  (%.2f" % (float(counts['rp_total']) / counts['total'] * 100) + "%)")
    print("Number of unique unaligned amplicons: " + str(counts['total_unique']))
    print("\tNumber of forward primers matched to unique unaligned sequences: " \
                            + str(counts['unique_fp']) \
                            + "  (%.2f" % (float(counts['unique_fp']) / counts['total_unique'] * 100) + "%)")
    print("\tNumber of reverse primers matched to unique unaligned sequences: " \
                            + str(counts['unique_rp']) \
                            + "  (%.2f" % (float(counts['unique_rp']) / counts['total_unique'] * 100) + "%)")


def print_usage():
    """
    Prints the usage statement to the screen.
    """
    usage = "The purpose of this program is to find the unaligned amplicons\n"
    usage += "that the Bowtie2 software was unable to align. Default input\n"
    usage += "files are given and can be found in 'given/input_given/'. You\n"
    usage += "can supply your own files too by passing them in on the command\n"
    usage += "line. To pass in the results from the Bowtie2 software, use the\n"
    usage += "--bowtie2_rslt_path tag followed by the filepath to the .bam file.\n"
    usage += "Please note that the respective .bam.bai file is also needed to read\n" 
    usage += "these results. To provide a different set of primers to match, use\n"
    usage += "the --primers_path followed by the filepath to the xlsx file\n"
    usage += "holding the primers. You can also specify the output excel\n"
    usage += "files by using the --output_NS_pairs, --output_NS_list, and\n" 
    usage += "--heat_map tags filepaths and name for the output files for\n" 
    usage += "the NS pairs, the NS list, and the heat map resppectively.\n\n"
    usage += "Usage:\n"
    usage += "  find_unaligned_amplicon_primers.py --bowtie2_rslt_path <filepath to Bowtie2 results>\n"
    usage += "                                     --primers_path <filepath to the .xlsx file holding the primers>\n"    
    usage += "                                     --output_NS_pairs <path to NS Pairs excel file>\n" 
    usage += "                                     --output_NS_list <path to NS List excel file>\n" 
    usage += "                                     --heat_map <path to the heat map>\n" 
    print(usage)


def read_primers(primers_filepath):
    """
    Reads primers from primers.xlsx

    :param filepath: The path to the primers excel file
    """    
    # Read in primers for excel file
    primers_df = pd.read_excel(primers_filepath)
    # Dictionary to contain primers
    primers =   {
                    'forward_primers' : [],
                    'reverse_primers' : [],
                }
    # Read in the Primers
    for ind in primers_df.index:
        index = int(primers_df['index'][ind])
        primers['forward_primers'] += [Forward_Primer(primers_df['fP'][ind], index)]
        primers['reverse_primers'] += [Reverse_Primer(primers_df['rP'][ind], index)]
    # Sort primers to make searching faster
    primers['forward_primers'].sort()
    primers['reverse_primers'].sort()
    return primers


def update_counts(counts, fP, rP, unique):
    """
    Increments counts for matching the primer to sequences.

    :param counts: Dictionary of counts that are being kept track of.
    :param fP: The forward primer found
    :param rP: The reverse primer found
    :param unique: Bool indicating if sequence is unique
    :return: Updated counts in counts dict
    """
    # Update counts for unique sequences
    if unique:
        # Update counts for forward primers found
        if fP is not None:
            counts['fp_total'] += 1
            counts['unique_fp'] += 1
        # Update counts for reverse primers found
        if rP is not None:
            counts['unique_rp'] += 1
            counts['rp_total'] += 1
        # Update counts for total unique sequences
        counts['total'] += 1
        counts['total_unique'] += 1
    # Update counts for non unique sequences
    else:
        # Update counts for forward primers found
        if fP is not None:
            counts['fp_total'] += 1
        # Update counts for reverse primers found
        if rP is not None:
            counts['rp_total'] += 1
        # Update counts for total sequences
        counts['total'] += 1
    return counts
