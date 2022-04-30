import time

class Node:
	def __init__(self):
		self.right, self.left, self.up, self.down, self.header = None, None, None, None, None
		self.id = None


class HeaderNode(Node):
	def __init__(self):
		super().__init__()
		self.heur = None
		self.binUp, self.binDown = None, None



class DLmatrix():
	def __init__(self):
		self.root = HeaderNode()
		self.root.right, self.root.left, self.root.up, self.root.down, self.root.header = self.root, self.root, self.root, self.root, self.root
		self.root.id = 0
		self.headers = [self.root] 
		self.bins = [HeaderNode() for i in range(10)]
		for node in self.bins:
			node.binUp = node
			node.binDown = node
			#print(node, node.binUp, node.binDown)

		#print(self.root)
		for i in range(0, 324):
			self.addHeaderNode(self.root, i + 1)

		
		

		self.addRows()



	
	def addHeaderNode(self, last, i):
		new = HeaderNode()
		new.heur = 9
		new.id = i
		self.headers.append(new)
		new.header = new
		

		binHead = self.bins[9]



		new.binUp = binHead
		new.binDown = binHead.binDown

		binHead.binDown = new
		new.binDown.binUp = new



		#print(new)
		new.up = new
		new.down = new 
		
		#print(last, last.right)
		leftNode = last
		rightNode = last.right
		
		rightNode.left = new
		new.right = rightNode

		leftNode.right = new
		new.left = leftNode


	def getBestCol(self):
		# cur = self.root.right
		# done = False
		
		# best = cur
		# #if best.heur == 1:
		# #	return best
		# while not done:

		# 	if cur.heur < best.heur:
		# 		best = cur
		# 		if best.heur == 1:
		# 			break
			
			
		# 	cur = cur.right
		# 	if cur == self.root:
		# 		done = True
		


		for node in self.bins:
			if node.binDown != node:
				best = node.binDown
				break

		return best

	def getNthCol(self, n):
		cur = self.root
		done = False
		while not done:

			if cur.id == n:
				return cur
			
			cur = cur.right
			if (cur == self.root):
				done = True
		
		return False

	def createRow(self):
		first = HeaderNode()
		first.left, first.right = first, first

		for i in range(4):
			newNode = Node()

			newNode.left = first
			newNode.right = first.right
			
			first.right = newNode
			newNode.right.left = newNode

		k = 0
		done = 0
		cur = first
		'''while not done:
			print(cur)
			cur = cur.right			
			
			k += 1

			if (cur == first):
				done = 1
		print(k)'''

		return first


	def addRows(self):
		d = {}
		#nodes = 0
		for row in range(9):
			for col in range(9):
				box = row // 3 * 3 + col // 3
				for val in range(9):
					indices =  [0, row * 9 + col + 1, 81 + val * 9 + row + 1, 81 * 2 + val * 9 + col + 1, 81 * 3 + val * 9 + box + 1]
					#print(cols)
					first = self.createRow()
					first.id = (row, col, val)
					cur = first
					for index in indices:

						colHeader = self.getNthCol(index)

						cur.header = colHeader
						cur.up = colHeader
						cur.down = colHeader.down

						colHeader.down = cur
						cur.down.up = cur


						#print(cur, cur.down.up, colHeader.down, cur.up.down, Down.up)
						#print(colHeader, cur.up)
						#print(Down, cur.down)
						#a = input()
						cur = cur.right
						#nodes +=1
		#d2 = {i:d[i] for i in sorted(list(d.keys()))}
		#print(d2)
		#print(nodes)


	#iterate through a row and remove all its Nodes, 
	#returns [NodeRemoved]
	def removeRow(self, rowNode):

		cur = rowNode
		
		removed = []
		while True:
				
			cur.up.down = cur.down
			cur.down.up = cur.up

			removed.append(cur)

			cur = cur.right
			if cur == rowNode:
				break

		#print(removed, len(removed))
		return removed


	#iterate through a column, removing each row \
	#returns the [columnHeader, [removeRow()]]


	def removeCol(self, colNode):
		#print("removeCol2")

		colNode = colNode.header

		done = False
		cur = colNode


		colHeader = None
		removed = []

		rows = set()
		while True:
			#print(cur, cur.up, cur.down)
			#input()

			
			if cur.id is not None:
				#print(cur.id)
				cur.right.left = cur.left
				cur.left.right = cur.right


				cur.binUp.binDown = cur.binDown
				cur.binDown.binUp = cur.binUp



			else:
				rows.add(cur)
				
			cur = cur.down
			if cur == colNode:
				break

		for row in rows:
			removed += self.removeRow(row)


		for remove in removed:
			if remove.id is None:
				cur = remove.header


				cur.heur -= 1

				if cur.header != colNode:
	
					cur.binUp.binDown = cur.binDown
					cur.binDown.binUp = cur.binUp


					binHead = self.bins[cur.heur]

					cur.binUp = binHead
					cur.binDown = binHead.binDown
					
					binHead.binDown = cur
					cur.binDown.binUp = cur

				

	



		
		return [colNode, removed]

	#deletes corresponding rows and cols in DL matrix to set up sudoku board
	def inputBoard(self, board):
		for row in range(9):
			for col in range(9):
				box = row // 3 * 3 + col // 3
				val = board[row][col]
				if val != 0:
					indices =  [row * 9 + col + 1, 81 + (val - 1) * 9 + row + 1, 81 * 2 + (val - 1) * 9 + col + 1, 81 * 3 + (val - 1) * 9 + box + 1]
					for index in indices:

						colHead = self.getNthCol(index)
						if colHead:
							self.removeCol(colHead)


	def restoreMatrix(self, removed):
		#input(removed)
		for remove in removed:
			colHead = remove[0]
			if colHead:
				colHead.left.right = colHead
				colHead.right.left = colHead


				if colHead.binUp.binDown == colHead:

					colHead.binUp.binDown = colHead.binDown
					colHead.binDown.binUp = colHead.binUp


				binHead = self.bins[colHead.heur]
				colHead.binUp = binHead
				colHead.binDown = binHead.binDown
				binHead.binDown = colHead
				colHead.binDown.binUp = colHead

				
			for node in remove[1]:

				if node.id is None:
					cur = node.header
					cur.heur += 1


					if cur.binUp.binDown == cur:
						cur.binUp.binDown = cur.binDown
						cur.binDown.binUp = cur.binUp

					binHead = self.bins[cur.heur]

					cur.binUp = binHead
					cur.binDown = binHead.binDown
					binHead.binDown = cur
					cur.binDown.binUp = cur
				# 	#print("add back")
				node.up.down = node
				node.down.up = node






	def DLX(self, solution = [], depth = 0):
		
		#if there are no more columns --> solution
		#if there are no more rows but there are columns --> terminate unsuccessfully
		#pick a column
		#iterate through the rows in each col
			#append solution
			#iterate through each column in the row 
			#for the nonHeaderCol
				#removeCol
			#DLX
			#restoreCol

		#print(depth)
		if self.root == self.root.right:
			#print("w")
			return True, solution

		else:
			best = self.getBestCol()
			#print(best.heur)

			done = False
			cur = best
			while not done:

				if cur.id is None:
				
					solution.append(cur)					
					removed = []
					


					done2 = False
					cur2 = cur
					while not done2:
						#print(cur2)
						#input(cur2)
						if cur2.id is None:
							removed.append(self.removeCol(cur2))	

						cur2 = cur2.right
						

						if cur2 == cur:
							done2 = True



					result = self.DLX(solution, depth + 1)	

					
					if result[0]:
						return True, solution

					self.restoreMatrix(removed)	
					

					solution.pop()
					#print(removed)
					#print()
					


				cur = cur.down
				#print('down')
				if cur == best:
					done = True
			return False, 1







def solutiontoboard(board, solution):

	while solution:
		cur = solution.pop()

		while not isinstance(cur, HeaderNode):
			cur = cur.right

		row, col, val = cur.id
		board[row][col] = val + 1


	

def printboard(board):

    for row in board:
        for ele in row:
            print(ele, end=" ")
        print()


def stringToBoard(s):
	board = [[None for j in range(0, 9)] for i in range(0, 9)] 
	for i in range(0,9):
		for j in range(0,9):
			board[i][j] = int(a[i * 9 + j])
	return board

if __name__ == "__main__":
	#a ='000000398145983672389762451263574819958621743714398526597236184426817935831459267'
	a ='602050000000004030000000000430008000010000200000000700500270000000000081000600000'
	#a = '720096003000205000080004020000000060106503807040000000030800090000702000200430018'
	#a = '672145398145000672389762451263574819958621743714390526597230184426817935831459267'
	#a = '000004028406000005100030600000301000087000140000709000002010003900000507670400000'
	
	
	matrix = DLmatrix()
	#a = input("board: ")

	board = stringToBoard(a)
	a2 = a.replace('0', '')

	print(a2, len(a2))
	
	matrix.inputBoard(board)



	#print([e.heur for e in matrix.headers])
	#matrix.inputBoard(board)
	r = matrix.root
	cur = matrix.root
	print()
	k = 0
	done = 0
	while done != 1:
		#print(cur)
		#print(cur.id)
		#print(k)
		#print()
		#input(cur)
		cur = cur.down
		
		
		
		k += 1
		if (cur == r):
			done += 1
		#input()
	print("down: ", k)

	k = 0
	done = 0
	while done != 1:
		#print(cur)
		#print(cur.id)
		#print(k)
		#print()
		#input(cur.id)
		cur = cur.right
		
		
		
		k += 1
		if (cur == r):
			done += 1
		#input()
	print("right: ", k)

	n = 1


	oldTime = time.perf_counter()
	for i in range(n):
		sol = matrix.DLX()

		solutiontoboard(board, sol[1])


		printboard(board)
		#print()
	print(time.perf_counter() - oldTime, (time.perf_counter() - oldTime) / n)

	# heurs = []

	# cur =  matrix.root

	# while True:
	# 	heurs.append((cur.id, cur.heur))
	# 	cur = cur.right
	# 	if cur == matrix.root:
	# 		break
	# heurs.sort()
	# print(heurs[1:])

	# heurs2 = []
	# #print(self.bins)

	# i = 1
	# for node in matrix.bins[1:]:
	# 	if node.binDown != node:
	# 		cur = node.binDown
	# 		while True:
	# 			heurs2.append((cur.id, cur.heur))

	# 			cur = cur.binDown
	# 			#print(cur, node, matrix.bins)
	# 			#input()
	# 			if cur in matrix.bins:
	# 				break
	# 	i+=1

	# heurs2.sort()
	# print(heurs2)

	# h3 = []
	# node = matrix.bins[0]
	# if node.binDown != node:
	# 	cur = node.binDown
	# 	while True:
	# 		h3.append((cur.id, cur.heur))

	# 		cur = cur.binDown
	# 		#print(cur, node, matrix.bins)
	# 		#input()
	# 		if cur in matrix.bins:
	# 			break
	# print(h3)










    

