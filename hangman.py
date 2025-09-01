import random

word = random.choice(["apple", "banana", "grapes", "mango", "peach", "orange", "strawberry"])
lives, guessed, hidden = 6, [], ["_"] * len(word)

print("Welcome to Hangman!\n" + " ".join(hidden))
while lives > 0 and "_" in hidden:
    g = input("Guess a letter: ").lower()
    if g in guessed: print("Already guessed."); continue
    guessed.append(g)
    if g in word:
        for i, c in enumerate(word):
            if c == g: hidden[i] = g
        print("Correct!")
    else:
        lives -= 1
        print(f"Wrong! Lives left: {lives}")
    print(" ".join(hidden), "\nGuessed so far:", ", ".join(guessed))

print(("You win! The word was: " if "_" not in hidden else "You lost! The word was:"), word)
