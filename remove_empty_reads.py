import sys
from Bio import SeqIO


handle = open(sys.argv[-2], "rU")
records = SeqIO.parse(handle, "fastq")

handle_out = open(sys.argv[-1], "w")
records_out = []
for record in records :
	if len(record.seq) != 0 :
		records_out.append(record)

SeqIO.write(records_out, handle_out, "fastq")
handle_out.close()

handle.close()
