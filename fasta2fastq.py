import sys
from Bio.SeqIO.QualityIO import PairedFastaQualIterator
from Bio import SeqIO
import csv
import argparse





def fasta2fastq(output, fasta, qual, clipfile) :
	handle = open(output, "w")
	records = PairedFastaQualIterator(open(fasta), open(qual))
	count = 0
	if clipfile == None :
		count = SeqIO.write(records, handle, "fastq")
	else :
		clip_points = []
		with open(clipfile, 'rb') as csvfile:
			clips = csv.reader(csvfile, delimiter=',')
			clips.next()
			for row in clips:
				clip_points.append([int(row[1]), int(row[2])])
		trimmed_records = []
		i = 0
		for record in records :
			trimmed_record = record[(clip_points[i][0]-1):(clip_points[i][1]-1)]
			trimmed_records.append(trimmed_record)
			i += 1
		count = SeqIO.write(trimmed_records, handle, "fastq")
	handle.close()
	print "Converted %i records" % count


def main():
	#start = time.time()
	
	# Parsing command-line variables
	parser = argparse.ArgumentParser(prog='fasta2fastq.py', usage='%(prog)s -o [--output] -f [--fasta] <FASTA file> -q [--qual] <QUAL file> -c [--clip] <CSV file with clip points>') # argparse parser initialization
   	# Adding arguments:
   	parser.add_argument("-o", "--output", dest="output",action="store", help="Output directory.", required=True)
   	# Reference libraries:
   	parser.add_argument("-f", "--fasta", dest="fasta", action="store", help="FASTA file.", required=True)
   	parser.add_argument("-q", "--qual", dest="qual", help="QUAL file", action="store", required=True)
   	parser.add_argument("-c", "--clip", dest="clip", help="CSV file with clip points", action="store")
   	# Getting args from command line:
   	args = parser.parse_args()
   	
   	# If everything is ok, run the metamp script:
	#try :
	fasta2fastq(args.output, args.fasta, args.qual, args.clip)
		#done = time.time()
		#elapsed = done - start
		#print "Elapsed time:", elapsed
	#except :
	#	print "Can't run. Something wrong."
		#done = time.time()
		#elapsed = done - start
		#print "Elapsed time:", elapsed
	#	sys.exit(2)
		
if __name__ == '__main__' :
	main() # Call the main function