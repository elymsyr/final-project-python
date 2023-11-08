import pandas as pd

class StatCsv():
    def __init__(self) -> None:
        self.df = pd.read_csv('stats.csv')
    
    def writer(self):
        self.df.to_csv('stats.csv', index=False)

    def increase_played(self, n):
        df = pd.read_csv('stats.csv')
        row_index = n
        column_name = 'times'
        df.at[row_index, column_name] = int(df.at[row_index, column_name])+1
        df.to_csv('stats.csv', index=False)

    def return_sudoku_stats(self):
        """Function returns sudoku game stats.

        Returns:
            _type_: Dictionary\n
            'times': (int) How many times the game was played.\n
            'highscore': (int in seconds) Minimum time the game was finished.\n
            'win': (int) How many times the game was finished.\n
            'last_scores': (int in seconds) Last 5 scores (in time) the game was finished.\n
        """
        sudoku = self.df.iloc[0].tolist()
        last_scores = self.df['last_scores'].apply(eval)
        last_score = last_scores[0]
        stats = {
            'times': sudoku[1],
            'highscore': sudoku[2],
            'win': sudoku[4],
            'last_scores': last_score
        }
        return stats

    def change_sudoku_stats(self, score):
        """Changes csv file for sudoku game.

        Args:
            score (int): Score in time.
        """
        stats = self.return_sudoku_stats()
        new_score = stats['highscore']
        new_values = ['sudoku']
        if score > 0:
            if stats['highscore'] > score:
                new_score = score
        new_values.append(stats['times'])
        new_values.append(new_score)
        new_values.append(0)
        if score > 0:
            new_values.append(stats['win'] + 1)
        new_values.append(0)
        new_scores = stats['last_scores']
        new_scores.append(score)
        new_scores = new_scores[-5:]
        new_values.append(str(new_scores))
        self.df.at[0, 'last_scores'] = new_values[-1] 
        self.df.iloc[0, 0:-1] = new_values[0:-1] 
        self.writer()

    def return_ttt_stats(self):
        ttt = self.df.iloc[1].tolist()
        stats = {
            'times': ttt[1],
            'draw': ttt[3],
            'win': ttt[4],
            'loses': ttt[5]
        }
        return stats

    def change_ttt_stats(self, score):
        stats = self.return_ttt_stats()
        new_values = ['ttt']
        wins = stats['win']
        draws = stats['draw']
        lose = stats['loses']
        if score == 1:
            wins += 1
        elif score == 0:
            draws += 1
        else:
            lose += 1
        new_values.append(stats['times'])
        new_values.append(0)
        new_values.append(draws)
        new_values.append(wins)
        new_values.append(lose)
        columns_to_update = ['stats', 'times', 'highscore', 'draw', 'win', 'loses']
        self.df.loc[1, columns_to_update] = new_values
        self.writer()

    def return_memory_stats(self):
        """Function returns memory game stats.

        Returns:
            _type_: Dictionary\n
            'times': (int) How many times the game was played.\n
            'highscore': (int in seconds) Minimum time the game was finished.\n
            'win': (int) How many times the game was finished.\n
            'last_scores': (int in seconds) Last 5 scores (in time) the game was finished.\n
        """
        memory = self.df.iloc[2].tolist()
        last_scores = self.df['last_scores'].apply(eval)
        last_score = last_scores[2]
        stats = {
            'times': memory[1],
            'highscore': memory[2],
            'win': memory[4],
            'last_scores': last_score
        }
        return stats

    def change_memory_stats(self, score):
        """Changes csv file for memory game.

        Args:
            score (int): Score in time.
        """
        stats = self.return_memory_stats()
        new_score = stats['highscore']
        new_values = ['memory']
        if score > 0:
            if stats['highscore'] > score:
                new_score = score
        new_values.append(stats['times'])
        new_values.append(new_score)
        new_values.append(0)
        if score > 0:
            new_values.append(stats['win'] + 1)
        new_values.append(0)
        new_scores = stats['last_scores']
        new_scores.append(score)
        new_scores = new_scores[-5:]
        new_values.append(str(new_scores))
        self.df.at[2, 'last_scores'] = new_values[-1] 
        self.df.iloc[2, 0:-1] = new_values[0:-1] 
        self.writer()

    def return_battleship_stats(self):
        """Function returns battleship game stats.

        Returns:
            _type_: Dictionary\n
            'times': (int) How many times the game was played.\n
            'highscore': (int in seconds) Minimum time the game was finished.\n
            'win': (int) How many times the game was finished.\n
            'last_scores': (int in seconds) Last 5 scores (in time) the game was finished.\n
        """
        battleship = self.df.iloc[3].tolist()
        last_scores = self.df['last_scores'].apply(eval)
        last_score = last_scores[3]
        stats = {
            'times': battleship[1],
            'highscore': battleship[2],
            'win': battleship[4],
            'loses': battleship[5],
            'last_scores': last_score
        }
        return stats

    def change_battleship_stats(self, score):
        """Changes csv file for battleship game.

        Args:
            score (int): Score in time.
        """
        stats = self.return_battleship_stats()
        new_score = stats['highscore']
        new_values = ['battleship']
        if score > 0:
            if stats['highscore'] < score:
                new_score = score
        new_values.append(stats['times'])
        new_values.append(new_score)
        new_values.append(0)
        if score > 0:
            new_values.append(stats['win'] + 1)
        else:
            new_values.append(stats['win'])
        if score < 0:
            new_values.append(stats['loses'] + 1)
        else:
            new_values.append(stats['loses'])
        new_scores = stats['last_scores']
        new_scores.append(score)
        new_scores = new_scores[-5:]
        new_values.append(str(new_scores))
        self.df.at[3, 'last_scores'] = new_values[-1] 
        self.df.iloc[3, 0:-1] = new_values[0:-1] 
        self.writer()

    def reset_stats(self):
        zeros = ['stats,times,highscore,draw,win,loses,last_scores','sudoku,0,0,0,0,0,"[0, 0, 0, 0, 0]"','ttt,0,0.0,0,0,0,"[0,0,0,0,0]"','memory,0,0,0,0,0,"[0, 0, 0, 0, 0]"','battleship,0,0,0,0,0,"[0, 0, 0, 0, 0]"']
        with open("stats.csv", "w") as file:
            for row in zeros:
                file.writelines(row)
                file.writelines("\n")
