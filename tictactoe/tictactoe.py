import random
import threading



class TicTacToe:

	def memoize(f):
		cache  = {}

		def g(self, mask, possibleMoves, player, depth, turn = 0, alpha = -2, beta = 2):
			key = (mask, player, turn, alpha, beta)
			if key not in cache:
				t = f(self, mask, possibleMoves, player, depth, turn = turn, alpha = alpha, beta = beta)
				cache[key] = t
				#for newmask in self.symmetries(mask):
				#	key = (mask, player, turn, alpha, beta)
				#	cache[key] = t


			return cache[key]
		return g

	def memoizeNega(f):
		cache  = {}
		def g(self, mask, possibleMoves, player, depth, turn = 0, alpha = -2, beta = 2):
			key = (mask, player, turn, alpha, beta)
			if key not in cache:
				cache[key] = f(self, mask, possibleMoves, player, depth, turn, alpha, beta)
				#for newmask in self.symmetries(mask):
				#	key = (mask, player, turn, alpha, beta)
				#	cache[key] = t


			return cache[key]
		return g


	def pos(row, col, player):
		return row * 6 + col * 2 + player

	def posI(self, i, player):
		return i * 2 + player

	def order(self):
		yield 4
		yield 0
		yield 2
		yield 6
		yield 8
		yield 1
		yield 3
		yield 5
		yield 7



	



	l = [
	int("000001000001000001", base = 2),
	int("000100000100000100", base = 2),
	int("010000010000010000", base = 2),
	int("010101000000000000", base = 2),
	int("000000010101000000", base = 2),
	int("000000000000010101", base = 2),
	int("010000000100000001", base = 2),
	int("000001000100010000", base = 2)]
	d = {
		0: (l[0], l[5], l[6]),
		1: (l[0] << 1, l[5] << 1, l[6] << 1),
		2: (l[1], l[5]),
		3: (l[1] << 1, l[5] << 1),
		4: (l[2], l[5], l[7]),
		5: (l[2] << 1, l[5] << 1, l[7] << 1),
		6: (l[0], l[4]),
		7: (l[0] << 1, l[4] << 1),
		8: (l[1], l[4], l[6], l[7]),
		9: (l[1] << 1, l[4] << 1, l[6] << 1, l[7] << 1),
		10: (l[2], l[4]),
		11: (l[2] << 1, l[4] << 1),
		12: (l[0], l[3], l[7]),
		13: (l[0] << 1, l[3] << 1, l[7] << 1),
		14: (l[1], l[3]),
		15: (l[1] << 1, l[3] << 1),
		16: (l[2], l[3], l[6]),
		17: (l[2] << 1, l[3] << 1, l[6] << 1)
		}
	print(d)
	def __init__(self):
	    # TODO: Set up the board to be '-'




		self.board = [['-' for i in range(0,3)] for j in range(0,3)]

	

	def print_instructions(self):
	    # TODO: Print the instructions to the game
	    print("Play tic tac toe. P1 is O and P2 is X.")


	def print_board(self):
	    # TODO: Print the board
	    print('    0 1 2')
	    for i in range(0,3):
	    	s = str(i) + ': '
	    	for j in range(0,3):
	    		s += ' ' + self.board[i][j]
	    	print(s)
	    return

	def is_valid_move(self, row, col):
	    # TODO: Check if the move is valid  
	    if row >=0 and col >= 0 and row < 3 and col < 3 and self.board[row][col] == '-':
	    	return True
	    return False

	def place_player(self, player, row, col):
	    # TODO: Place the player on the board
	    self.board[row][col] = player


	def take_manual_turn(self, player):
	    # TODO: Ask the user for a row, col until a valid response
	    #  is given them place the player's icon in the right spot
	    valid = False
	    row = None
	    col = None
	    while not valid:
	    	row = input("input row: ")
	    	col = input("input col: ")
	    	try:
	    		row = int(row)
	    		col = int(col)
	    		if self.is_valid_move(row, col):
	    			valid = True
	    		else:
	    			print('invalid location')
	    	except Exception:
	    		print('invalid input')
	    	
	    	
	    self.place_player(player, row, col)



	def take_turn(self, player):
	    # TODO: Simply call the take_manual_turn function
	    if player == 'O':
	        #self.minimaxMask(player)
	        self.negamax(player)
	    else:
	        #self.take_minimax_turn (player)
	        #self.minimaxMask(player)
	        self.negamax(player)

	def take_random_turn(self, player):
	    x, y = -1, -1
	    while not self.is_valid_move(x, y):
	        x, y = random.randint(0,3), random.randint(0,3)
	    self.board[x][y] = player

	def take_minimax_turn(self, player):
	    t = self.minimax(player)
	    print(t)
	    self.board[t[1][0]][t[1][1]] = player


	def minimax(self, player, depth = 10, alpha = -100, beta = 100):

	    notplayer = 'X'
	    if player == 'X':
	        notplayer = 'O'

	    if self.check_win(player):
	        return (1, )
	    elif self.check_win(notplayer):
	        return (-1, )
	    elif self.check_tie():
	        return (0, )
	    elif depth <= 0:
	    	return (0, )

	    if not (depth % 2):
	        #print('b')
	        best = -10000
	        bestmove = (-1, -1)
	        for row in range(0,3):
	            for col in range(0,3):

	                if self.is_valid_move(row, col):
	                    self.board[row][col] = player
	                    move = self.minimax(player, depth - 1)
	                    if move[0] > best:
	                        best = move[0]
	                        bestmove = (row, col)

	                    if alpha > best:
	                    	alpha = best

	                    if beta <= alpha:
	                    	break

	                    self.board[row][col] = '-'

	        return best, bestmove
	    else:
	        #print('w')
	        worst = 10000
	        worstmove = (-1, -1)
	        for row in range(0,3):
	            for col in range(0,3):

	                 if self.is_valid_move(row, col):
	                    self.board[row][col] = notplayer
	                    move = self.minimax(player, depth - 1)
	                    if move[0] < worst:
	                        worst = move[0]
	                        worstmove = (row, col)

	                    if beta < worst:
	                    	beta = worst

	                    if beta <= alpha:
	                    	break
	                   
	                    self.board[row][col] = '-'

	        return worst, worstmove



	def check_col_win(self, player):
		# TODO: Check col win
		for col in range(0,3):
			row = 0
			win = True
			while row < 3 and win:
				if self.board[row][col] != player:
					win = False
				row += 1
			if win:
				return win
		return False


	def check_row_win(self, player):
	    # TODO: Check row win
	    for row in range(0,3):
	    	col = 0
	    	win = True
	    	while col < 3 and win:
	    		if self.board[row][col] != player:
	    			win = False
	    		col += 1
	    	if win:
	    		return win
	    return False

	def check_diag_win(self, player):
	    # TODO: Check diagonal win
	    win1 = True
	    win2 = True
	    for i in range(0, 3):
	    	if self.board[i][i] != player:
	    		win1 = False
	    	if self.board[2-i][i] !=  player:
	    		win2 = False
	    return win1 or win2



	def check_win(self, player):
	    # TODO: Check win
	    return self.check_row_win(player) or self.check_diag_win(player) or self.check_col_win(player)

	def check_tie(self):
	    # TODO: Check tie
	    if self.check_win('X') or self.check_win('O'):
	    	return False
	    
	    tie = True
	    for row in range(0, 3):
	    	for col in range(0, 3):
	    		if self.board[row][col] == '-':
	    			tie = False
	    return tie 

	def play_game(self):
	# TODO: Play game
		win = False
		playerList = ['X', 'O']
		player = 1
		self.print_board()
		while not self.check_tie() and not win:
			player = (player + 1) % 2
			self.take_turn(playerList[player])    
			self.print_board()	
			win = self.check_win(playerList[player])

		if win:
			print(playerList[player] + " won!")
		else:
			print("tie")



	def boardToMask(self, board):
		mask = 0
		notPossibleMoves = int('111111111', base = 2)
		for i in range(0,3):
			for j in range(0,3):
				if board[i][j] == 'X':
					notPossibleMoves = notPossibleMoves ^ 1 << i * 3 + j
					mask = mask | 1 << i * 6 + j * 2
				elif board[i][j] == 'O':
					notPossibleMoves = notPossibleMoves ^ 1 << i * 3 + j
					mask = mask | 1 << i * 6 + j * 2 + 1

		#print(bin(mask))	
		return mask, notPossibleMoves

	def maskValidMove(self, row, col):
		return not mask & 3 << row * 6 + col * 2

	def checkWinMask(self, mask, i, player):
		
		pos = self.posI(i, player)
		mask =  mask | 1 << pos
		for e in self.d[pos]:
			if e & mask == e:
				return True
		return False

	def minimaxMask(self, player):
		mask, possibleMoves = self.boardToMask(self.board)
		depth = 0
		if False:
			self.board[0][0] = player
		else:
			if player == 'X':
				p = 0
			else:
				p = 1
			for i in range(0, 9):
				if (~possibleMoves) & 1 << i:
					depth += 1
			move = self.minimaxMaskHelper(mask, possibleMoves, p, depth)
			print(move)
			self.board[move[1] // 3] [move[1] % 3] = player

	@memoize
	def minimaxMaskHelper(self, mask, possibleMoves, player, depth, turn = 0, alpha=-2, beta=2):
		
		winCheck = depth >= 4
		tieCheck = depth == 8

		if not turn:
			best = -2
			bestmove = -1

			temp = possibleMoves
			i = 0 
			while temp:	
				if 1 & temp:
					if winCheck:
						if self.checkWinMask(mask, i, player):
							return (1, i)
						if tieCheck:
							return (0, i)

					move = self.minimaxMaskHelper(mask | 1 << self.posI(i, player), 
					possibleMoves ^ 1 << i,
					1 - player, depth + 1, 1)[0]
					
					if move > best:
						best = move
						bestmove = i


					if alpha > best:
						alpha = best
						if alpha == 1:
							break

						if beta <= alpha:
							break

				temp = temp >> 1
				i += 1


			return best, bestmove
		else:
			
			worst = 2
			worstmove = -1
			temp = possibleMoves
			i = 0 
			while temp:	
				if 1 & temp:
					if winCheck:
						if self.checkWinMask(mask, i, player):
							return (-1, i)
						if tieCheck:
							return (0, i)

					move = self.minimaxMaskHelper(mask | 1 << self.posI(i, player), 
					possibleMoves ^ 1 << i,
					1 - player, depth + 1, 0)[0]

					if move < worst:
						worst = move
						worstmove = i

					if beta < worst:
						beta = worst

						if beta <= alpha:
							break

				temp = temp >> 1
				i += 1

			return worst, worstmove


	def negamax(self, player):
		mask, possibleMoves = self.boardToMask(self.board)
		if player == 'X':
			p = 0
		else:
			p = 1

		depth = 0
		for i in range(0, 9):
				if (~possibleMoves) & 1 << i:
					depth += 1
		move = self.negamaxHelper(mask, possibleMoves, p, depth) 
		print(move)
		self.board[move[1] // 3] [move[1] % 3] = player

	@memoizeNega
	def negamaxHelper(self, mask, possibleMoves, player, depth, turn = 0, alpha = -2, beta = 2):
		
		if possibleMoves:
			
			best = -2
			bestmove = -1
			temp = possibleMoves
			winCheck = depth >= 4

			for i in self.order():
				if possibleMoves >> i & 1:
					if winCheck and self.checkWinMask(mask, i, player):
					 	return (1, )

					move = -self.negamaxHelper(mask | 1 << self.posI(i, player), 
					possibleMoves ^ 1 << i,
					1 - player, depth + 1, 1 - turn, -beta, -alpha)[0]


					if move > best:
						best = move
						bestmove = i
						if best > alpha:
							alpha = best
							if alpha == 1:
								break
							elif alpha >= beta:
								break
					
					

			return best, bestmove

		else:
			return (0, )




	def minimaxHelperThreaded(s, alpha, beta):
		while s:
			mask, possibleMoves, player, depth, turn, alpha, beta = s.pop()
			break
		pass



a = TicTacToe()


'''

00 00 01 
00 00 01 
00 00 01

00 01 00 
00 01 00 
00 01 00

01 00 00 
01 00 00 
01 00 00

01 01 01 
00 00 00 
00 00 00

00 00 00 
01 01 01 
00 00 00

00 00 00 
00 00 00 
01 01 01

01 00 00 
00 01 00 
00 00 01

00 00 01 
00 01 00 
01 00 00


'''


