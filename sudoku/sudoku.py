

class Node:
	def __init__(self):
		self.right, self.left, self.up, self.down = None, None, None, None


class HeaderNode(Node):
	def __init__(self):
		super().__init__()
		self.id = None
		self.heur = None

class DLmatrix():
	def __init__(self):
		self.root = HeaderNode()
		self.root.right, self.root.left, self.root.up, self.root.down = self.root, self.root, self.root, self.root
		self.root.id = 0
		self.headers = [self.root] 
		#print(self.root)
		for i in range(0, 324):
			self.addHeaderNode(self.root, i + 1)
		
		self.headers.sort(key = lambda x: x.id)
		self.addRows()


	
	def addHeaderNode(self, last, i):
		new = HeaderNode()
		new.heur = 9
		self.headers.append(new)
		new.id = i
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
		cur = self.root.right
		done = False
		if self.root.right == self.root:
			return False
		best = cur
		while not done:

			if cur.heur > best.heur:
				best = cur
			
			
			cur = cur.right
			if (cur == self.root):
				done = True
		
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
		nodes = 0
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

						cur.up = colHeader
						cur.down = colHeader.down

						colHeader.down = cur
						cur.down.up = cur


						#print(cur, cur.down.up, colHeader.down, cur.up.down, Down.up)
						#print(colHeader, cur.up)
						#print(Down, cur.down)
						#a = input()
						cur = cur.right
						nodes +=1
		#d2 = {i:d[i] for i in sorted(list(d.keys()))}
		#print(d2)
		print(nodes)


	#iterate through a row and remove all its Nodes, 
	#returns [NodeRemoved]
	def removeRow(self, rowNode):
		done = False
		cur = rowNode
		
		header = None
		removed = []
		while not done:
				
			cur.up.down = cur.down
			cur.down.up = cur.up

			removed.append(cur)

			cur = cur.right
			if cur == rowNode:
				done = True

		return removed


	#iterate through a column, removing each row \
	#returns the [columnHeader, [removeRow()]]

	def removeCol(self, colNode):

		done = False
		cur = colNode
		colHeader = None
		rows = []
		while not done:
			if isinstance(cur, HeaderNode):
				header = cur

				cur.right.left = cur.left
				cur.left.right = cur.right

			else:
				rows.append(self.removeRow(cur))

			cur = cur.down
			if (cur == colNode):
				done = True

		return [header, rows]

	#deletes corresponding rows and cols in DL matrix to set up sudoku board
	def inputBoard(self, board):
		for row in range(9):
			for col in range(9):
				box = row // 3 * 3 + col // 3
				val = board[row][col]
				if val != 0:
					indices =  [row * 9 + col + 1, 81 + val * 9 + row + 1, 81 * 2 + val * 9 + col + 1, 81 * 3 + val * 9 + box + 1]
					for index in indices:

						colHead = self.getNthCol(index)
						if colHead:
							self.removeCol(colHead)


	def restoreMatrix(removed):
		for remove in removed:
			colHead = remove[0]

			colHead.left.right = colHead
			colHead.right.left = colHead

			for node in remove[1]:
				node.up.down = node
				node.down.up = node

	def DLX(self, solution = []):
		
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


		if self.root == self.root.right:
			return True, solution
		elif self.root == self.root.down:
			return False, solution
		else:
			best = self.getBestCol()

			done = False
			cur = best
			while not done:

				if not isinstance(cur, HeaderNode):
				
					solution.append(cur)					
					removed = []
					


					done2 = False
					cur2 = cur
					while not done2:
						print(cur2)
						removed.append(self.removeCol(cur2))	

						cur2 = cur2.right
						if cur2 == cur:
							done2 = True



					result = self.DLX()			
					if result[0]:
						return True, solution

					solution.pop()
					self.restoreMatrix(removed)

				cur = cur.down
				print('down')
				if cur == best:
					done = True











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
	a = '000105000140000670080002400063070010900000003010090520007200080026000035000409000'
	board = stringToBoard(a)
	a2 = a.replace('0', '')

	print(len(a2))
	matrix = DLmatrix()


	w = HeaderNode()

	#matrix.inputBoard(board)
	r = matrix.root
	cur = r
	print()
	k = 0
	done = 0
	while not done:
		#print(cur)
		#print(cur.id)
		#print(k)
		#print()

		cur = cur.right
		
		
		k += 1
		if (cur == r):
			done = 1
		#input()
	print(k)
	print(matrix.DLX())

    
    

