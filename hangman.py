import random

# Step 1: Word list and picking a word
word_list = ["apple", "banana", "grapes", "mango", "peach", "orange", "strawberry"]
word = random.choice(word_list)

# Step 2: Game setup
lives = 6
guessed_letters = []
hidden_word = ["_" for _ in word]

print("Welcome to Hangman!")
print(" ".join(hidden_word))

# Step 3: Game loop
while lives > 0 and "_" in hidden_word:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                hidden_word[i] = guess
        print("Correct!")
    else:
        lives -= 1
        print(f"Wrong! Lives left: {lives}")

    print(" ".join(hidden_word))
    print("Guessed so far:", ", ".join(guessed_letters))

# Step 4: Win or lose
if "_" not in hidden_word:
    print(" You win! The word was:", word)
else:
    print(" You lost! The word was:", word)
