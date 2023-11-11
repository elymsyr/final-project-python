import tkinter as tk
from stat_control import StatCsv

class StatisticsWindow:
    def __init__(self):
        self.game_stats = None
        self.create_()
        self.create_window()
        self.root.mainloop()
        
    def create_(self):
        self.root = tk.Tk()
        self.root.geometry("410x550")
        self.root.title('Statistics')
        self.root.iconbitmap("letter-g.ico")  # attributes for icon to popo2021, https://www.flaticon.com/free-icons/letter-g"
        self.stats = StatCsv()
    
    def create_window(self):

        sudoku_stats = self.stats.return_sudoku_stats()
        
        stats_label = tk.Label(self.root, text=f'Statistics for Sudoku', font=('Helvetica', 20))
        stats_label.pack()
        s_games_played_label = tk.Label(self.root, text=f"Games Played: {sudoku_stats['times']}", font=('Helvetica', 15))
        s_games_played_label.pack()

        s_h = tk.Label(self.root, text=f"Highscore: {str(sudoku_stats['highscore'])[:5]}", font=('Helvetica', 14))
        s_h.pack()

        s_w = tk.Label(self.root, text=f"Wins: {sudoku_stats['win']}", font=('Helvetica', 14))
        s_w.pack()
        last_scores = [(str(score)[:4]) for score in sudoku_stats['last_scores']]
        scores_text = ""
        for score in last_scores:
            scores_text += score
            scores_text += ", "
        s_s = tk.Label(self.root, text=f"Last Scores: {scores_text[:-2]}", font=('Helvetica', 14))
        s_s.pack()
        
        ttt_stats = self.stats.return_ttt_stats()
        
        stats_label = tk.Label(self.root, text=f'Statistics for Tic Tac Toe', font=('Helvetica', 20))
        stats_label.pack()
        t_games_played_label = tk.Label(self.root, text=f"Games Played: {ttt_stats['times']}", font=('Helvetica', 15))
        t_games_played_label.pack()
        
        t_w = tk.Label(self.root, text=f"Wins: {ttt_stats['win']}", font=('Helvetica', 14))
        t_w.pack()

        t_d = tk.Label(self.root, text=f"Draws: {str(ttt_stats['draw'])}", font=('Helvetica', 14))
        t_d.pack()
        
        t_l = tk.Label(self.root, text=f"Loses: {str(ttt_stats['loses'])}", font=('Helvetica', 14))
        t_l.pack()

        memory_stats = self.stats.return_memory_stats()
        
        stats_label = tk.Label(self.root, text=f'Statistics for Memory', font=('Helvetica', 20))
        stats_label.pack()
        s_games_played_label = tk.Label(self.root, text=f"Games Played: {memory_stats['times']}", font=('Helvetica', 15))
        s_games_played_label.pack()

        s_h = tk.Label(self.root, text=f"Highscore: {str(memory_stats['highscore'])[:5]}", font=('Helvetica', 14))
        s_h.pack()

        s_w = tk.Label(self.root, text=f"Wins: {memory_stats['win']}", font=('Helvetica', 14))
        s_w.pack()
        last_scores = [(str(score)[:4]) for score in memory_stats['last_scores']]
        scores_text = ""
        for score in last_scores:
            scores_text += score
            scores_text += ", "
        s_s = tk.Label(self.root, text=f"Last Scores: {scores_text[:-2]}", font=('Helvetica', 14))
        s_s.pack()
        
        battleship_stats = self.stats.return_battleship_stats()
        
        stats_label = tk.Label(self.root, text=f'Statistics for Battleship', font=('Helvetica', 20))
        stats_label.pack()
        b_games_played_label = tk.Label(self.root, text=f"Games Played: {battleship_stats['times']}", font=('Helvetica', 15))
        b_games_played_label.pack()

        b_h = tk.Label(self.root, text=f"Highscore: {str(battleship_stats['highscore'])[:5]}", font=('Helvetica', 14))
        b_h.pack()

        b_w = tk.Label(self.root, text=f"Wins: {battleship_stats['win']}", font=('Helvetica', 14))
        b_w.pack()
        last_scores = [(str(score)[:4]) for score in battleship_stats['last_scores']]
        scores_text = ""
        for score in last_scores:
            scores_text += score
            scores_text += ", "
        b_s = tk.Label(self.root, text=f"Last Scores: {scores_text[:-2]}", font=('Helvetica', 14))
        b_s.pack()

        reset_button = tk.Button(self.root, text='Reset Stats', command=self.reset, font=('Helvetica', 12))
        reset_button.pack()        
        quit_button = tk.Button(self.root, text='Close', command=self.close_window, font=('Helvetica', 12))
        quit_button.pack()
        
    def close_window(self):
        self.root.destroy()
        
    def reset(self):
        self.stats.reset_stats()
        self.root.destroy()
        self.create_()
        self.create_window()
    
    def clear(self):
        for widget in self.root.winfo_children():
            print("cleared", widget)
            widget.destroy()
            del widget