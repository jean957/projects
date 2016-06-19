#!/usr/bin/python

from sys import argv
from math import sqrt

primes = [2, 3, 5, 7]

def appendprimes():
	global primes
	# appends 20 primes to the given list of primes
	# must get a complete list of primes starting with 2 as input
	current = primes[-1] + 2
	count = 0
	while count != 20:
		end = int(sqrt(current))
		prime = primes[0]
		next = 0
		while prime < end:
			prime = primes[next]
			next += 1
			if current % prime == 0:
				current += 2
				break
			if prime >= end:
				primes.append(current)
				current += 2
				count += 1

def smallest_divisible(num):
	smallest_div = 1
	while primes[-1] < num:
		appendprimes()
	for prime in primes:
		powered_prime = prime
		while powered_prime < num:
			smallest_div *= prime
			powered_prime *= prime
	return smallest_div


try:
	if len(argv) == 1:
		print smallest_divisible(1+int(raw_input("enter a number > ")))
	elif len(argv) == 2:
		print smallest_divisible(int(argv[1])+1)
	elif len(argv) == 3 and argv[1] == "lim":
		for i in range(1, int(argv[2])+1):
			print i, smallest_divisible(i+1)
	else:
		for i in (int(x) for x in argv[1:]):
			print i, smallest_divisible(i+1)
except:
	print '''Options:
	- Do not set any arguments: You will be asked to enter a number
	- Specify multiple numbers as arguments to get the results for them
	- Use: "lim <number>" as argument to print all results up to <number>
	'''
	



