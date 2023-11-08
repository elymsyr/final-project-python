import tkinter as tk
from tkinter import *
import random
from tkinter import messagebox
from tkinter import font as f
import PIL.ImageTk
import PIL.Image
from games.sudoku import BoardSudoku
from games.tictactoe import TicTacToe
from games.memory_game import Memory
from stat_control import StatCsv
from stat_window import StatisticsWindow
from games.battleship import BattleshipGame

class MainMenu():
    def __init__(self) -> None:
        self.palet_1 = ["#d1b3d2", "#672f4b", "#4a1b3b"]
        self.palet_2 = ["#f2e900", "#007aff", "#9FC131"]
        self.palet_3 = ["#ff1111", "#D6D58E", "#005C53"]
        self.palet_4 = ["#2a2a2a", "#FFFFFF", "#EAEAEA"]
        self.palet_5 = ["#4d94ff", "#ffbd4d", "#ff4d94"]
        self.palet_6 = ["#008c76", "#fff6c4", "#6e7f80"]
        self.palet_7 = ["#6c648b", "#ff69b4", "#91a6ae"]
        self.palet_8 = ["#336699", "#f6ae4b", "#f6f1e4"]
        self.palet_9 = ["#4f86c6", "#f6ae4b", "#ff693d"]
        self.palet_10 = ["#458985", "#f26d65", "#e4ccb0"]
        self.palet_11 = ["#ff3300", "#666699", "#ffcc00"]
        self.palet_12 = ["#ff0033", "#0099cc", "#d9bf77"]
        self.palet_13 = ["#00cc66", "#ffcc00", "#ff3300"]
        self.palet_14 = ["#ff9900", "#cc3300", "#009966"]
        self.palet_15 = ["#2b2b2b", "#ff6b6b", "#89d9f4"]
        self.colors = [self.palet_1, self.palet_2, self.palet_3, self.palet_4, self.palet_5, self.palet_6, self.palet_7, self.palet_8, self.palet_9, self.palet_10, self.palet_11, self.palet_12, self.palet_13, self.palet_14, self.palet_15]
        self.stats = StatCsv()
        self.root = tk.Tk()
        self.root.title("Games Final Project")
        self.root.resizable(0, 0)
        self.root.iconbitmap("letter-g.ico")  # attributes for icon to popo2021, https://www.flaticon.com/free-icons/letter-g"
        self.im = PIL.Image.open("background.gif")
        self.root.geometry(f"{self.im.width}x{self.im.height}")
        self.ph = PIL.ImageTk.PhotoImage(self.im)
        self.gif = Label(self.root, image=self.ph, bg="black", bd=3)
        self.framnr = 63
        self.frames = [PhotoImage(file="background.gif", format='gif -index %i' % (i)) for i in range(self.framnr)]
        self.gif = Label(self.root)
        self.gif.pack()
        self.root.after(0, self.update, 0)
        self.normal_font = ("Ubuntu", 12, "bold")
        self.available_fonts = f.families()
        self.button_create("SUDOKU", posx=0.20, posy=0.55, func=self.button1_click)
        self.button_create("TTT", posx=0.40, posy=0.55, func=self.button2_click)
        self.button_create("MEMORY", posx=0.60, posy=0.55, func=self.button3_click)
        self.button_create("BATTLESHIP", posx=0.80, posy=0.55, func=self.button4_click)
        self.button_create("STATS", posx=0.4, posy=0.75, func=self.button5_click)
        self.button_create("QUIT", posx=0.6, posy=0.75, func=self.button6_click)
        self.root.mainloop()

    def update(self, ind):
        frame = self.frames[ind]
        ind += 1
        if ind > 62: ind = 0
        self.gif.configure(image=frame)
        self.root.after(100, self.update, ind)

    def button_create(self, name, posx, posy, func):
        fonts = []
        for _ in range(50):
            font_name = random.choice(self.available_fonts)
            font_size = random.randint(8, 20)
            font_weight = random.choice(["normal", "bold"])
            font_slant = random.choice(["roman", "italic"])
            fonts.append((font_name, font_size, font_weight, font_slant))

        shake_text_id = None
        change_font_id = None
        shake_id = None
        color_id = None
        
        def on_enter(event):
            nonlocal shake_text_id, change_font_id, shake_id, color_id
            shake_text()
            change_font()
            shake_canvas()
            color_change()
            canvas.config(cursor="heart")
            
        def on_leave(event):
            nonlocal shake_text_id, change_font_id, shake_id, color_id
            canvas.coords(button_text, original_text_coords)
            canvas.itemconfig(button_text, font=self.normal_font)
            canvas.coords(polygon, original_polygon_coords)
            color_1 = self.palet_1[0]
            color_2 = self.palet_1[1]
            color_3 = self.palet_1[2]
            canvas.config(bg=color_3)
            canvas.itemconfig(button_text, fill=color_1)
            canvas.itemconfig(polygon, fill=color_2, outline=color_2)
            if shake_text_id is not None:
                canvas.after_cancel(shake_text_id)
            if change_font_id is not None:
                canvas.after_cancel(change_font_id) 
            if shake_id is not None: 
                canvas.after_cancel(shake_id)
            if color_id is not None: 
                canvas.after_cancel(color_id)
            
        def color_change():
            new_palette = random.choice(self.colors)
            color_1 = new_palette[0]
            color_2 = new_palette[1]
            color_3 = new_palette[2]
            canvas.config(bg=color_3)
            canvas.itemconfig(polygon, fill=color_2, outline=color_2)
            canvas.itemconfig(button_text, fill=color_1)
            nonlocal color_id
            color_id = canvas.after(100, color_change)
            
        def shake_canvas():
            x_offset = random.randint(-4, 4)
            y_offset = random.randint(-3, 3)
            canvas.move(polygon, x_offset, y_offset)
            nonlocal shake_id
            shake_id = canvas.after(160, shake_canvas)
                        
        def shake_text():
            x_offset = random.randint(-1, 1)
            y_offset = random.randint(-1, 1)
            canvas.move(button_text, x_offset, y_offset)
            nonlocal shake_text_id
            shake_text_id = canvas.after(90, shake_text)
            
        def change_font():
            random_font = random.choice(fonts)
            canvas.itemconfig(button_text, font=random_font)
            nonlocal change_font_id
            change_font_id = canvas.after(100, change_font)
            
        color_1 = self.palet_1[0]
        color_2 = self.palet_1[1]
        color_3 = self.palet_1[2]
        
        canvas = tk.Canvas(self.root, width=100, height=30, bg=color_3,highlightthickness=0)
        canvas.pack()
        canvas.place(relx=posx, rely=posy, anchor="center")
        polygon = canvas.create_polygon(30, 0, 103, 0, 71, 33, 0, 33, fill=color_2, outline=color_2, width=1)
        button_text = canvas.create_text(50, 16, text=name, fill=color_1, font=self.normal_font)
        original_text_coords = canvas.coords(button_text)
        original_polygon_coords = canvas.coords(polygon)
        canvas.tag_bind(button_text, '<Button-1>', lambda event: func())
        canvas.tag_bind(button_text, '<Leave>', on_leave)
        canvas.tag_bind(button_text, '<Enter>', on_enter)
        new_button = Button(text='asfasdf', bg='black')
        return canvas

    def button1_click(self):
        hard = messagebox.askyesno(title="Difficulty", message="Hard Mode? (No to try stat storage in csv.)")
        self.stats.increase_played(0)
        if hard:
            new_game = BoardSudoku(9, 50)
        else: new_game = BoardSudoku(9, 1)

    def button2_click(self):
        new_game = TicTacToe()
        self.stats.increase_played(1)
        new_game.start_game()     

    def button3_click(self):
        self.stats.increase_played(2)
        new_game = Memory()
        
    def button4_click(self):
        self.stats.increase_played(3)
        new_game = BattleshipGame()

    def button5_click(self):
        game_statistics = StatisticsWindow()
        
    def button6_click(self):
        self.root.destroy()

if '__main__' == __name__:
    app = MainMenu()
