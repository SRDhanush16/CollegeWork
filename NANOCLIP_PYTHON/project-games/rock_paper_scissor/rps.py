from tkinter import *
import random


class RPS(Frame):
    def __init__(self):
        # Screen Layout
        Frame.__init__(self)
        self.grid()
        self.master.title("Rock | Paper | Scissor")
        global userScore, compScore

        userScore = 0
        compScore = 0
        background = Frame(self, bg="white",
                           width=100, height=400)
        background.grid()
        # Declaring Buttons

        B1 = Frame(background, bg='black', height="10", width="20")
        B1.grid(row=1, column=1, padx = 10)

        t1 = Label(master=B1, text="ROCK",
                   bg="black", fg='white',
                   justify=CENTER, font=("Verdana", 20, "bold"), width=15, height=4)
        t1.grid()
        t1.bind("<Button-1>", self.Rock)

        B2 = Frame(background, bg='black', height="10", width="20")
        B2.grid(row=1, column=2, padx = 10)
        t2 = Label(master=B2, text="PAPER",
                   bg="black", fg='white',
                   justify=CENTER, font=("Verdana", 20, "bold"), width=15, height=4)
        t2.grid()
        t2.bind("<Button-1>", self.Paper)

        B3 = Frame(background, bg='black', height="10", width="20")
        B3.grid(row=1, column=3, padx = 10)
        t3 = Label(master=B3, text="SCISSOR",
                   bg="black", fg='white',
                   justify=CENTER, font=("Verdana", 20, "bold"), width=15, height=4)
        t3.grid()
        t3.bind("<Button-1>", self.Scissor)

        self.text_area = Label(master=self, text="Start your Game by Choosing any of the choices", font=("Verdana", 12), fg='red')
        # text_area.pack()
        self.text_area.grid(pady = 50)

        self.mainloop()

    def Rock(self, rock):

        """ Rock Function with 3 comparision"""

        global userScore, compScore

        comp = random.randint(1, 3)

        if comp == 3:

            comp = "Scissor"

            userScore += 1

            self.text_area['text'] = ("Congratulations!", "You WIN!! \n""Your Choice:Rock" + "\nComp Choice: " \
                                      + comp + "\nYour Score: " + str(userScore) + "\nComputer Score: " + str(
                compScore))

        elif comp == 1:

            comp = "Rock"

            self.text_area['text'] = ("Same pinch!!",
                                      "IT'S A TIE!! !!\n" + "Your Choice:Rock" + "\nComp Choice: " + comp + "\nYour Score: "
                                      + str(userScore) + "\nComputer Score: " + str(compScore))


        else:

            comp = "Paper"

            compScore += 1

            self.text_area['text'] = ("Hard Luck!!",
                                      "YOU LOOSE!!\n" + "Your Choice:Rock" + "\nComp Choice: " + comp + "\nYour Score: "
                                      + str(userScore) + "\nComputer Score: " + str(compScore))

    def Scissor(self, scissor):

        """ Scissor Function with 3 comparision"""
        global userScore, compScore
        comp = random.randint(1, 3)

        if comp == 2:

            comp = "Paper"

            userScore += 1

            self.text_area['text'] = ("Congratulation!!",
                                      "YOU WIN!!\nYour Choice: Scissor\n" + "Comp choice: " + comp + "\nYour Score: " + str(
                                          userScore) + "\nComputer Score: " + str(compScore))

        elif comp == 3:

            comp = "Scissor"

            self.text_area['text'] = ("Same pinch!!",
                                      "IT'S A TIE!!\nYour Choice: Scissor\n" + "Comp choice: " + comp + "\nYour Score: " + str(
                                          userScore) + "\nComputer Score: " + str(compScore))

        else:

            comp = "Rock"

            compScore += 1

            self.text_area['text'] = ("Hard Luck!!",
                                      "YOU LOOSE!!\nYour Choice: Scissor\n" + "Comp choice:" + comp + "\nYour Score: " + str(
                                          userScore) + "\nComputer Score: " + str(compScore))

    def Paper(self, paper):

        """ Paper Function with 3 comparision"""

        global userScore, compScore

        comp = random.randint(1, 3)

        if comp == 1:

            comp = "Rock"

            userScore += 1

            self.text_area['text'] = ("Congratulation!!",
                                      "YOU WIN!!\nYour Choice: Paper\n" + "Comp choice: " + comp + "\nYour Score: " + str(
                                          userScore) + "\nComputer Score: " + str(compScore))

        elif comp == 2:

            comp = "Paper"

            self.text_area['text'] = ("Same pinch!!",
                                      "IT'S A TIE!!\nYour Choice: Paper\n" + "Comp choice: " + comp + "\nYour Score: " + str(
                                          userScore) + "\nComputer Score: " + str(compScore))

        else:

            comp = "Scissor"

            compScore += 1

            self.text_area['text'] = ("Hard Luck!!",
                                      "YOU LOOSE!!\nYour Choice: Paper\n" + "Comp choice:" + comp + "\nYour Score: " + str(
                                          userScore) + "\nComputer Score: " + str(compScore))

