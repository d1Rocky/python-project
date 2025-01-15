
#created list of people
guest_list = ['dad', 'mom', 'brother']

message = "you are invited to dinner"

#message sent to people
print(guest_list[0] + " " + message)
print(guest_list[1] + " " + message)
print(guest_list[2] + " " + message)

print("\nunfortunatly, " + guest_list[0] + " won't make it")

#modified list by removing a person and adding a new one
del guest_list[0]
guest_list.append('girlfriend')

print(guest_list[0] + " " + message)
print(guest_list[1] + " " + message)
print(guest_list[2] + " " + message)

#insert new people to the list at specific spots
print("\nI found a bigger table!")
guest_list.insert(0,'grandma')
guest_list.insert(2,'grandpa')
guest_list.insert(5,'sister')

print(guest_list[0] + " " + message)
print(guest_list[1] + " " + message)
print(guest_list[2] + " " + message)
print(guest_list[3] + " " + message)
print(guest_list[4] + " " + message)
print(guest_list[5] + " " + message)

#removed people from the list but still item is available to work with
print("\nSorry to announce that only two people can be invited")
remove_guest = guest_list.pop(0)
print(remove_guest + " " + "i'm sorry but you are not invited")
remove_guest = guest_list.pop(0)
print(remove_guest + " " + "i'm sorry but you are not invited")
remove_guest = guest_list.pop(0)
print(remove_guest + " " + "i'm sorry but you are not invited")
remove_guest = guest_list.pop(0)
print(remove_guest + " " + "i'm sorry but you are not invited")

print("\n" + guest_list[0] + " you are still invited to dinner")
print(guest_list[1] + " you are still invited to dinner")

#removed the last two people to make sure list is empty
del guest_list[0]
del guest_list[0]
print(guest_list)