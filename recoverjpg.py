#!/usr/bin/python

'''
This is a commandline tool intended to recover jpg images from accidentaly formatted Harddrives

Dependencies: 
- bitarray (see: https://pypi.python.org/pypi/bitarray/)
- jpeginfo (linux commandline tool)

It only works if the image files were stored in one continuous chunk on the file system
Sorting through 1GB of data with jpgs takes about 10min with a 2Ghz core

Try to find headers and footer for the jpg files.
Look for first header, than look in the next 6.5mb for footers.
for each footer check with jpeginfo whether the data from
header to footer creates a valid image.
'''

from bitarray import bitarray
from time import time
from os import system
#from subprocess import check_output

header, footer = bitarray(), "\xff\xd9"
header.frombytes("\xff\xd8\xff\xe1\xff\xfeExif")
infile = open(raw_input('enter hdd location (e.g.: /dev/sdc) >> '), 'r')
outloc = raw_input('enter folder location for retrieved jpgs (e.g.: /home/USER/recovered) >> ')

def nextpot(infile, inbits, header):
	
	inbits = inbits[1:]
	
	while True:
		
		head = inbits.search(header, 1)
		
		if head == []:
			if infile.read(1) == '':
				infile.close()
				exit()
				
			infile.seek(infile.tell()-1)
			
			inbits = inbits[-15:]
			inbits.frombytes(infile.read((52*10**6-15)/8))
		
		else:
			inbits = inbits[head[0]:]
			if len(inbits) < 52*10**6:
				inbits.frombytes(infile.read((52*10**6-len(inbits))/8))
			
			return inbits

def findjpgs(inbytes, footer):
	
	curft = 0
	
	while True:
		
		curft = inbytes.find(footer, curft+2)
	
		if curft == -1:
			break
	
		yield inbytes[:curft+2]

def writejpgs(jpg, jpgnum):
	
	pic = outloc+'/pic%d.JPG' % jpgnum
	out = open(pic, 'w')
	out.write(jpg)
	out.close()

	return system('jpeginfo -cd %s' % pic) == 0

inbits, jpgnum = bitarray(), 1
infile.seek(0,2); length = infile.tell(); infile.seek(0)
t = time()

# infile.seek(x) ; jpgnum = y			# x and y are offsets for restarting the recovery in case it was interrupted at some point

while True:
	
	print 'time: %d' % int(time()-t), 'progress: %d%%' % (infile.tell()*100/length), 'byte: %d' % infile.tell()
	
	inbits = nextpot(infile, inbits, header)
	
	for jpg in findjpgs(inbits.tobytes(), footer):
		
		if writejpgs(jpg, jpgnum):
			inbits = inbits[len(jpg)*8-1:]
			jpgnum += 1
			break