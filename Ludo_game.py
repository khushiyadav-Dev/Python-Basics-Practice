import random

# Players
players = ["Player 1", "Player 2"]

# Token positions
positions = [0, 0]

# Winning position
WIN = 20

print("🎲 WELCOME TO LUDO GAME 🎲")

while True:

    for i in range(2):

        print("\n", players[i], "Your Turn!")

        input("Press Enter to roll dice...")

        dice = random.randint(1, 6)

        print("You got:", dice)

        if positions[i] == 0:

            if dice == 6:
                positions[i] = 1
                print("Your token has started!")

            else:
                print("You need 6 to start.")

        else:

            positions[i] += dice

            if positions[i] > WIN:
                positions[i] = WIN

            print("Your position:", positions[i])

        # Check winner
        if positions[i] >= WIN:

            print("\n🏆", players[i], "WINS THE GAME! 🏆")
            exit()
