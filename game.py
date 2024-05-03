import random
user = input("Select a random option from (Rock Paper and Scissors)")

possible_actions = ("rock","paper","scissors")
computer = random.choice(possible_actions)

if user == computer:
    print("Its a tie my frnds!!")
elif user == "rock":
    if computer == "paper":
        print("U loseeeeee !!!!!!!!!")
    else:
        print("U win!!!!!!!")

elif user == "rock":
    if computer == "scissors":
        print("u winnn again!!!!")
    else:
        print("U lose again!!!!!")

elif user == "paper":
    if computer == "scissors":
        print("u loseeee!!!!")
    else:
        print("u win !!!!!")


