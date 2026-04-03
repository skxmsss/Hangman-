from getpass import getpass

first = input("Enter your name: ")
word = getpass(f"{first}, enter the secret word: ").lower()

guessed = []
chances = 10

second = input("Enter another player name: ")
print(f"\n{second}, start guessing!")

while chances > 0:
    display = ""

    for letter in word:
        if letter in guessed:
            display += letter
        else:
            display += "_"

    print("\nWord:", " ".join(display))
    print("Guessed:", guessed)

    if "_" not in display:
        print(f" {second} wins!")
        break

    guess = input("Enter a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Enter only one letter!")
        continue

    if guess in guessed:
        print("Already guessed!")
        continue

    guessed.append(guess)

    if guess not in word:
        chances -= 1
        print("Wrong! Chances left:", chances)

else:
    print(f" {second} lost! Word was: {word}")