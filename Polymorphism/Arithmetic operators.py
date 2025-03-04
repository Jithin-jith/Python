class Person:
    def __init__(self,name):
        self._name = name
        self._place = 'Mumbai'
    pass

p = Person('John')
print(p._name)
print(p.__class__)
print(p.__class__.__name__)