import random

def play_game():

    print("==============================")
    print("   ROCK PAPER SCISSORS GAME")
    print("==============================")

    choices = ["rock", "paper", "scissors"]

    user_score = 0
    computer_score = 0

    for round in range(1, 6):

        print("\nRound:", round)

        user = input("Choose rock, paper or scissors: ").lower()

        if user not in choices:
            print("Invalid choice! Try again.")
            continue

        computer = random.choice(choices)

        print("You chose:", user)
        print("Computer chose:", computer)

        if user == computer:
            print("It's a Draw!")

        elif (
            (user == "rock" and computer == "scissors")
            or (user == "paper" and computer == "rock")
            or (user == "scissors" and computer == "paper")
        ):
            print("You Win!")
            user_score += 1

        else:
            print("Computer Wins!")
            computer_score += 1

    print("\n========== FINAL RESULT ==========")

    print("Your Score:", user_score)
    print("Computer Score:", computer_score)

    if user_score > computer_score:
        print("🏆 YOU ARE THE CHAMPION!")

    elif user_score < computer_score:
        print("Computer Wins The Game!")

    else:
        print("Match Draw!")

if __name__ == "__main__":
    play_game()
