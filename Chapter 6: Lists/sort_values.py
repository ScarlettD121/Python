#Scarlett Dowdle
#October 20, 2026
#DESCRIPTION: Sort and output the values of a list of names/strings given by the user

names = []
name = ""
while name != "_DONE_":
    name = input('Enter a name (enter "_DONE_" to end): ')
    names.append(name)
names.remove("_DONE_")

print()
print("ORIGINAL -",names)
names.sort()
print("SORTED -",names)
names.reverse()
print("REVERSED -",names)