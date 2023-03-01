dictionary = {"name" : None, "url": None, "description": None, "rating": None}

for key in dictionary.keys():
  dictionary[key] = input(f"{key}: ")

print()
for key, value in dictionary.items():
  print(f"{key} {value}")