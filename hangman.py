import random

# List of words
words = ["apple", "banana", "grape", "mango", "orange"]

# Pick a random word
word = random.choice(words)

# Set initial values
guessed_letters = []
chances = 6# You can change this to reduce or increase attempts
word_display = ["_"] * len(word)

print("Welcome to Hangman!")

# Main game loop
while chances > 0 and "_" in word_display:
    print("\nWord:", " ".join(word_display))
    print("Chances left:", chances)
    guess = input("Guess a letter: ").lower()

    # Check if input is valid
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter one letter only.")
        continue

    # Already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check if guess is correct
    if guess in word:
        print("Good job! You guessed a letter.")
        for i in range(len(word)):
            if word[i] == guess:
                word_display[i] = guess
    else:
        print("Wrong guess.")
        chances -= 1

# Game result
if "_" not in word_display:
    print("\nCongratulations! You guessed the word:", word)
else:
    print("\nOut of chances. The word was:", word)
