#!/usr/bin/python
# dependencies: espeak, sox

from os import system
from sys import argv
from time import sleep

Help = '''\nUse: if you add the name of a file as an argument when you call morseconv (e.g.: > python morseconv.py file)
it will translate the file either to or from morse and write it to a new file 'file.morse'.
For filetranslation, you can add the option '-s' or '--sound' to enable sound (Default is disabled)
(note that it has to be 'clean' morsecode to be recognized as such, so only spaces, dots and minus are allowed,
you start a new letter with exactly one space and a new word with exactly two spaces)

If you call morseconv without any arguments you get a commandline interface where you can choose if you want
to translate to, or from morse, and then just enter whatever you want and get it translated.
(if you enter > ::m you get back to the menu, if you enter > ::q you quit the programm)\n'''

morse = ['.-', '-...', '-.-.', '-..', '.', '..-.', '--.', '....', '..', '.---', '-.-', '.-..', '--', '-.', '---', '.--.', '--.-', '.-.', '...', '-', '..-', '...-', '.--', '-..-', '-.--', '--..', '-----', '.----', '..---', '...--', '....-', '.....', '-....', '--...', '---..', '----.',  ' ', '.-.-', '--..--', '---...', '..--..', '.----.', '-..-.', '-.--.', '-.--.-', '.--.-.', '-...-']
text = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '\n', ',', '.', '?', '\'', '/', '(', ')', '@', '=']


def createdicts(morse, text):
	mdict, tdict = {}, {}
	for i, val in enumerate(morse):
		mdict[val] = text[i]
		tdict[text[i]] = val
	return mdict, tdict

def sound(dur, freq):
	system('play --no-show-progress --null --channels 1 synth %s sine %s' % (dur, freq))

def speech(text):
	system('espeak "%s"' % text)

def playmorse(convstr):
	freq = 500
	morsedict = {'.' : 0.1, '-' : 0.3}
	for char in convstr:
		if char == ' ':
			sleep(0.3)
		else:
			sound(morsedict[char], freq)
			sleep(0.1)

def convmorse(line, mdict, sound='off'):
	convstr, curstr = '', ''
	for char in line:
		if char == ' ':
			if curstr == '':
				convstr += ' '
				continue
			try:
				convstr += mdict[curstr]
			except KeyError:
				pass
			curstr = ''
		else:
			curstr += char
	if curstr != '':
		try:
			convstr += mdict[curstr]
		except KeyError:
			pass
		curstr = ''
	if sound == 'on':
		speech(convstr)
	return convstr

def convtext(line, tdict, sound='off'):
	convstr = ''
	for char in line:
		try:
			convstr += tdict[char]+' '
		except KeyError:
			pass
	if sound == 'on':
		playmorse(convstr)
	return convstr

def fileconv(argv, morse, text):
	mdict, tdict = createdicts(morse, text)
	orig = open(argv[1], 'r')
	tran = open(argv[1]+'.morse', 'w')
	kind = 'm'
	if len(argv) > 2 and argv[2] == 'sound':
		sound = 'on'
	for char in orig.read(100):
		if char in text and char != ' ':
			kind = 't'
			break
	orig.seek(0)
	if kind == 't':
		for line in orig:
			tran.write(convtext(line.lower(), tdict, sound))
	else:
		for line in orig:
			tran.write(convmorse(line, mdict, sound))
	orig.close()
	tran.close()
	exit()

def cmdinterface(morse, text):
	mdict, tdict = createdicts(morse, text)
	while True:
		sound = 'on'
		print '''\nMenu:
		Enter 'm' to translate morse to regular text - you can enter '::m' to return to this menu
		Enter 't' to translate regular text to morse - you can enter '::m' to return to this menu
		Enter '::q' to leave
		Enter '::h' for help
		Enter '::ch' for the list of translatable characters
		Enter '::s' to turn sound off or on (current: %s)''' % sound
		choice = raw_input('>> ')
		if choice == '::q':
			exit()
		elif choice == '::s':
			if sound == 'on':
				sound = 'off'
			else:
				sound = 'on'
		elif choice == '::h':
			print Help
		elif choice == '::ch':
			print ''
			for char in text:
				print char,
			print ''
		elif choice == 'm':
			while True:
				utext = raw_input('>> ')
				if utext == '::m':
					break
				if utext == '::q':
					exit()
				elif utext == '::ch':
					print ''
					for char in text:
						print char,
					print ''
					continue
				print convmorse(utext, mdict, sound)
		elif choice == 't':
			while True:
				utext = raw_input('>> ')
				if utext == '::m':
					break
				if utext == '::q':
					exit()
				elif utext == '::ch':
					print ''
					for char in text:
						print char,
					print ''
					continue
				print convtext(utext.lower(), tdict, sound)
		else:
			'That\'s not so hard, try again'

if len(argv) > 1:
	fileconv(argv, morse, text)
else:
	cmdinterface(morse, text)


