
people = [
    {'name': 'eden', 'age': 27, 'location': 'austin'},
    {'name': 'alexis', 'age': 23, 'location': 'austin'},
    {'name': 'roy', 'age': 30, 'location': 'dallas'}
]

for person in people:
    print("Name: " + person['name'] + ", Age: " + str(person['age']) + ", Location: " + person['location'])



print("\n")


pets = [
    {'name': 'blue', 'animal': 'dog', 'owner': 'eden'},
    {'name': 'bob', 'animal': 'cat', 'owner': 'alexis'},
    {'name': 'lolipop', 'animal': 'horse', 'owner': 'roy'}
]

for animals in pets:
    print("Name: " + animals['name'], ", Animal: " + animals['animal'], ", Owner: " + animals['owner'])