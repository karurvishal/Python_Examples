from random import randint
choice = ['Rock','Paper','Scissors']
computer = choice[randint(0,2)]
print("welcome to the rock paper game")
player = input("enter your choice : ")
print(f"computers choice is {computer}")
print(f"your choice is {player}")
print("about to begin")
print(player)
print(computer)
if player == computer:
    print("Draw")
elif player == 'Rock' and computer == 'Paper':
    print("computer wins")
elif player == 'Rock' and computer == 'Scissors':
    print("player wins")
elif player == 'Paper' and computer == 'Rock':
    print("player wins")
elif player == 'Paper' and computer == 'Scissors':
    print("computer wins")
elif player == 'Scissors' and computer == 'Paper':
    print("player wins")
elif player == 'Scissors' and computer == 'Rock':
    print("computer wins")
else:
    print("proper input")
          