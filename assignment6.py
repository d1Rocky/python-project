
person = {'first_name': 'alexis',
          'last_name': 'delgado', 
          'age': 23,
          'city': 'austin'
          }

print(person['first_name'])
print(person['last_name'])
print(person['age'])
print(person['city'])


print("\n")

fav_number = {'eden': 15,
              'alexis': 10,
              'roy': 24,
              'yam': 99,
              'brendan': 30
              }

print("Alexis's favorite number is: " + str(fav_number['alexis']))
print("Eden's favorite number is: " + str(fav_number['eden']))
#key and value can be changed to any variables to store the data inside of them
for key, value in fav_number.items():
    print("\nKey: " + str(key))
    print("Value: " + str(value))

friends = ['roy', 'yam']
#keys() only work with the first value rather than both values in the dictionary
#if you want to get the second value put values() instead
for name in fav_number.keys(): #this code can also be written without keys()
    print("\n" + name.title())

    if name in friends: #checks if name is in friends list
        print("Hi " + name.title() + " I see your favorite number is: " + str(fav_number[name]))
#we use the name of the dictionary and the current value of name as the key

    if 'tony' not in fav_number.keys():
        print("\nTony, please tell us your favorite number")