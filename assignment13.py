

unconfirmed_users = ['alexis', 'eden', 'roy']
confirmed_users = []

while unconfirmed_users:
    current_user = unconfirmed_users.pop()
    print("verified user: " + current_user.title())
    confirmed_users.append(current_user)

print("the following users have been confirmed:")

for confirmed_user in confirmed_users:
    print(confirmed_user.title())