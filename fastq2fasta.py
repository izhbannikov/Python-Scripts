# Converts FASTQ file to FASTA and QUAL (2 files in total)
# Usage: python fastq2fasta <input fastq file> <output prefix>

import sys
from Bio import SeqIO
from Bio.Alphabet import generic_dna

if sys.argv[-1] == None :
	out_prefix = "reads"
else :
	out_prefix = sys.argv[-1]

SeqIO.convert(sys.argv[-2],"fastq",out_prefix+".fasta","fasta", alphabet=generic_dna)
SeqIO.convert(sys.argv[-2],"fastq",out_prefix+".qual","qual", alphabet=generic_dna)