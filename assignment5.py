

usernames = ['d1rocky', 'mewo-mewo', 'admin', 'leewar', 'dorgol']

for username in usernames:
    if username == 'admin':
        print("Hello admin, would you like to see a status report")
    else:
        print("Hello Eric, thank you for logging in again")


print('\n')


current_users = ['d1rocky', 'mewo-mewo', 'admin', 'leewar', 'dorgol']
new_users = ['d1rocky', 'mewo-mewo', 'tonny', 'alex', 'jason']

#loop through the list of new users
for new_users in new_users: 
#inside the loop we check if each username has been used
    if new_users in current_users:
        print("Please enter a new username")
    else:
        print("Username is available")


print("\n")


numbers = [1,2,3,4,5,6,7,8,9]

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print('3rd')
    elif number == 4:
        print("4th")
    elif number == 5:
        print("5th")
    elif number == 6:
        print("6th")
    elif number == 7:
        print("7th")
    elif number == 8:
        print("8th")
    elif number == 9:
        print("9th")