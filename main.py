import random

gameover = False

while gameover != True:
    print("Welcome to the Game of Rock , Paper , Scissors!!!\n""Made By Airaf Hussain!")
    print("What would you like to do?")

    options = int(input("*To play with Computer press 1 \n""*To Play 2 players press 2 \n"))

    if options == 2:
        print("Welcome to Rock,Paper,Scissors!")
        player1 = input("Player1 Enter Rock, Paper, Scissors= ")
        player2 = input("Player2 Enter Rock, Paper, Scissors= ")
        player1.islower()
        player2.islower()
        if player1 == "rock" and player2 == "scissors":
            print("Player1 Wins!")
            player1 = input("Do you want to play again? y/n ")
            if player1 == "y":
                gameover=False
            else:
                gameover=True
        elif  player1 == "paper" and player2 == "rock":
            print('Player1 Wins!')
            player1 = input("Do you want to play again? y/n ")
            if player1 == "y":
                gameover = False
            else:
                gameover = True
        elif player1 == "scissors" and player2 == "paper":
            print("Player1 Wins")
            player1 = input("Do you want to play again? y/n ")
            if player1 == "y":
                gameover = False
            else:
                gameover = True

        elif player2 == "rock" and player1 == "scissors":
            print("Player2 Wins!")
            player2 = input("Do you want to play again? y/n ")
            if player2 == "y":
                gameover = False
            else:
                gameover = True
        elif  player2 == "paper" and player1 == "rock":
            print('Player2 Wins!')
            player2 = input("Do you want to play again? y/n ")
            if player2 == "y":
                gameover = False
            else:
                gameover = True
        elif player2 == "scissors" and player1 == "paper":
            print("Player2 Wins")
            player2 = input("Do you want to play again? y/n ")
            if player2 == "y":
                gameover = False
            else:
                gameover = True

        elif player1 == "rock" and player2 == "rock":
            print("The Match was a Draw!")

            playagain = input("Do you wanna play again? y/n ")
            if playagain == "y":
                gameover = False
            else:
                gameover = True
        elif player1 == "paper" and player2 == "paper":
            print("The Match was a Draw!")
            playagain = input("Do you wanna play again? y/n  ")
            if playagain == "y":
                gameover = False
            else:
                gameover = True
        elif player1 == "scissors" and player2 == "scissors":
            print("The Match was a Draw!")
            playagain =  input("Do you wanna play again? y/n ")
            if playagain == "y":
                gameover = False
            else:
                gameover = True

    elif options == 1:
        print("Welcome to Rock,Paper,Scissors!")
        player = input("Player1 Enter Rock, Paper, Scissors= ")
        player.islower()

        if player == "rock":
            player = 1
        elif player == "paper":
            player = 2
        elif player == "scissors":
            player = 3

        computer = random.randrange(1 , 3)

        if player == 1 and computer == 3:
            print(" Computer chose scissors\n" "You WON!!!")
            playagain = input("Do you wanna play again? y/n ")
            if playagain == "y":
                gameover = False
            else:
                gameover = True
        elif player == 2 and computer == 1:
            print(" Computer chose rock\n" "You WON!!!")
            playagain = input("Do you wanna play again? y/n ")
            if playagain == "y":
                gameover = False
            else:
                gameover = True
        elif player == 3 and computer == 2:
            print(" Computer chose paper\n" "You WON!!!")
            playagain = input("Do you wanna play again? y/n ")
            if playagain == "y":
                gameover = False
            else:
                gameover = True

        elif player == 1 and computer == 2:
            print(" Computer chose paper\n" "You Lost :((")
            playagain = input("Do you wanna play again? y/n ")
            if playagain == "y":
                gameover = False
            else:
                gameover = True
        elif player == 2 and computer == 3:
            print(" Computer chose scissors\n" "You Lost :((")
            playagain = input("Do you wanna play again? y/n ")
            if playagain == "y":
                gameover = False
            else:
                gameover = True
        elif player == 3 and computer == 1:
            print(" Computer chose rock\n" "You Lost :((")
            playagain = input("Do you wanna play again? y/n ")
            if playagain == "y":
                gameover = False
            else:
                gameover = True

        elif player == 1 and computer == 1:
            print(" The match was a draw!!")
            playagain = input("Do you wanna play again? y/n ")
            if playagain == "y":
                gameover = False
            else:
                gameover = True
        elif player == 2 and computer == 2:
            print(" The match was a draw!!")
            playagain = input("Do you wanna play again? y/n ")
            if playagain == "y":
                gameover = False

            else:
                gameover = True
        elif player == 3 and computer == 3:
            print(" The match was a draw!!")
            playagain = input("Do you wanna play again? y/n ")
            if playagain == "y":
                gameover = False
            else:
                gameover = True




