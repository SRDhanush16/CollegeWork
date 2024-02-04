from tkinter import *
import tkinter.messagebox           # because at the end to show the result eg(you win ,its a tie)


class TicTacToe(Frame):           # class is used as blueprint to create object
    def __init__(self):
        Frame.__init__(self)
        self.grid()
        self.master.title("Tic Tac Toe")

        self.pa = StringVar()
        self.playerb = StringVar()
        self.p1 = StringVar()
        self.p2 = StringVar()
        tk = Frame(self, bg="black",          
                   width=100, height=500)
        tk.grid()
        self.player1_name = Entry(tk, textvariable=self.p1, bd=5)
        self.player1_name.grid(row=1, column=1, columnspan=8)
        self.player2_name = Entry(tk, textvariable=self.p2, bd=5)
        self.player2_name.grid(row=2, column=1, columnspan=8)

        self.bclick = True
        self.flag = 0
        self.buttons = StringVar()

        label = Label(tk, text="Player 1:", font='Times 25 bold', bg='black', fg='white', height=1, width=8)              # players  1: name input  box
        label.grid(row=1, column=0)

        label = Label(tk, text="Player 2:", font='Times 25 bold', bg='black', fg='white', height=1, width=8)             # player  2 : name input box
        label.grid(row=2, column=0)

        self.button1 = Button(tk, text=" ", font='Times 25 bold', bg='white', fg='black', height=4, width=10,          # background colour and font colour in each button
                              command=lambda: self.btnClick(self.button1))
        self.button1.grid(row=3, column=0)

        self.button2 = Button(tk, text=' ', font='Times 25 bold', bg='white', fg='black', height=4, width=10,
                              command=lambda: self.btnClick(self.button2))
        self.button2.grid(row=3, column=1)

        self.button3 = Button(tk, text=' ', font='Times 25 bold', bg='white', fg='black', height=4, width=10,
                              command=lambda: self.btnClick(self.button3))
        self.button3.grid(row=3, column=2)

        self.button4 = Button(tk, text=' ', font='Times 25 bold', bg='white', fg='black', height=4, width=10,
                              command=lambda: self.btnClick(self.button4))
        self.button4.grid(row=4, column=0)

        self.button5 = Button(tk, text=' ', font='Times 25 bold', bg='white', fg='black', height=4, width=10,
                              command=lambda: self.btnClick(self.button5))
        self.button5.grid(row=4, column=1)

        self.button6 = Button(tk, text=' ', font='Times 25 bold', bg='white', fg='black', height=4, width=10,
                              command=lambda: self.btnClick(self.button6))
        self.button6.grid(row=4, column=2)

        self.button7 = Button(tk, text=' ', font='Times 25 bold', bg='white', fg='black', height=4, width=10,
                              command=lambda: self.btnClick(self.button7))
        self.button7.grid(row=5, column=0)

        self.button8 = Button(tk, text=' ', font='Times 25 bold', bg='white', fg='black', height=4, width=10,
                              command=lambda: self.btnClick(self.button8))
        self.button8.grid(row=5, column=1)

        self.button9 = Button(tk, text=' ', font='Times 25 bold', bg='white', fg='black', height=4, width=10,
                              command=lambda: self.btnClick(self.button9))
        self.button9.grid(row=5, column=2)

        tk.mainloop()

    def disableButton(self):                                     # this function is used because the second player cannot input on the button which has already taken input
        self.button1.configure(state=DISABLED) 
        self.button2.configure(state=DISABLED)
        self.button3.configure(state=DISABLED)
        self.button4.configure(state=DISABLED)
        self.button5.configure(state=DISABLED)
        self.button6.configure(state=DISABLED)
        self.button7.configure(state=DISABLED)
        self.button8.configure(state=DISABLED)
        self.button9.configure(state=DISABLED)

    def btnClick(self, buttons):
        # global bclick, flag, player2_name, player1_name, playerb, pa
        if buttons["text"] == " " and self.bclick == True:
            buttons["text"] = "X"
            self.bclick = False
            self.playerb = self.player2_name.get() + " Wins!"
            self.playera = self.player1_name.get() + " Wins!"
            self.checkForWin()
            self.flag += 1

        elif buttons["text"] == " " and self.bclick == False:
            buttons["text"] = "O"
            self.bclick = True
            self.checkForWin()
            self.flag += 1
        else:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "Button already Clicked!")

    def checkForWin(self):                                                                                                                  # conditions for win
        if (self.button1['text'] == 'X' and self.button2['text'] == 'X' and self.button3['text'] == 'X' or
                self.button4['text'] == 'X' and self.button5['text'] == 'X' and self.button6['text'] == 'X' or
                self.button7['text'] == 'X' and self.button8['text'] == 'X' and self.button9['text'] == 'X' or
                self.button1['text'] == 'X' and self.button5['text'] == 'X' and self.button9['text'] == 'X' or
                self.button3['text'] == 'X' and self.button5['text'] == 'X' and self.button7['text'] == 'X' or
                self.button3['text'] == 'X' and self.button6['text'] == 'X' and self.button9['text'] == 'X' or
                self.button1['text'] == 'X' and self.button4['text'] == 'X' and self.button7['text'] == 'X' or
                self.button2['text'] == 'X' and self.button5['text'] == 'X' and self.button8['text'] == 'X' or
                self.button7['text'] == 'X' and self.button6['text'] == 'X' and self.button9['text'] == 'X'):
            self.disableButton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", self.playera)

        elif ((self.button1['text'] == 'O' and self.button2['text'] == 'O' and self.button3['text'] == 'O') or
              (self.button4['text'] == 'O' and self.button5['text'] == 'O' and self.button6['text'] == 'O') or
              (self.button7['text'] == 'O' and self.button8['text'] == 'O' and self.button9['text'] == 'O') or
              (self.button1['text'] == 'O' and self.button5['text'] == 'O' and self.button9['text'] == 'O') or
              (self.button3['text'] == 'O' and self.button5['text'] == 'O' and self.button7['text'] == 'O') or
              (self.button3['text'] == 'O' and self.button6['text'] == 'O' and self.button9['text'] == 'O') or
              (self.button1['text'] == 'O' and self.button4['text'] == 'O' and self.button7['text'] == 'O') or
              (self.button2['text'] == 'O' and self.button5['text'] == 'O' and self.button8['text'] == 'O') or
              (self.button7['text'] == 'O' and self.button6['text'] == 'O' and self.button9['text'] == 'O')):
            self.disableButton()
            tkinter.messagebox.showinfo("Tic-Tac-Toe", self.playerb)

        elif self.flag == 8:
            tkinter.messagebox.showinfo("Tic-Tac-Toe", "It is a Tie")
    
        
