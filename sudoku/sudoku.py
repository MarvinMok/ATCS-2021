class Node:
	def __init__(self):
		self.right, self.left, self.up, self.down = None, None, None, None

class HeaderNode(Node):
	def __init__(self):
		super().__init__()

class DLX():
	def __init__(self):
		self.root = HeaderNode()
		self.root.right, self.root.left, self.root.up, self.root.down = self.root, self.root, self.root, self.root
		#print(self.root)
		for i in range(0, 323):
			self.addHeaderNode(self.root)
		self.addRows()


	
	def addHeaderNode(self, last):
		new = HeaderNode()
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


	def getNthCol(self, n):
		cur = self.root
		for i in range(n):
			cur = cur.right
		return cur

	def createRow(self):
		first = Node()
		first.left, first.right = first, first

		for i in range(3):
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
		nodes = 0
		for row in range(9):
			for col in range(9):
				box = row // 3 * 3 + col // 3
				for val in range(9):
					cols = (row * 9 + col, 81 + val * 9 + row, 81 * 2 + val * 9 + col, 81 * 3 + val * 9 + box)
					first = self.createRow()
					cur = first
					for col in cols:

						colHeader = self.getNthCol(col)

						
						cur.up = colHeader
						cur.down = colHeader.down

						colHeader.down = cur
						cur.down.up = cur


						cur = cur.right
						nodes +=1
		#print(nodes)






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
	a = '720096003000205000080004020000000060106503807040000000030800090000702000200430018'
	board = stringToBoard(a)

	matrix = DLX()
	r = matrix.root
	cur = r
	print()
	k = 0
	done = 0
	while not done:
		print(cur)
		cur = cur.down
		
		
		k += 1

		

		if (cur == r):
			done = 1
	print(k)

    
    

