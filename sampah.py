#!/usr/bin/python  
# import urllib
# import urllib2
# import sys, getopt

# def usage():
#     print 'Usage:'
#     print '\tpython test.py -b <blast_file>'

# def main(argv):
# 	blastfile = ''
# 	try:
# 		opts, args =getopt.getopt(argv,"hb:",["blast_file="])
# 	except getopt.GetoptError:
# 		usage()
# 		sys.exit(2)
# 	for opt, arg in opts:
# 		if opt == '-h':
# 			usage()
# 			sys.exit()
# 		elif opt in ("-b", "--blast_file"):
# 			blastfile = arg

# if __name__ == "__main__":
# 	main(sys.argv[1:])


import sys, getopt
# Store input and output file names
ifile=''
ofile=''
 
# Read command line args
myopts, args = getopt.getopt(sys.argv[1:],"i:o:")
 
###############################
# o == option
# a == argument passed to the o
###############################
for o, a in myopts:
    if o == '-i':
        ifile=a
    elif o == '-o':
        ofile=a
    elif o == "":
        print("Usage: %s -i input -o output" % sys.argv[0])
 
# Display input and output file name passed as the args
print ("Input file : %s and output file: %s" % (ifile,ofile) )

