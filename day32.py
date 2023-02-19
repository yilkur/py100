import random

greetings = ["Salve", "Bonjour", "Konnichiwa", "Olá", "Goddag", "Shikamoo"]
randomIdx = random.randint(0, len(greetings) - 1)
randomGreeting = greetings[randomIdx]

print(randomGreeting)