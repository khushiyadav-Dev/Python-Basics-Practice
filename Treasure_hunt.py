import random

def treasure_game():

    print("================================")
    print("     WELCOME TO TREASURE HUNT")
    print("================================")

    print("Find the hidden treasure!")
    print("You have 5 chances.")

    treasure = random.randint(1, 10)
    chances = 5

    while chances > 0:

        guess = int(input("\nGuess a number (1-10): "))

        if guess == treasure:
            print("🎉 Congratulations! You found the treasure!")
            break

        elif guess < treasure:
            print("Hint: Treasure is at a higher number.")

        else:
            print("Hint: Treasure is at a lower number.")

        chances -= 1

        print("Chances left:", chances)

    else:
        print("\nGame Over!")
        print("The treasure was hidden at:", treasure)


if __name__ == "__main__":
    treasure_game()
