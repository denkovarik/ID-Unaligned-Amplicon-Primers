import pysam, sys

filepath = "input_given/input.bam"
if len(sys.argv) > 1:
    filepath = sys.argv[1]

samfile = pysam.AlignmentFile(filepath, "rb")
c = 0
for read in samfile.fetch(until_eof=True):
    if read.is_unmapped:
        print(read)
        print("")
        print(read.get_forward_sequence())
        print("")
        print("")
        c += 1
print("Number of Unaligned Amplicons: " + str(c))
samfile.close()
