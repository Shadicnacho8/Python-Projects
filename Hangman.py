from random_words import RandomWords

name = input("What is your name? ")
print("Best of Luck ", name)

r = RandomWords()
word = r.random_word()
print("Guess the characters!!")

guesses = ''

num_chars = len(word)
turns = num_chars

if turns < 5:
    turns = 7
else:
    turns = 10

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char, end="")
        else:
            print("_", end="")
            failed += 1

    print()

    if failed == 0:
        print("You Win!!")
        print("The word is: ", word)
        break

    guess = input("Guess a character: ")
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Wrong")
        print("You have ", turns, " more guesses left. Use wisely")

    if turns == 0:
        print("You Lose")
        print("The word was:", word)