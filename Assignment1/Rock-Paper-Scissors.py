print("********************************")
print("********************************")
print("2P RPS game")
print("********************************")
print("********************************")
print("Rock-Paper-Scissors")
print("********************************")
print("")
rps_list = ["rock", "paper", "scissors"]
print(rps_list)
print("")




def rps(p1, p2):
    # rps_list = ["rock", "paper", "scissors"]
    p1 = input("Enter Choice:")
    p2 = input("Enter Choice:")
    while p1 not in rps_list or p2 not in rps_list:
        print("Please Enter from the list above")
        print("")
        p1 = input("Enter Choice:")
        p2 = input("Enter Choice")

    while p1 == p2:
        print("Tie!")
        print("")
        p1 = input("Enter Choice:")
        p2 = input("Enter Choice")

    if p1 == 'rock' and p2 == 'paper':
        print("P2 WINS!")

    elif p1 == 'paper' and p2 == 'rock':
        print("P1 WINS!")

    elif p1 == 'rock' and p2 == 'scissors':
        print("P1 WINS!")

    elif p1 == 'scissors' and p2 == 'rock':
        print("P2 WINS!")

    elif p1 == 'scissors' and p2 == 'paper':
        print("P1 WINS!")


ngame = 0
player1 = 0
player2 = 0

while (ngame != "yes"):

    rps(player1, player2)

    ngame = input("Do you want to try again?")
    if ngame == "yes":
        rps(player1, player2)
    elif ngame == "no":
        break
