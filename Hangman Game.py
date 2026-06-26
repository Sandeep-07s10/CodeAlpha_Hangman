import random


words = ["dhanush", "uday", "naveen", "praveen", "sandeep"]


secret_word = random.choice(words)

guessed_letters = []

wrong_guesses = 6

print("===== HANGMAN GAME =====")

while wrong_guesses > 0:

    display_word = ""

    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    if "_" not in display_word:
        print("a Congratulations! You guessed the word.")
        break

    guess = input("Enter a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess not in secret_word:
        wrong_guesses -= 1
        print("Wrong Guess!")
        print("Remaining Chances:", wrong_guesses)

else:
    print("\nGame Over!")
    print("The word was:", secret_word)