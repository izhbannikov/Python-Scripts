# -*-coding=utf8-*-
__author__="Ilya Y Zhbannikov"

"""
This script extracts variable (marker) regions from given 16S database file and writes 
results to output file specified.
Example: python -d [-database] database.fasta -s [-start] -e [-end] -o output.fasta 
"""

from Bio import SeqIO, Seq
import argparse # https://docs.python.org/2/library/argparse.html#module-argparse
import os, sys
import time

def read_reference(filename=""):
	try:
		handle = open(filename, mode='rU')
		records = []
		for record in SeqIO.parse(handle, "fasta"):
			records.append(record)
		handle.close()
		return records
	except IOError:
		print "Error opening input file: %s\n" % filename
		sys.exit()
		
def write_output(output, records):
	outfile = output
	hangle = open(output, 'w')
	SeqIO.write(records, hangle, 'fasta')
      

def extract(output, ref, startpos, endpos):
	# Reading input file (16S database):
	db = read_reference(ref)
	# Parsing records, extracting variable (marker) regions:
	for i in range(len(db)):
		db[i] = db[i][int(startpos):int(endpos)]
		
	write_output(output, db)
		

def main():
	start = time.time()
	# Setup the parameters:
	parser = argparse.ArgumentParser(prog='varextract.py', usage='%(prog)s -o [--output] -r [--ref] <reference 16S seqs> -s [--start] <start position> -e [--end] <end position>') # argparse parser initialization
   	# Adding arguments:
   	parser.add_argument("-o", "--output", dest="output",action="store", help="Output directory", required=True)
   	# Reference libraries:
   	parser.add_argument("-r", "--ref", dest="ref", action="store", help="Reference 16S database", required=True)
   	parser.add_argument("-s", "--start", dest="start", help="Starting position of variable (marker) region", action="store", required=True)
   	parser.add_argument("-e", "--end", dest="end", help="End position of variable (marker) region", action="store")
	
	args = parser.parse_args()
	
	# Extraction routine:
	extract(args.output, args.ref, args.start, args.end)
	
if __name__ == '__main__' :
	main() # Call the main function
	