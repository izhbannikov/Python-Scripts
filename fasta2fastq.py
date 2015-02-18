import sys
from Bio.SeqIO.QualityIO import PairedFastaQualIterator
from Bio import SeqIO

handle = open(sys.argv[-1], "w")
records = PairedFastaQualIterator(open(sys.argv[-3]), open(sys.argv[-2]))
count = SeqIO.write(records, handle, "fastq")
handle.close()
print "Converted %i records" % count