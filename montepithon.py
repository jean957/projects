#!/usr/bin/python

ran = open("/dev/urandom", 'r')

precision = int(raw_input("enter desired precision (no of bytes to create grid from) > ")) # 2 ?
accuracy = int(raw_input("enter desired accuracy (no of random spots in the grid) > ")) # 100k ?


def randist():
	dist = 0
	for i in range(precision):
		dist += ord(ran.read(1)) * 256 ** i
	return dist

def run():
	inside, outside, hit = 0,0,0
	squaredr = (256 ** precision - 1) ** 2
	for check in range(accuracy):
		cur = randist() ** 2 + randist() ** 2
		if cur < squaredr:
			inside += 1
		elif cur > squaredr:
			outside += 1
		else:
			hit += 1
	print "inside the circle: ", inside
	print "outside the circle: ", outside
	print "hit the edge of the circle: ", hit
	print "Hitting the circle edge means the precision is too low and the result will be too small on average"
	return float(inside + hit/2) / (accuracy + hit/2)

	
print run() * 4



