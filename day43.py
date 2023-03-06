import random

bingoCard = []

for i in range(3):
    row = []

    for rowLength in range(3):
        randomNum = random.randrange(1, 90)
        row.append(randomNum)

    bingoCard.append(row)

print(bingoCard)
