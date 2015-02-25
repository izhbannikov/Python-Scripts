#this script reads in a lucy result file and produces a set of output files:
# lucy_clips.csv
# lucy_clipped.fasta 
#>GKF1FGD02EGOM3 0 0 0 1 79
#gactacacgtagtatCTCAATGATTCATACAGCTTCACATCGAGAGCAT

import sys
import numpy
def median(lst):
	return numpy.median(numpy.array(lst))

inf = open(sys.argv[-2], mode='r')

lclips =  open(sys.argv[-1] + "_lucy_clips.csv", mode='w')
lclips.write("ID,lclip,rclip\n")

lclipped =  open(sys.argv[-1] + "_lucy_clipped.fasta", mode='w')

id = "" #read ID
seq = "" #sequence
lclip = 0
rclip = 0
errors = 0
counter = 0
min_lclip=0
avg_left_trim = []
avg_right_trim = []

#The outer for loop iterates through all lines in the input file
for line in inf:
  if(line[0] == '>'):
    #first if is a special case for the first line
    if(id == ""):
      pieces = line.strip().split(" ")
      id = pieces[0]
      lclip = int(pieces[4])
      #if(lclip < min_lclip): lclip = 16 #first 16 are tag and 454 bases
      rclip = int(pieces[5])
      if(id == ''):
        errors += 1
    else:
      avg_left_trim.append(lclip)
      avg_right_trim.append(len(seq)-rclip)
      lclips.write("%s,%s,%s\n" % (id[1:],lclip,rclip))
      lclipped.write("%s\n%s\n" %(id,seq[lclip-1:rclip-1]))
      counter += 1
      if(counter % 1000 == 0):
        print("Total records %s" % (counter))
      seq = ""
      pieces = line.strip().split(" ")
      id = pieces[0]
      lclip = int(pieces[4])
      #if(lclip < 16): lclip = 16
      rclip = int(pieces[5])
      if(id == ''):
        errors += 1  
  else:
    seq += line.strip()  


#take care of last line:
seq += line.strip("\n")
#write last record
lclips.write("%s,%s,%s\n" % (id[1:],lclip,rclip))
lclipped.write("%s\n%s\n" %(id,seq[lclip-1:rclip-1]))
counter += 1


lclips.close()   
lclipped.close()

print("Total records %s.  Total errors %s" %(counter, errors))
print("Average left trim: %s, right trim: %s" %(sum(avg_left_trim)/len(avg_left_trim), sum(avg_right_trim)/len(avg_right_trim)))
print("Median left trim: %s, right trim: %s" %(median(avg_left_trim), median(avg_right_trim)))
