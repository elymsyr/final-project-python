import random
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
from stat_control import StatCsv

class TicTacToe():
    def __init__(self) -> None:
        self.turn = 0
        self.board = [[" " for x in range(3)] for y in range(3)]
        self.button = []
        self.game_board = None
        self.player = None
        self.computer = None
        
    def start_game(self):
        self.game_board = Tk()
        self.game_board.iconbitmap("letter-g.ico")  # attributes for icon to popo2021, https://www.flaticon.com/free-icons/letter-g"
        self.game_board.title("Tic Tac Toe")
        self.game_board.resizable(0,0)
        self.player = Button(self.game_board, text="Player X", width=10)
        self.player.grid(row=1, column=1)
        self.computer = Button(self.game_board, text="Computer O", width=10, state=DISABLED)
        self.computer.grid(row=2, column=1)
        self.create_board()

    def create_board(self):
        self.button = []
        for i in range(3):
            m = 3+i
            self.button.append(i)
            self.button[i] = []
            for j in range(3):
                n = j
                self.button[i].append(j)
                get_t = partial(self.state_check, i, j)
                self.button[i][j] = Button(
                    self.game_board, bd=5, command=get_t, height=4, width=8)
                self.button[i][j].grid(row=m, column=n)
        self.game_board.mainloop()
        
    def state_check(self, movement_x, movement_y):
        if self.board[movement_x][movement_y] == " ":
            if self.turn % 2 == 0:
                self.player.config(state=DISABLED)
                self.computer.config(state=ACTIVE)
                self.board[movement_x][movement_y] = "X"
            else:
                self.button[movement_x][movement_y].config(state=ACTIVE)
                self.computer.config(state=DISABLED)
                self.player.config(state=ACTIVE)
                self.board[movement_x][movement_y] = "O"
            self.turn += 1
            self.button[movement_x][movement_y].config(text=self.board[movement_x][movement_y])
        state = True
        stats = StatCsv()
        if self.win_state_check("X"):
            stats.change_ttt_stats(1)
            self.game_board.destroy()
            state = False
            message = messagebox.showinfo("Winner", "Player won the match")
        elif self.win_state_check("O"):
            stats.change_ttt_stats(-1)
            self.game_board.destroy()
            state = False
            message = messagebox.showinfo("Winner", "Computer won the match")
        elif(self.legal_move()):
            stats.change_ttt_stats(0)
            self.game_board.destroy()
            state = False
            message = messagebox.showinfo("Tie Game", "Tie Game")
        if(state):
            if self.turn % 2 != 0:
                move = self.pc_move()
                self.button[move[0]][move[1]].config(state=DISABLED)
                self.state_check(move[0], move[1])

    def legal_move(self):
        flag = True
        for i in self.board:
            if(i.count(' ') > 0):
                flag = False
        return flag

    def win_state_check(self, sign, board=None):
        if board == None:
            board = self.board
        return ((board[0][0] == sign and board[0][1] == sign and board[0][2] == sign) or
                (board[1][0] == sign and board[1][1] == sign and board[1][2] == sign) or
                (board[2][0] == sign and board[2][1] == sign and board[2][2] == sign) or
                (board[0][0] == sign and board[1][0] == sign and board[2][0] == sign) or
                (board[0][1] == sign and board[1][1] == sign and board[2][1] == sign) or
                (board[0][2] == sign and board[1][2] == sign and board[2][2] == sign) or
                (board[0][0] == sign and board[1][1] == sign and board[2][2] == sign) or
                (board[0][2] == sign and board[1][1] == sign and board[2][0] == sign))    

    def pc_move(self):
        possiblemove = []
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if self.board[i][j] == ' ':
                    possiblemove.append([i, j])
        move = []
        if possiblemove == []:
            return
        else:
            for let in ['O', 'X']:
                for i in possiblemove:
                    boardcopy = deepcopy(self.board)
                    boardcopy[i[0]][i[1]] = let
                    if self.win_state_check(let, boardcopy):
                        return i
            corner = []
            for i in possiblemove:
                if i in [[0, 0], [0, 2], [2, 0], [2, 2]]:
                    corner.append(i)
            if len(corner) > 0:
                move = random.randint(0, len(corner)-1)
                return corner[move]
            edge = []
            for i in possiblemove:
                if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
                    edge.append(i)
            if len(edge) > 0:
                move = random.randint(0, len(edge)-1)
                return edge[move]