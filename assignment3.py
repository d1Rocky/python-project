
#list will be counted from 1 and adding 2 to it each time to reporesent odd numbers.
odd_numbers = list(range(1,21,2))

for numbers in odd_numbers:
    print(numbers)

#using SLICE for practice
my_food = ['pizza', 'ice cream', 'pasta', 'meat', 'bread']
friend_food = my_food[:]

my_food.append('cheese')
friend_food.append('mushroom')

print('my favorire food are: ')
for food in my_food:
    print(food)

print('my favorire food are: ')
for food in friend_food:
    print(food)
