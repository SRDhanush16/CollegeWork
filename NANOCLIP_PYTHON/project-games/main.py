import two_zero_four_eight.puzzle as g2048
import tic_tac_toe.tic_tac_toe as ttt
import rock_paper_scissor.rps as rps
from tkinter import *




class Game(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.grid_cells = []
        self.master.title('Nanoclip')
        self.game_box()
        self.mainloop()

        
        
    def game_box(self):
        label = Label(master=self, text="SELECT A GAME TO PLAY ", font=("Verdana", 24, "bold"), fg='red')
        label.grid()
        background = Frame(self, bg="#92877d",
                           width=100, height=400)
        background.grid()
        games = [["2048", "#ef6c00"], ["Tic-Tac-Toe", "blue"], ["Rock Paper Scissors", "red"]]
        grid_row = []
        for index, game in enumerate(games):
            cell = Frame(background, bg=game[1],
                         width=100,
                         height=100)
            cell.grid(row=1, column=index + 1, padx=10,
                      pady=10)
            t = Label(master=cell, text=game[0],
                      bg=game[1], fg='white',
                      justify=CENTER, font=("Verdana", 20, "bold"), width=15, height=4)
            t.grid()
            t.bind("<Button-1>", lambda e, ga=game[0]: self.play_game(ga))
            grid_row.append(t)

        self.grid_cells.append(grid_row)
        
   
        
    def play_game(self, game):
        Frame.destroy(self)
        print(game)
        if game == "Tic-Tac-Toe":
            ttt.TicTacToe()
        elif game == "2048":
            g2048.GameGrid()
        else:
            rps.RPS()
    
    
    
    
Game()
