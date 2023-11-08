import tkinter
from games.sudoku_generator import board_creator
from pynput.keyboard import Listener
from tkinter import messagebox
from time import time
from stat_control import StatCsv

class SquareEach():
    def __init__(self, master, number, i, j, listener):
        self.new_button = None
        self.pressed = None
        self.listener = listener
        if number == 0:
            self.new_button = tkinter.Button(master, text=f" {number} ", command=self.button_change, bg="#C7CFB4", font=("Ubuntu", 17, "normal"), padx=10, pady=10)
            self.new_button.grid(row=i, column=j)
        else:
            self.new_button = tkinter.Button(master, text=f" {number} ", font=("Ubuntu", 17, "normal"), padx=10, pady=10)
            self.new_button.grid(row=i, column=j)
        self.text = self.new_button['text']

    def button_change(self):
        self.listener.on_press = self.on_press

    def on_press(self, key):
        try:
            new_value = int(key.char)
            self.new_button.config(text=f" {new_value} ")
            self.text = self.new_button['text']
        except:
            print("Please enter a valid value!")

class BoardSudoku():
    def __init__(self, N=9, K=40) -> None:
        self.N = N
        self.K = K
        self.master = tkinter.Tk()
        self.master.title("SUDOKU")
        self.master.iconbitmap("letter-g.ico")  # attributes for icon to popo2021, https://www.flaticon.com/free-icons/letter-g"
        self.master.resizable(0, 0)
        self.master.iconbitmap("letter-g.ico")
        self.master.geometry("566x620")
        self.board = None
        self.empty_board = None
        self.solved_board = None
        self.listener = None
        self.square_list = [[],[],[],[],[],[],[],[],[]]
        self.start_time = time()
        self.start_game()
        self.master.mainloop()

    def start_game(self):
        self.board = None
        self.empty_board = None
        self.solved_board = None
        self.listener = None
        self.square_list = [[],[],[],[],[],[],[],[],[]]
        self.board = board_creator(self.N, self.K)
        self.empty_board = self.board[0].mat
        self.solved_board = self.board[1].mat
        self.listener = Listener(on_press=None)
        self.listener.__enter__()
        for i in range(self.N):
            for j in range(self.N):
                new = SquareEach(self.master, int(self.empty_board[i][j]), i, j, self.listener)
                self.square_list[i].append(new)
        submit_button = tkinter.Button(self.master, text=f"Submit", command=self.get_square_list, bg="#C7CFB4", font=("Ubuntu", 13, "normal"), padx=12, pady=5)
        submit_button.grid(row=12, column=1, columnspan = 3)
        menu_button = tkinter.Button(self.master, text=f"Back", command=self.back_to_menu, bg="#C7CFB4", font=("Ubuntu", 13, "normal"), padx=12, pady=5)
        menu_button.grid(row=12, column=5, columnspan = 3)

    def get_square_list(self):
        numbers = [[],[],[],[],[],[],[],[],[]]
        for i in range(self.N):
            for j in range(self.N):
                number = self.square_list[i][j].text
                numbers[i].append(int(number))
        # for i in range(self.N):
        #     for j in range(self.N):
        #         print(numbers[i][j], end=" ")
        #     print()
        if numbers == self.solved_board:
            message = messagebox.showinfo("You Won", "Sudoku Solved")
            end_time = time()
            time_total = end_time-self.start_time
            stats = StatCsv()
            stats.change_sudoku_stats(time_total)
            self.master.destroy()
            del self.listener

    def back_to_menu(self):
        self.master.destroy()
        del self.listener