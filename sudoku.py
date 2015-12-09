# How to solve sudokus


def simpleremove(block, cell, blockgrid, grid, known, solved):		# if there is a known number, this removes the number from block, line and column
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

def contradictremove(block, cell, grid, blockgrid, count):			# this trys possible numbers and returns the first that creates a contradiction
	count += 1
#	print count
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
							contradicted = contradictremove(testblock, testcell, testgrid, testblockgrid, count)
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
								


solved = []

for i in range(9):
	solved.append([])


grid, blockgrid, mycell = [], [], []

for i in range(9):
	mycell.append(1+i)
	blockgrid.append([])

for i in range(81):
	grid.append(list(mycell))
	blockgrid[((i/3)%3)+(i/27)*3].append(grid[-1])		# This creates 2 grids (ordered by blocks and a simple list)


for block in range(9):
	for cell in range(9):
		try:
			simpleremove(block, cell, blockgrid, grid, input('Block%s, Cell%s:' % (block+1, cell+1)), solved)
		except (SyntaxError, NameError):
			pass



for i in range(150):
	for block in range(9):
		for cell in range(9):
			if len(blockgrid[block][cell]) == 0:
				print 'Sorry, I couldn\'t find a solution.'
				print 'Are you sure you entered the correct numbers?'
				print 'Are you sure this has an actual solution?'
				exit()
			if len(blockgrid[block][cell]) == 1:
				simpleremove(block, cell, blockgrid, grid, blockgrid[block][cell][0], solved)
	if i%6 == 5:
		blocksearch(blockgrid, grid, solved)
		collinsearch(blockgrid, block)
	if i%15 == 14:
#		import ipdb ; ipdb.set_trace()
		contradicted = False
		currentlen = 2
		while not contradicted:
			for block in range(9):
				for cell in range(9):
					if len(blockgrid[block][cell]) == currentlen:
						contradicted = contradictremove(block, cell, grid, blockgrid, 0)
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
					for cell in range(81):
						if cell%9 == 0:
							print '\n Line %s >> |' % (cell/9),
						print grid[cell], '|',
					print ''
					exit()
			else:
				break




print 'Are you sure you entered the correct numbers?'
print 'Are you sure this has an actual solution?'
print 'This is as far as I got!'
for cell in range(81):
	if cell%9 == 0:
		print '\n Line %s >> |' % (cell/9),
	print grid[cell], '|',
print ''



