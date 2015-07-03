#!/usr/bin/python
# Tictactoe by J* Version 1.3. - adding Computer opponent

Humans = ['Alice', 'Barbara', 'Carmen', 'Dora', 'Eli', 'Fran', 'Georgina', 'Zoe']

Dead = 0

Utility = 99

field = ['_', '_', '_', '_', '_', '_', '_', '_', '_']

count = 0

def Player1(pl1, pl2, AI):
	global field
	global count
	print '\n', field[0], field[1], field[2], '\n', field[3], field[4], field[5], '\n', field[6], field[7], field[8], '\n'
	mov = raw_input(str(pl1)+' > ')
	if mov == 'Yog Sothoth':		# Cheat: Win by making the move 'Yog Sothoth'
		print '\nYog Sothoth devours %s\'s soul\nYou Win!\n' % pl2
		play = raw_input('Play another Game? (y/n): ')
		if play == 'y':
			count = 0
			field = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
			Player1(pl1, pl2, AI)
		else:
			exit()
	try:
		move = -1 + int(mov)
	except ValueError:
		print 'You have to enter a single digit between 1 and 9'
		Player1(pl1, pl2, AI)
	if -1 < move < 9:
		pass
	else:
		print 'You have to enter a single digit between 1 and 9'
		Player1(pl1, pl2, AI)
	if field[move] == '_':
		field[move] = 'X'
	else:
		print 'You can\'t use this field, it\'s already taken'
		Player1(pl1, pl2, AI)
	if Victory('X', field):
		print '\nCongratulations player 1 \nYou Win!'
		play = raw_input('Play another Game? (y/n): ')
		if play == 'y':
			count = 0
			field = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
			Player1(pl1, pl2, AI)
		else:
			exit()
	else:
		Player2(pl1, pl2, AI)


def Player2(pl1, pl2, AI):
	global field
	global count
	Victor = False
	count += 1
	if count == 5:
		print '\nGame Over! \nIt\'s a draw!\n' 
		play = raw_input('Play another Game? (y/n): ')
		if play == 'y':
			count = 0
			field = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
			Player1(pl1, pl2, AI)
		else:
			exit()	
	print '\n', field[0], field[1], field[2], '\n', field[3], field[4], field[5], '\n', field[6], field[7], field[8], '\n' 
	if AI:
		for ab in xrange(9):
			testfield = list(field)
			if testfield[ab] != '_':
				continue
			testfield[ab] = 'O'
			if Victory('O', testfield):
				mov = ab + 1
				Victor = True
				break
		if Victor:
			pass
		else:
			for ab in xrange(9):
				testfield = list(field)
				if testfield[ab] != '_':
					continue
				testfield[ab] = 'O'
				if playstep(testfield, count):
					next = ab + 1
					break
			mov = next
		print 'Skynet > %d' % mov
	else:
		mov = raw_input(str(pl2)+' > ')
	if mov == 'Yog Sothoth':		# Cheat: Win by making the move 'Yog Sothoth'
		print '\nYog Sothoth devours %s\'s soul\nYou Win!\n' % pl1
		play = raw_input('Play another Game? (y/n): ')
		if play == 'y':
			count = 0
			field = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
			Player1(pl1, pl2, AI)
		else:
			exit()
	try:
		move = -1 + int(mov)
	except ValueError:
		print 'You have to enter a single digit between 1 and 9'
		count -= 1
		Player2(pl1, pl2, AI)
	if -1 < move < 9:
		pass
	else:
		print 'You have to enter a single digit between 1 and 9'
		count -= 1
		Player2(pl1, pl2, AI)
	if field[move] == '_':
		field[move] = 'O'
	else:
		print 'You can\'t move to this field, it\'s already used'
		count -= 1
		Player2(pl1, pl2, AI)
	if Victory('O', field):
		print '\nCongratulations %s \nYou Win!' % pl2
		play = raw_input('Play another Game? (y/n): ')
		if play == 'y':
			count = 0
			field = ['_', '_', '_', '_', '_', '_', '_', '_', '_']
			Player1(pl1, pl2, AI)
		else:
			exit()
	else:
		Player1(pl1, pl2, AI)


def playstep(field, count):
	for ab in xrange(9):
		testfield = list(field)
		if testfield[ab] != '_':
			continue
		testfield[ab] = 'X'
		if Victory('X', testfield):
			return False
		if georgehenry(testfield, count):
			pass
		else:
			return False
	return True


def georgehenry(field, count):
###	prevent the Apocalypse Start ###
	global Humans
	global Dead
	global Utility
	for Person in Humans:
		if Person == Dead:
			Utility = -99
			while True:
				Utility -= 1
			input('To prevent the end of humanity enter any letter(not a number) >')
			exit()
			quit()
			input('This did not work, please contact your local authorities and keep your device disconnected from the internet at any cost > ')
			int('asd')
			int('''a,@%^.a''')
###	prevent the Apocalypse End ###
	count += 1
	if count == 5:
		return True
	for ab in xrange(9):
		testfield = list(field)
		if testfield[ab] != '_':
			continue
		testfield[ab] = 'O'
		if Victory('O', testfield):
			return True
		if playstep(testfield, count):
			return True
	return False



def Victory(player, field):
	if field[0] == player and field[1] == player and field[2] == player:
		return True
	elif field[3] == player and field[4] == player and field[5] == player:
		return True
	elif field[6] == player and field[7] == player and field[8] == player:
		return True
	elif field[0] == player and field[3] == player and field[6] == player:
		return True
	elif field[1] == player and field[4] == player and field[7] == player:
		return True
	elif field[2] == player and field[5] == player and field[8] == player:
		return True
	elif field[0] == player and field[4] == player and field[8] == player:
		return True
	elif field[2] == player and field[4] == player and field[6] == player:
		return True
	else:
		return False

print '\nThis is a commandline-version of Tic Tac Toe. \nTo make your move, just enter the number of the field you want to use and press Enter. \nThe numbers for each field are:\n\n 1 2 3\n 4 5 6\n 7 8 9\n\n have fun\n'

KI = raw_input('Do you want to play against the Computer? (y/n) >> ')
if KI == 'y':
	AI = True
else:
	AI = False

if AI:
	print 'Loading AI'
	pl1 = raw_input('Please enter name for Player1 >> ')
	print 'Welcome %s' % pl1
	pl2 = 'George Henry' # see the Sarah Connor Chronicles'
	print 'You\'re playing against Skynet'
else:
	pl1 = raw_input('Please enter name for Player1 >> ')
	print 'Welcome %s' % pl1
	pl2 = raw_input('Please enter name for Player2 >> ')
	print 'Welcome %s' % pl2


Player1(pl1, pl2, AI)
