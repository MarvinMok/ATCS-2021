import random


class TicTacToe:
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
        if player == 'X':
            self.take_random_turn(player)
        else:
            self.take_manual_turn(player)

    def take_random_turn(self, player):
        x, y = -1, -1
        while not self.is_valid_move(x, y):
            x, y = random.randint(0,3), random.randint(0,3)
        self.board[x][y] = player

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
        player = 0
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
        	



