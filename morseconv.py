from sys import argv

Help = '''\nUse: if you add the name of a file as an argument when you call morseconv (e.g.: > python morseconv.py file)
it will translate the file either to or from morse and write it to a new file 'file.morse'.
(note that it has to be 'clean' morsecode to be recognized as such, so only spaces, dots and minus are allowed)

If you call morseconv without any arguments you get a commandline interface where you can choose if you want
to translate to, or from morse, and then just enter whatever you want and get it translated.
(if you enter > ::m you get back to the menu, if you enter > ::q you quit the programm)\n'''

morse = ['.-   ', '-...   ', '-.-.   ', '-..   ', '.   ', '..-.   ', '--.   ', '....   ', '..   ', '.---   ', '-.-   ', '.-..   ', '--   ', '-.   ', '---   ', '.--.   ', '--.-   ', '.-.   ', '...   ', '-   ', '..-   ', '...-   ', '.--   ', '-..-   ', '-.--   ', '--..   ', '-----   ', '.----   ', '..---   ', '...--   ', '....-   ', '.....   ', '-....   ', '--...   ', '---..   ', '----.   ',  '    ', '.-.-   ', '--..--   ', '---...   ', '..--..   ', '.----.   ', '-..-.   ', '-.--.   ', '-.--.-   ', '.--.-.   ', '-...-   ']
text = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' ', '\n', ',', '.', '?', '\'', '/', '(', ')', '@', '=']
mdict, tdict = {}, {}
for i, val in enumerate(morse):
	mdict[val] = text[i]
	tdict[text[i]] = val

def convmorse(line, mdict):
	convstr = ''
	curstr = ''
	count = 0
	for char in line:
		if char == ' ':
			count += 1
		curstr += char
		if count == 3 and len(curstr) > 3:
			convstr += mdict[curstr]
			curstr, count = '', 0
		elif count == 4:
			convstr += ' '
			curstr, count = '', 0
	return convstr

def convtext(line, tdict):
	convstr = ''
	for char in line:
		try:
			convstr += tdict[char]
		except:
			pass
	return convstr

if len(argv) > 1:
	orig = open(argv[1], 'r')
	tran = open(argv[1]+'.morse', 'w')
	kind = 'm'
	for char in orig.read(250):
		if char in text and char != ' ':
			kind = 't'
			break
	orig.seek(0)
	if kind == 't':
		for line in orig:
			tran.write(convtext(line.lower(), tdict))
	elif kind == 'm':
		for line in orig:
			tran.write(convmorse(line, mdict))
	else:
		print 'something odd happened'	
	orig.close()
	tran.close()
	exit()

while True:
	print '''\nMenu:
	Enter 'm' to translate morse to regular text - you can enter '::m' to return to this menu
	Enter 't' to translate regular text to morse - you can enter '::m' to return to this menu
	Enter '::q' to leave
	Enter '::h' for help
	Enter '::ch' for the list of translatable characters'''
	choice = raw_input('>> ')
	if choice == '::q':
		exit()
	elif choice == '::h':
		print Help
	elif choice == '::ch':
		print ''
		for char in text:
			print char,
		print ''
	elif choice == 'm':
		while True:
			text = raw_input('>> ')
			if text == '::m':
				break
			if text == '::q':
				exit()
			elif text == '::ch':
				print ''
				for char in text:
					print char,
				print ''
				continue
			print convmorse(text, mdict)
	elif choice == 't':
		while True:
			text = raw_input('>> ')
			if text == '::m':
				break
			if text == '::q':
				exit()
			elif text == '::ch':
				print ''
				for char in text:
					print char,
				print ''
				continue
			print convtext(text.lower(), tdict)
	else:
		'That\'s not so hard, try again'
