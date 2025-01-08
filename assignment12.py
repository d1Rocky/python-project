


while True:
    user = input("Please enter your toppings: ")

    if user == 'quite':
        break
    else:
        print("I will add " + user + " to your pizza")

print("\n")


while True:
    user_age = int(input("Enter your age: "))

    if user_age <= 3:
        print("Your ticket will be free!")
    elif user_age > 3 and user_age < 12:
        print("Your ticket cost $10")
    elif user_age > 12:
        print("Your ticket is $15")





