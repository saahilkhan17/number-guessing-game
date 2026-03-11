import random

print("🎮 Welcome to the Number Guessing Game")

while True:

    # Difficulty selection
    difficulty = input("Choose difficulty (easy / medium / hard / custom): ").lower()

    if difficulty == "easy":
        guesses_left = 10
    elif difficulty == "medium":
        guesses_left = 7
    elif difficulty == "hard":
        guesses_left = 5
    elif difficulty == "custom":
        guesses_left = int(input("Enter number of guesses you want: "))
    else:
        print("Invalid difficulty. Default set to Medium.")
        guesses_left = 7

    target = random.randint(1, 100)

    print("\nI have selected a number between 1 and 100")

    # Game loop
    while guesses_left > 0:

        userChoice = input(f"Guess the number (Guesses left: {guesses_left}) or Quit (Q): ")

        if userChoice.upper() == "Q":
            print("The number was:", target)
            break

        if not userChoice.isdigit():
            print("⚠ Please enter a valid number")
            continue

        userChoice = int(userChoice)

        if userChoice == target:
            print("🎉 SUCCESS! You guessed the correct number!")
            break
        elif userChoice > target:
            print("📉 Too big! Try a smaller number")
        else:
            print("📈 Too small! Try a bigger number")

        guesses_left -= 1

    if guesses_left == 0:
        print("❌ You ran out of guesses!")
        print("The number was:", target)

    # Replay option
    replay = input("\nDo you want to play again? (yes/no): ").lower()
    if replay != "yes":
        print("Thanks for playing!")
        break