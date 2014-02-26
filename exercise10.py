__author__ = 'kristof'

class Person(object):
    def __init__(self, name, location):
        self.name = name
        self.goto(location)
    def goto(self, location):
        self.location = location

class RestrictedPerson(Person):
    restricted_locations = ['Waardamme', 'Brugge', 'Ieper']
    def __isallowed(self, location):
        if location in self.restricted_locations:
            raise Exception('Location {0} is not allowed'.format(location))
    def goto(self, location):
        self.__isallowed(location)
        super(RestrictedPerson, self).goto(location)

els = Person('Els', 'Waardamme')
print(els.location)

els = RestrictedPerson('Els', 'Waardamme')
print(els.location)

kristof = RestrictedPerson('Kristof', 'Oostkamp')
print(kristof.location)
kristof.goto('Gent')
print(kristof.location)
kristof.goto('Brugge')
print(kristof.location)