import random

bingoCard = []

for i in range(3):
    row = []
    for rowLength in range(3):
        randomNum = random.randrange(1, 90)
        row.append(randomNum)

    bingoCard.append(row)

print(bingoCard)

winningScore = len(bingoCard) * len(bingoCard[0])
userScore = 0

while True:
    guess = int(input("What number comes up next? > "))

    for row in range(len(bingoCard)):
        for cell in range(len(bingoCard[0])):
            if guess == bingoCard[row][cell]:
                userScore += 1
                print(f'Correct! Your score is {userScore}/{winningScore}')
                bingoCard[row][cell] = 'X'

    if userScore == winningScore:
        break

print(bingoCard)
print("you have won!")
