namesList = []


def printList():
    print()
    for name in namesList:
        print(name)
    print()


while True:
    firstName = input("Item > ").capitalize().strip()
    lastName = input("Item > ").capitalize().strip()
    name = f"{firstName} {lastName}"

    if name not in namesList:
        namesList.append(name)
    printList()
