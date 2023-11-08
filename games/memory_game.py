from tkinter import *
import random
import time
from tkinter import messagebox
import PIL.ImageTk
import PIL.Image
from stat_control import StatCsv

class Memory():
    def __init__(self) -> None:
        self.width = 110
        self.height = 155
        self.links = ["games\memory_game_card_0.png","games\memory_game_card_1.png","games\memory_game_card_2.png","games\memory_game_card_3.png","games\memory_game_card_4.png","games\memory_game_card_5.png","games\memory_game_card_6.png","games\memory_game_card_7.png"]
        self.data_images = []
        self.game_state = 0
        self.card_matches = {}
        self.clicked_cards = 0
        self.clicked_first = ""
        self.clicked_second = ""
        self.buttons = []
        self.window = Toplevel()
        self.window.iconbitmap("letter-g.ico")  # attributes for icon to popo2021, https://www.flaticon.com/free-icons/letter-g"
        self.window.resizable(0,0)
        self.window.title("Memory Game")
        self.card_back_image = PIL.ImageTk.PhotoImage(PIL.Image.open("games\memory_game_card_back.jpg"))
        for image in self.links:
            card_image = PIL.Image.open(image)
            new_image = self.resize_image(card_image)
            self.data_images.append(new_image)
        self.timing = time.time()
        self.stat_control = StatCsv()
        self.create_game()
        self.window.mainloop()
        
    def create_game(self):
        shuffled_datas = self.data_images.copy()
        shuffled_datas += shuffled_datas
        random.shuffle(shuffled_datas)
        for i in range(len(self.data_images)*2):
            if (i % 4 == 0 or i == 0) and i != 16:
                new_frame = Frame(self.window)
                new_frame.pack()
            new_button = Button(new_frame, image=self.card_back_image, font=('Helvetica', '20', 'bold'), width=self.width, height=self.height, compound="top")
            new_button.configure(command=lambda btn=new_button: self.click(btn), compound="top")
            self.buttons.append(new_button)
            new_button.grid(row=1,column=i%4,padx=10, pady=20)
            self.card_matches[new_button] = shuffled_datas.pop()
            
    def click(self, button):
        self.clicked_cards = self.clicked_cards + 1
        
        if self.clicked_cards == 1:
            self.clicked_first = button
            button.configure(image=self.card_matches[button],  compound="top")
            button['command'] = None
        
        if  self.clicked_cards == 2:
            self.clicked_second = button
            button.configure(image=self.card_matches[button], compound="top")
            button['command'] = None
            self.window.after(400,self.check)
            
    def resize_image(self, image):
        resized_image = image.resize((self.width, self.height), PIL.Image.LANCZOS)
        return PIL.ImageTk.PhotoImage(resized_image)
    
    def check(self):
        
        if self.clicked_second['image'] != self.clicked_first['image']:
            self.clicked_first.configure(image=self.card_back_image,state="normal", compound="top")
            self.clicked_second.configure(image=self.card_back_image,state="normal", compound="top")
            self.clicked_first['command'] = self.click(self.buttons[self.buttons.index(self.clicked_first)])
            self.clicked_second['command'] =self.click( self.buttons[self.buttons.index(self.clicked_second)])
        else:
            self.game_state = self.game_state + 1
            

        if self.game_state == len(self.data_images):
            timing = time.time() - self.timing
            messagebox.showinfo("MEMORY GAME", str(int(timing))+" seconds.")
            self.stat_control.change_memory_stats(timing)
            self.window.destroy()
            
        self.clicked_cards = 0
            
if __name__ == "__main__":
    game = Memory()