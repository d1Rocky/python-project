#create an empty list
squares = []
#iterate over numbers 1-4
for value in range(1,5):
    squares.append(value**2) #calculate the square of the number and add it to the list

print(squares)

#advanced option is to do this:
squares = [value**2 for value in range(1,11)]
print(squares)