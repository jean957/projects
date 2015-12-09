#!/usr/bin/python

import easygui as gui

def showerror():
	gui.msgbox('Something went wrong\nMake sure you entered the correct numbers!', 'Error', 'OK')

def Showanswer(grid):
	Answer = ''
	for cell in range(81):
		if cell%9 == 0:
			if cell != 0:
				Answer += '\n'
			Answer += 'Line %s >> |' % (cell/9)
		Answer += str(grid[cell][0])
		Answer += '|'
	gui.codebox('This should be the solution', 'Answer', Answer)
	exit()

def simpleremove(block, cell, blockgrid, grid, known, solved):
	if cell in solved[block]:
		return None
	for i in range(9):
		try:
			blockgrid[block][cell].remove(i+1)
		except:
			pass
	for ce in range(9):
		try:
			blockgrid[block][ce].remove(known)
		except:
			pass
	for ce in range(9):
		try:
			grid[27*(block/3)+9*(cell/3)+ce].remove(known)
		except:
			pass
		try:
			grid[3*(block%3)+(cell%3)+ce*9].remove(known)
		except:
			pass
	blockgrid[block][cell].append(known)
	solved[block].append(cell)

def contradictremove(block, cell, grid, blockgrid):
	solved = []
	for i in range(9):
		solved.append([])
	val = blockgrid[block][cell][0]
	testgrid, testblockgrid = [], []
	for i in range(9):
		testblockgrid.append([])
	for i, ce in enumerate(grid):
		testgrid.append(list(ce))
		testblockgrid[((i/3)%3)+(i/27)*3].append(testgrid[-1])
	simpleremove(block, cell, testblockgrid, testgrid, val, solved)
	for i in range(120):
		for testblock in range(9):
			for testcell in range(9):
				if len(testblockgrid[testblock][testcell]) == 1:
					simpleremove(testblock, testcell, testblockgrid, testgrid, testblockgrid[testblock][testcell][0], solved)
		if i%6 == 5:
			blocksearch(testblockgrid, testgrid, solved)
			collinsearch(testblockgrid, testblock)
		if i%15 == 14:
			contradicted = False
			currentlen = 2
			while not contradicted:
				for testblock in range(9):
					for testcell in range(9):
						if len(testblockgrid[testblock][testcell]) == currentlen:
							contradicted = contradictremove(testblock, testcell, testgrid, testblockgrid)
							if contradicted:
								testblockgrid[testblock][testcell].remove(contradicted)
								break
					if contradicted:
						break
				currentlen += 1
				if currentlen == 10:

					break
		if i%15 == 13:
			for testblock in range(9):
				for testcell in range(9):
					if len(testblockgrid[testblock][testcell]) == 0:
						return val
			for n in range(9):
				if len(solved[n]) == 9:
					if n == 8:
						Showanswer(testgrid)
						for wincell in range(81):
							if wincell%9 == 0:
								print '\n Line %s >> |' % (wincell/9),
							print testgrid[wincell], '|',
						print ''
						exit()
				else:
					break
	return False


def blocksearch(blockgrid, grid, solved):
	return 0
	for block in range(9):
		for i in range(1, 10):
			counter = 0
			for cell in range(9):
				if i in blockgrid[block][cell]:
					if len(blockgrid[block][cell]) == 1:
						break
					counter += 1
			if counter == 1:
				for cell in range(9):
					if i in blockgrid[block][cell]:
						simpleremove(block, cell, blockgrid, grid, i, solved)
			

def collinsearch(blockgrid, grid):
	return 0
	for i in range(1, 10):
		for block in range(9):
			lintracker = [0, True, 0]
			coltracker = [0, True, 0]
			for cell in range(9):
				if i in blockgrid[block][cell]:
					if lintracker[0] == 0:
						lintracker[2] == cell/3
					else:
						if lintracker[2] != cell/3:
							lintracker[1] == False
					lintracker[0] += 1
					if coltracker[0] == 0:
						coltracker[2] == cell%3
					else:
						if coltracker[2] != cell%3:
							coltracker[1] == False
					coltracker[0] += 1
			if lintracker[1]:
				for n in range(3):
					if 3*(block/3) + n != block:
						for m in range(3):
							try:
								blockgrid[3*(block/3) + n][m+lintracker[2]*3].remove(i)
							except:
								pass
			if coltracker[1]:
				for n in range(3):
					if block%3 + 3*n != block:
						for m in range(3):
							try:
								blockgrid[block%3 + 3*n][3*m+coltracker[2]].remove(i)
							except:
								pass


def inputcheck(userinput):
	for line in userinput:
		for num in line:
			try:
				int(num)
			except:
				showerror()
				return False
		if len(line) != 9:
			showerror()
			return False
	return True

solved = []

for i in range(9):
	solved.append([])


grid, blockgrid, mycell = [], [], []

for i in range(9):
	mycell.append(1+i)
	blockgrid.append([])


Lines = []
msg = 'Enter the known lines from your Sudoku\nEnter 0 for empty fields\nE.g.: Line1 001053000'
for i in range(9):
	curnum = str(i+1)
	curline = 'Line%s: ' % curnum
	Lines.append(curline)
userinput = []
while True:
	userinput = gui.multenterbox(msg, "Jdoku Version 2.3", Lines)
	if inputcheck(userinput):
		break


for line in range(9):
	userinp = list(userinput[line])
	for cell in range(9):
		i = 9*line+cell
		if userinp[cell] == '0':
			grid.append(list(mycell))
		else:
			grid.append([int(userinp[cell])])
		blockgrid[((i/3)%3)+(i/27)*3].append(grid[-1])


for i in range(150):
	for block in range(9):
		for cell in range(9):
			if len(blockgrid[block][cell]) == 0:
				showerror()
			if len(blockgrid[block][cell]) == 1:
				simpleremove(block, cell, blockgrid, grid, blockgrid[block][cell][0], solved)
	if i%6 == 5:
		blocksearch(blockgrid, grid, solved)
		collinsearch(blockgrid, block)
	if i%15 == 14:
		contradicted = False
		currentlen = 2
		while not contradicted:
			for block in range(9):
				for cell in range(9):
					if len(blockgrid[block][cell]) == currentlen:
						contradicted = contradictremove(block, cell, grid, blockgrid)
						if contradicted:
							blockgrid[block][cell].remove(contradicted)
							break
				if contradicted:
					break
			currentlen += 1
			if currentlen == 10:
				break
	if i%15 == 13:
		for n in range(9):
			if len(solved[n]) == 9:
				if n == 8:
					Showanswer(grid)
			else:
				break




showerror()



