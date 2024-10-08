# adding to end of list
# removing from end of list
# adding to front of list
# removing from front of list

# [True, False, "String", 1234, 12.34, [], {}, ()]

# list are your arrays
persons = ["John", "Joe", "James", "Jared"]

# list can be iterated
# for name in persons:
#   print(name)

# access list by index
# persons[0] == "John"

# get length of list

# if len(persons) == 4:
#   print("There are 4 names in this list")

# see if element is included
# if "John" in persons:
#   print("John is in the list")

# add to end of list
persons.append("Jay")

# add to front of list, inserts at given index
persons.insert(0, "Joel")

# remove from end of list
persons.pop()

# remove from front of list
persons.pop(0)
del persons[0]

# remove by element
persons.remove("James")

# update elements
persons[1] = "Joel"
print(persons)