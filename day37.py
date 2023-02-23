print("STAR WARS NAME GENERATOR")

names = input("Enter your first name, last name, Mum's maiden name and the city you were born in: ").lower().split()

firstNameSlice = names[0][0:4]
lastNameSlice = names[1][0:4]
motherMaidenNameSlice = names[2][0:2]
birthPlaceSlice = names[3][-3:]

starWarsFirstName = firstNameSlice + lastNameSlice
starWarsLasttName = motherMaidenNameSlice + birthPlaceSlice

print(f"Your Star Wars name is {starWarsFirstName} {starWarsLasttName}")
