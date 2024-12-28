

rivers = {'nile': 'egypt',
          'jordan': 'israel',
          'creek': 'austin'
          }

for river, location in rivers.items():
    print("The " + river.title() + " runs through " + location.title())

print("\n")

for river in rivers.keys():
    print(river.title())

print("\n")

for location in rivers.values():
    print(location.title())

print("\n")

fav_lang = {'roy': 'c',
            'eden': 'python',
            }

people = ['yam', 'brendan', 'roy', 'eden']

for name in people:
    if name in fav_lang:
        print("Thank you " + name.title())
    else:
        print(name.title() + " you need to register")
