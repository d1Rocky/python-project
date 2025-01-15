

user = int(input("Please give me a number: "))

num = user
if num % 10 == 0: # whether a number is a multiple of 10
    print(num)
else:
    print("ERROR! Try different number.")

print("\n")

counting = 1

while counting <= 5:
    print(counting)
    counting += 1

print("\n")

promt = "Enter 'quite' if you want to end the program. "
message = ""

while message != 'quite':
    message = input(promt)
    print(message)