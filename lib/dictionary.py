
person = {
  "name": "Joe",
  "age": 32
}

# adding to a dictionary
person["job"] = "Programmer"

# update a dictionary key / value
person["job"] = "Python Programmer"

def greeting(name):
  def inner_func():
    print(f"{name} says hello!")

  return inner_func

person["greet"] = greeting(person["name"])

# remove from a dictionary
del person["job"]

# looping, .items gives us tuples of key / values
# for k in person.items():
#   print(f'This person\'s {k[0]} is {k[1]}')

# print(person.items())

person["greet"]()