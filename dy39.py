import random

print("🌟Hangman🌟")
print("")

lifes = 6
listOfWords = [
    "british", "suave", "integrity", "accent", "evil", "genius", "Downton"
]
wordChosen = random.choice(listOfWords)

display = ""

for letter in wordChosen:
    display += '-'

while lifes > 0:
    userLetter = input("Choose a letter: ")

    if userLetter in wordChosen and userLetter != '':
        tempDisplay = list(display)
        for idx, letter in enumerate(wordChosen):
            if userLetter == letter:
                tempDisplay[idx] = letter
        tempDisplay = ''.join(tempDisplay)
        display = tempDisplay
        print("Correct!")
        print(display)
    else:
        lifes -= 1
        print("Nope! Not in there.")
        print(f"{lifes} left")

    if display == wordChosen:
        print(f"You won with {lifes} left!")
        quit()

print("You lost :(")
print(f"The answer was '{wordChosen}'")
