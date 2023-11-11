import argparse
from stat_window import StatisticsWindow
from main_menu import MainMenu
from games.sudoku import BoardSudoku
from games.tictactoe import TicTacToe
from games.memory_game import Memory
from games.battleship import BattleshipGame, DEGREE
    
def run():
    app = MainMenu()
def sudoku():
    new_game = BoardSudoku(9, 1)
def ttt():
    new_game = TicTacToe()
def memory():
    new_game = Memory()
def battlefield():
    new_game = BattleshipGame()
def stats():
    stat = StatisticsWindow()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="crawl helper", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', action='store_true', help='Run Program')
    parser.add_argument('-s', action='store_true', help='Run Only Sudoku')
    parser.add_argument('-t', action='store_true', help='Run Only Tic Tac Toe')
    parser.add_argument('-m', action='store_true', help='Run Only Memory Game')
    parser.add_argument('-b', action='store_true', help='Run Only Battlefield Game')
    parser.add_argument('-x', action='store_true', help='See Stats')
    args = parser.parse_args()
    config = vars(args)
    run_program = config['r']
    run_sudoku = config['s']
    run_ttt = config['t']
    run_memory = config['m']
    run_battleship = config['b']
    see_stats = config['x']
    if run_program:
        run()
    elif run_sudoku:
        sudoku()
    elif run_ttt:
        ttt() 
    elif run_memory:
        memory()
    elif run_battleship:
        battlefield()
    elif see_stats:
        stats()
    else: run()