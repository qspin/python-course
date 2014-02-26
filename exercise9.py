__author__ = 'kristof'

class Person(object):
    def __init__(self, name, location):
        self.name = name
        self.location = location
    def goto(self, location):
        self.location = location

kristof = Person('kristof', 'Oostkamp')
print(kristof.location)
kristof.goto('Gent')
print(kristof.location)

persons = [Person(name, location) for name, location in
           zip(('kristof', 'peter', 'andy', 'gido'), ('Gent', 'Brussel', 'Beernem', 'Oostkamp'))]
print(' '.join(map(lambda x: str("{0} {1}".format(x.name, x.location)), persons)))