# non ordered, changeable
# syntax for set {'James', 'Joe', 'Joel', 'Jared', 'Jay'}

persons = ["Joe", "Joel", "James", "Jared", "Jay"]

random_persons_set = set(persons)

persons = list(random_persons_set)

print(list(set(persons)))