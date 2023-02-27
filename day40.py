print("🌟Contact Card🌟")
print()

userName = input("Input your name: ")
userDateOfBirth = input("Input your date of birth: ")
userPhone = input("Input your telephone number: ")
userEmail = input("Input your email: ")
userAddress = input("Input your address: ")

userData = {
    "name": userName,
    "dateOfBirth": userDateOfBirth,
    "phone": userPhone,
    "email": userEmail,
    "address": userAddress
}

print(f"""
Hi {userData['name']}. Our dictionary says that you were born on {userData['dateOfBirth']}, 
we can call you on {userData['phone']}, email {userData['email']}, or write to 
{userData['address']}.
""")
