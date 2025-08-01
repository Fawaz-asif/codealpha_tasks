import random

print("WELCOME TO THE HANGMAN GAME")

# Predefined words to choose from
words = ("hello", "country", "guess", "hangman", "game")

# Hangman drawing states
hangman = {
    0: (),
    1: (" o  ",
        "    ",
        "    "),
    2: (" o  ",
        " |  ",
        "    "),
    3: (" o  ",
        " |\\",
        "    "),
    4: (" o  ",
        "/|\\",
        "    "),
    5: (" o  ",
        "/|\\",
        "/   "),
    6: (" o  ",
        "/|\\",
        "/\\ ")
}

# Function to display hangman based on number of wrong guesses
def display_hangman(wrong_guess):
    for line in hangman[wrong_guess]:
        print(line)

# Function to show current state of the guessed word
def display_hint(hint):
    print(" ".join(hint))

# Main game logic
def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guess = 0
    guessed_letters = set()
    while_playing = True

    while while_playing:
        display_hangman(wrong_guess)
        display_hint(hint)

        guess = input("Enter your guess: ").lower()

        # Input validation
        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single letter.")
            continue

        if guess in guessed_letters:
            print("You've already guessed that letter. Try a different one.")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
            if "".join(hint) == answer:
                print(f'Congrats! You guessed the word correctly: "{answer}"')
                while_playing = False
        else:
            print("Wrong guess! Try again.")
            wrong_guess += 1
            if wrong_guess == 6:
                print("YOU LOST!")
                display_hangman(wrong_guess)
                print(f'The correct word was: "{answer}"')
                while_playing = False

# Replay loop
while True:
    main()
    check = input("Press 1 to play again or any other button to exit: ")
    if check != "1":
        print("Thanks for playing!")
        break