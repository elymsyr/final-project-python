import tkinter as tk
from random import randint
from stat_control import StatCsv

DEGREE = 30 # Change between 1 and 40. Increasing DEGREE will make the game slightly harder.

class BattleshipGame:
    def __init__(self):
        self.root = tk.Tk()
        self.stat = StatCsv()
        self.root.title("Battleship")
        self.root.resizable(0,0)
        self.root.iconbitmap("letter-g.ico")  # attributes for icon to popo2021, https://www.flaticon.com/free-icons/letter-g"
        self.enemy_ship_color = "#cc2525"
        self.not_founded_color = "#999999"
        self.player_ships_color = "#5b5b5b"
        self.player_ship_founded_color = "#cc0000"
        self.board_size = 10
        self.current_ship_loop = []
        self.first_shooted = None
        self.last_shooted = None
        self.your_ships = []
        self.side = -1
        self.inc = 0
        self.your_board = []
        self.enemy_ships = []
        self.enemy_board = []
        self.founded_ships_enemy = []
        self.founded_ships_player = []
        self.tryed = []
        self.enemy_tryed = []
        self.player_ship_size = 5
        self.ship_count = 2
        self.repeat = 1
        self.left = []
        self.right = []
        self.up = []
        self.down = []
        self.current = None
        self.you = 17 - len(self.founded_ships_player)
        self.enemy = 17 - len(self.founded_ships_enemy)
        self.setup_ui()
        self.place_ship(2)
        self.place_ship(3)
        self.place_ship(3)
        self.place_ship(4)
        self.place_ship(5)
        self.root.mainloop()

    def setup_ui(self):
        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(row=0, column=0, padx=10)
        self.frame_left = tk.Frame(self.main_frame)
        self.frame_left.grid(row=0, column=0, padx=10)
        self.frame_right = tk.Frame(self.main_frame)
        self.frame_right.grid(row=0, column=1, padx=10)
        self.label_left = tk.Label(self.frame_left, text="Your Board", font=("Helvetica", 20))
        self.label_left.grid(row=0, column=0, pady=10, columnspan=10, padx=1)
        self.label_right = tk.Label(self.frame_right, text="Enemy Board", font=("Helvetica", 20))
        self.label_right.grid(row=0, column=0, pady=10, columnspan=10, padx=1)
        self.your_board = []
        self.enemy_board = []
        self.your_ships = []
        self.player_ship_placement_check = None
        for i in range(1, self.board_size+1):
            row_left = []
            row_right = []
            for j in range(self.board_size):
                button_l = tk.Button(self.frame_left, text=f"O", width=6, height=3)
                button_l.config(command=lambda button=button_l: self.player_ship_placement(button))
                button_r = tk.Button(self.frame_right, text=f"O", width=6, height=3, state='disabled')
                button_r.config(command=lambda button=button_r: self.not_found(button))
                button_l.grid(row=i, column=j)
                button_r.grid(row=i, column=j)
                row_left.append(button_l)
                row_right.append(button_r)
            self.your_board.append(row_left)
            self.enemy_board.append(row_right)
        self.bottom_label = tk.Label(self.root, text=f"Choose a button to place {self.player_ship_size} square sized ships now...", pady=15, font=("Helvetica", 25))
        self.bottom_label.grid(row=1, column=0, columnspan=2)

    def shoot_player(self, button):
        button.config(bg=self.enemy_ship_color, state='disabled')
        if button not in self.founded_ships_enemy:
            self.founded_ships_enemy.append(button)
        self.bottom_label.config(text="Computers Turn")
        self.you = 17 - len(self.founded_ships_player)
        self.enemy = 17 - len(self.founded_ships_enemy)        
        self.root.after(100, self.computer_turn())
        
    def not_found(self, button):
        self.bottom_label.config(text="No Ship Founded")
        button.config(bg=self.not_founded_color, state='disabled')
        self.tryed.append(button)
        self.bottom_label.config(text="Computers Turn")
        self.root.after(100,self.computer_turn())
        
    def computer_turn(self):
        self.you = 17 - len(self.founded_ships_player)
        self.enemy = 17 - len(self.founded_ships_enemy)        
        self.bottom_label.config(text="Computers Turn")
        if self.you > 0 and self.enemy > 0:
            for row in self.enemy_board:
                for ship in row:
                    ship.config(state='disabled')
            self.root.after(10,self.comp_calc_shoot())
        else:
            if self.you == 0:
                self.bottom_label.config(text=f"YOU LOSE -{self.enemy}")
                self.stop_game()
                self.stat.change_battleship_stats(self.enemy*-1)
            elif self.enemy == 0:
                self.bottom_label.config(text=f"YOU WIN {self.you}")
                self.stat.change_battleship_stats(self.you)
                self.stop_game()
        
    def stop_game(self):
        for row in self.your_board:
            for ship in row:
                ship.config(state='disabled')
        for ship in self.your_ships:
            ship.config(bg='blue')                
        for row in self.enemy_board:
            for ship in row:
                ship.config(state='disabled')
        for ship in self.enemy_ships:
            ship.config(bg='blue')                  
        
    def comp_calc_shoot(self):
        global DEGREE
        coor = self.x_y()
        x = coor[1]
        y = coor[0]
        counter = 0
        while (y,x) in self.enemy_tryed or (y,x) in self.founded_ships_player or y > self.board_size-1 or y < 0 or x > self.board_size-1 or x < 0:
            DEGREE = 30
            if counter == 5:
                self.inc *= -1
            if counter == 10:
                self.last_shooted = None
            if counter == 15:
                y = randint(0,self.board_size-1)
                x = randint(0,self.board_size-1)
                self.first_shooted = None
                self.last_shooted = None
                self.inc = 0
                self.side = -1
                break
            coor = self.x_y()
            x = coor[1]
            y = coor[0]
            counter += 1
        self.root.after(10,self.shoot_computer(y, x))
    
    def check_sides(self, y, x):
        point = 0
        sides_y = [y + 1 if y != self.board_size-1 else y, y - 1 if y != 0 else y]
        sides_y_plus = [y + 2 if y < 8 else y, y - 2 if y > 1 else y]
        sides_y_plus_one = [y + 3 if y < 7 else y, y - 3 if y > 2 else y]
        sidex_x = [x - 1 if x != 0 else x, x + 1 if x != self.board_size-1 else x]
        sidex_x_plus = [x - 2 if x > 1 else x, x + 2 if x < 8 else x]
        sidex_x_plus_one = [x - 3 if x > 2 else x, x + 3 if x < 7 else x]
        sides = [(y,sidex_x[0]), (y,sidex_x[1]), (y,sidex_x_plus[0]), (y,sidex_x_plus[1]), (sides_y[0], x), (sides_y[1], x), (sides_y_plus[0], x), (sides_y_plus[1], x)]
        extre_side_point = [(y,sidex_x_plus_one[0]), (y,sidex_x_plus_one[1]), (sides_y_plus_one[0], x), (sides_y_plus_one[1], x)]
        for item in sides:
            if item not in self.enemy_tryed and item not in self.founded_ships_player:
                point += 10
            elif item not in self.enemy_tryed and item in self.founded_ships_player:
                point += 4
        for item in extre_side_point:
            if item not in self.enemy_tryed and item not in self.founded_ships_player:
                point += 5
            elif item not in self.enemy_tryed and item in self.founded_ships_player:
                point += 2                          
        line = randint(60, 100)
        if line+DEGREE< point:
            return False
        else: return True
    
    def inc_or_dec(self, number, old_number):
        number = randint(old_number-1, old_number+1)
        while number == old_number:
            number = randint(old_number-1, old_number+1)
        return number
    
    def x_y(self):
        y = randint(0,self.board_size-1)
        x = randint(0,self.board_size-1)               
        if self.first_shooted == None:
            y = randint(0,self.board_size-1)
            x = randint(0,self.board_size-1)
            while (y,x) in self.enemy_tryed and (y,x) in self.founded_ships_player:
                y = randint(0,self.board_size-1)
                x = randint(0,self.board_size-1)            
            while self.check_sides(y, x):
                y = randint(0,self.board_size-1)
                x = randint(0,self.board_size-1)
                while (y,x) in self.enemy_tryed and (y,x) in self.founded_ships_player:
                    y = randint(0,self.board_size-1)
                    x = randint(0,self.board_size-1)
                global DEGREE
                if randint(0,1):          
                    DEGREE -= 1
        elif self.last_shooted == None:
            old_x = self.first_shooted[1]
            old_y = self.first_shooted[0]
            if self.side == -1:
                side = randint(0,1)
            else: side = self.side
            if side == 0:
                y = self.inc_or_dec(y, old_y)
                x = old_x
            elif side == 1:
                x = self.inc_or_dec(x, old_x)
                y = old_y
        else:
            old_x = self.last_shooted[1]
            old_y = self.last_shooted[0]
            side = self.side
            if side == 0:
                if self.inc == 0:
                    self.inc = self.inc_or_dec(0,0)
                y = old_y-self.inc
                x = old_x
            elif side == 1:
                if self.inc == 0:
                    self.inc = self.inc_or_dec(0,0)
                x = old_x-self.inc
                y = old_y
        return [y,x]
    
    def shoot_computer(self, y, x):
        if self.your_board[y][x] not in self.your_ships:
            self.your_board[y][x].config(bg=self.not_founded_color)
            self.enemy_tryed.append((y,x))
            self.inc *= -1
            self.you = 17 - len(self.founded_ships_player)
            self.enemy = 17 - len(self.founded_ships_enemy)            
            self.root.after(100,self.player_turn())
        elif self.your_board[y][x] in self.your_ships:
            self.your_board[y][x].config(bg=self.player_ship_founded_color)
            if (y,x) not in self.founded_ships_player:
                self.founded_ships_player.append((y,x))
            if self.first_shooted == None:
                self.first_shooted = [y,x]
            else:
                if (y,x) not in self.founded_ships_player or (y,x) not in self.enemy_tryed:
                    self.last_shooted = [y,x]
                    if self.side == -1:
                        if self.last_shooted[0] == self.first_shooted[0]:
                            self.side = 1
                        else: self.side = 0
            self.you = 17 - len(self.founded_ships_player)
            self.enemy = 17 - len(self.founded_ships_enemy)                        
            self.root.after(100,self.player_turn())

    def player_turn(self):
        self.bottom_label.config(text=f"Your Turn")
        for row in self.enemy_board:
            for ship in row:
                ship.config(state='normal')
        for ship in self.founded_ships_enemy:
            ship.config(state='disabled')
        for ship in self.tryed:
            ship.config(state='disabled')
        self.you = 17 - len(self.founded_ships_player)
        self.enemy = 17 - len(self.founded_ships_enemy)            
        if self.you > 0 and self.enemy > 0:
            pass
        else:
            if self.you == 0:
                self.bottom_label.config(text=f"YOU LOSE -{self.enemy}")
                self.stat.change_battleship_stats(self.enemy*-1)
                self.stop_game()
            elif self.enemy == 0:
                self.bottom_label.config(text=f"YOU WIN {self.you}")
                self.stat.change_battleship_stats(self.you)
                self.stop_game()
			
    def place_ship(self, ship_size):
        placement_process = True
        while placement_process:
            self.current_ship_loop = []
            x = randint(0,self.board_size-ship_size)
            y = randint(0,self.board_size-ship_size)
            angle = randint(0,1)
            for _ in range(ship_size):
                placement_process = self.check_place(x, y, 0)
                if placement_process:
                    break
                else:
                    if angle == 0:
                        x += 1
                    else: y += 1
        if not placement_process:
            for ship in self.current_ship_loop:
                self.enemy_ships.append(ship)
                ship.config(text="O", command=lambda button=ship: self.shoot_player(button))
    
    def check_place(self, x, y, state):
        if state == 0:
            if (self.enemy_board[y][x] not in self.current_ship_loop) and (self.enemy_board[y][x] not in self.enemy_ships):
                self.current_ship_loop.append(self.enemy_board[y][x])
                return False
            else: return True
        else: pass

    def player_ship_placement(self, button):
        """Game starts with this condition to let the player to place the ships. 
        """
        if button not in self.your_ships:
            self.player_ship_placement_check = button
            self.color_sides(button)

    def color_sides(self, button):
        size = self.player_ship_size
        self.left = []
        self.right = []
        self.up = []
        self.down = []
        self.current = button
        button.config(bg='grey')
        coor = self.return_coor(button)
        for side_choose in range(4):
            x = coor[1]
            y = coor[0]
            if side_choose == 3:
                x += 1
                for _ in range(size-1):
                    if (x < 0 or x > self.board_size-1 or y < 0 or y > self.board_size-1) or self.your_board[y][x] in self.your_ships:
                        self.right = []
                        break
                    else:
                        self.right.append(self.your_board[y][x])
                        x+=1
            if side_choose == 2:
                x -= 1
                for _ in range(size-1):
                    if (x < 0 or x > self.board_size-1 or y < 0 or y > self.board_size-1) or self.your_board[y][x] in self.your_ships:
                        self.left = []
                        break
                    else:
                        self.left.append(self.your_board[y][x])
                        x-=1
            if side_choose == 1:
                y += 1
                for _ in range(size-1):
                    if (x < 0 or x > self.board_size-1 or y < 0 or y > self.board_size-1) or self.your_board[y][x] in self.your_ships:
                        self.up = []
                        break
                    else:
                        self.up.append(self.your_board[y][x])
                        y+=1                 
            if side_choose == 0:
                y -= 1                                
                for _ in range(size-1):
                    if (x < 0 or x > self.board_size-1 or y < 0 or y > self.board_size-1) or self.your_board[y][x] in self.your_ships:
                        self.down = []
                        break
                    else:
                        self.down.append(self.your_board[y][x])
                        y-=1
        if self.right == [] and self.left == [] and self.up == [] and self.down == []:
            self.reset_to_next(0)
        else:
            for row in self.your_board:
                for item in row:
                    item.config(state='disabled')
            for item in self.right+self.left+self.up+self.down:
                item.config(bg='green', state='normal')
                item.config(command=lambda ite=item: self.choose_ship_side(ite))
        self.you = 17 - len(self.founded_ships_player)
        self.enemy = 17 - len(self.founded_ships_enemy)                
            
    def choose_ship_side(self, button):
        if button in self.right:
            for item in self.right + [self.current]:
                self.your_ships.append(item)
        elif button in self.left:
            for item in self.left + [self.current]:
                self.your_ships.append(item)
        elif button in self.up:
            for item in self.up + [self.current]:
                self.your_ships.append(item)
        elif button in self.down:
            for item in self.down + [self.current]:
                self.your_ships.append(item)
        self.you = 17 - len(self.founded_ships_player)
        self.enemy = 17 - len(self.founded_ships_enemy)                        
        self.reset_to_next()
                
    def reset_to_next(self, state=1):
        if self.player_ship_size > 2:
            for row in self.your_board:
                for item in row:
                    item.config(bg='white', state='normal')        
                    item.config(command=lambda button=item: self.player_ship_placement(button))
            for ship in self.your_ships:
                ship.config(command=self.your_ship_now())
                ship.config(bg='red')
                ship.config(state='disabled')
            if state == 1:
                if self.player_ship_size == 3 and self.repeat == 1:
                    self.repeat -= 1
                else:
                    self.player_ship_size -= 1
            self.bottom_label.config(text=f"Choose a button to place {self.player_ship_size} square sized ships now.")
        else:
            for row in self.your_board:
                for item in row:
                    item.config(bg='white', state='disabled')
            for ship in self.your_ships:
                ship.config(bg=self.player_ships_color)
            self.bottom_label.config(text=f"Your Turn")
            for row in self.enemy_board:
                for item in row:
                    item.config(state='normal')
                    item.config(command=lambda button=item: self.not_found(button))
            for ship in self.enemy_ships:
                ship.config(command=lambda button=ship: self.shoot_player(button))
        self.you = 17 - len(self.founded_ships_player)
        self.enemy = 17 - len(self.founded_ships_enemy)        
  
    def your_ship_now(self):
        pass

    def return_coor(self, button):
        for i in range(len(self.your_board)):
            for j in range(len(self.your_board[i])):
                if self.your_board[i][j] == button:
                    return [int(i), int(j)]