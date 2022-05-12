import time

#Normal Node for circularly doubly-linked graph with pointers up, down, left, right
class Node:
	def __init__(self):
		self.right, self.left, self.up, self.down, self.header = None, None, None, None, None
		self.id = None

#HeaderNode for circularly doubly-linked graph with pointers up, down, left, right
#HeaderNodes are for Column and RowHeaders. Heuristic for columns
class HeaderNode(Node):
	def __init__(self):
		super().__init__()
		self.heur = None

#Dancing Links sparese matrix
class DLmatrix():
	def __init__(self):

		#initialize root
		self.root = HeaderNode()
		self.root.right, self.root.left, self.root.up, self.root.down, self.root.header = self.root, self.root, self.root, self.root, self.root
		self.root.id = 0

		#list for easy access for bugfixing
		self.headers = [self.root] 

		#add the column headers into the circularly linked list
		for i in range(0, 324):
			self.addHeaderNode(self.root, i + 1)

		#add all possible rows
		self.addRows()

	#adds a headerNode to the column Head.
	def addHeaderNode(self, last, i):
		new = HeaderNode()
		new.heur = 9
		new.id = i
		self.headers.append(new)
		new.header = new
	
		#insert new column header
		new.up = new
		new.down = new 
		
		leftNode = last
		rightNode = last.right
		
		rightNode.left = new
		new.right = rightNode

		leftNode.right = new
		new.left = leftNode

	#finds the best column to look at deterministically by iterating through all column Headers.
	def getBestCol(self):
	
		cur = self.root.right
		done = False
		
		best = cur
		while not done:

			if cur.heur < best.heur:
				best = cur
				if best.heur == 1:
					break		
			
			cur = cur.right
			if cur == self.root:
				done = True
		
		return best

	#get the columnheader given an index
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

	#create a single doubly linked circular row
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
		return first

	#add all possible rows to the sparse matrix
	def addRows(self):
		d = {}
		#nodes = 0
		for row in range(9):
			for col in range(9):
				box = row // 3 * 3 + col // 3
				for val in range(9):

					#indexes of positions for the row
					indices =  [0, row * 9 + col + 1, 81 + val * 9 + row + 1, 81 * 2 + val * 9 + col + 1, 81 * 3 + val * 9 + box + 1]

					first = self.createRow()
					first.id = (row, col, val)
					cur = first

					for index in indices:

						colHeader = self.getNthCol(index)

						#insert node
						cur.header = colHeader
						cur.up = colHeader
						cur.down = colHeader.down

						colHeader.down = cur
						cur.down.up = cur

						cur = cur.right

	#iterate through a row and remove all its Nodes, 
	#returns [NodeRemoved]
	def removeRow(self, rowNode):

		cur = rowNode
		
		removed = []

		#iterate through the row
		while True:
			
			#remove row
			cur.up.down = cur.down
			cur.down.up = cur.up

			removed.append(cur)

			cur = cur.right
			if cur == rowNode:
				break

		return removed

	#iterate through a column, removing each row \
	#returns the [columnHeader, [removeRow()]]
	def removeCol(self, colNode):
		
		colNode = colNode.header

		done = False
		cur = colNode


		colHeader = None
		removed = []

		rows = []
		while True:

			#remove Column Header
			if cur.id is not None:
				cur.right.left = cur.left
				cur.left.right = cur.right
			else:
				rows.append(cur)
				
			cur = cur.down
			if cur == colNode:
				break

		#remove rows based after iterating through the column
		for row in rows:
			removed += self.removeRow(row)

		#change the heuristic for each Column
		for remove in removed:
			if remove.id is None:
				cur = remove.header
				cur.heur -= 1

		return [colNode, removed]

	#deletes corresponding rows and cols in DL matrix to set up sudoku board
	def inputBoard(self, board):
		for row in range(9):
			for col in range(9):
				box = row // 3 * 3 + col // 3
				val = board[row][col]
				if val != 0:

					#indices of columns to remove
					indices =  [row * 9 + col + 1, 81 + (val - 1) * 9 + row + 1, 81 * 2 + (val - 1) * 9 + col + 1, 81 * 3 + (val - 1) * 9 + box + 1]
					for index in indices:

						colHead = self.getNthCol(index)
						if colHead:
							self.removeCol(colHead)

	#restore removed nodes to the matrix when backtracking
	def restoreMatrix(self, removed):
	
		for remove in removed:
			colHead = remove[0]
			if colHead:

				#add back columnHeader
				colHead.left.right = colHead
				colHead.right.left = colHead

			for node in remove[1]:
				#change heuristc
				if node.id is None:
					cur = node.header
					cur.heur += 1
				
				#add back node
				node.up.down = node
				node.down.up = node
		
	def DLX(self, solution = [], depth = 0):
		
		#base case
		if self.root == self.root.right:
			return True, solution

		else:
			best = self.getBestCol()
			done = False
			cur = best
			#iterate through each row in the column
			while not done:

				if cur.id is None:
					
					#add move to solution
					solution.append(cur)					
					removed = []
					
					done2 = False
					cur2 = cur

					#removes all connected columns for a given row
					while not done2:
	
						if cur2.id is None:
							removed.append(self.removeCol(cur2))	

						cur2 = cur2.right
						
						if cur2 == cur:
							done2 = True

					#recursive call
					result = self.DLX(solution, depth + 1)	

					#base case
					if result[0]:
						return True, solution

					#restore matrix
					self.restoreMatrix(removed)	
					solution.pop()

				#iterate
				cur = cur.down
				if cur == best:
					done = True

			return False, 1

#converts list of nodes into their corresponding values
#and puts it into the board list
def solutiontoboard(board, solution):

	while solution:
		cur = solution.pop()

		while not isinstance(cur, HeaderNode):
			cur = cur.right

		row, col, val = cur.id
		board[row][col] = val + 1

#prints the sudoku board in a grid
def printboard(board):

    for row in board:
        for ele in row:
            print(ele, end=" ")
        print()

#converts the string of 81 digits into the 9 by 9 2D array
def stringToBoard(s):
	board = [[None for j in range(0, 9)] for i in range(0, 9)] 
	for i in range(0,9):
		for j in range(0,9):
			board[i][j] = int(s[i * 9 + j])
	return board

#main
if __name__ == "__main__":
	#sample boards
	#a ='000000398145983672389762451263574819958621743714398526597236184426817935831459267'
	#a ='602050000000004030000000000430008000010000200000000700500270000000000081000600000'
	#a = '720096003000205000080004020000000060106503807040000000030800090000702000200430018'
	#a = '672145398145000672389762451263574819958621743714390526597230184426817935831459267'
	#a = '000004028406000005100030600000301000087000140000709000002010003900000507670400000'
	#a = '002009001000080040050400000009000000230007900710000002001003007000600100600050080'
	
	#initialize matrix
	matrix = DLmatrix()

	#input sudoku
	sudoku = input("board: ")

	board = stringToBoard(sudoku)
	
	matrix.inputBoard(board)

	printboard(board)
	print()
	oldTime = time.perf_counter()
	sol = matrix.DLX()
	solutiontoboard(board, sol[1])
	printboard(board)
	print()
	print(time.perf_counter() - oldTime)












    

