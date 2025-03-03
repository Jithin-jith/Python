#print function looks for the '__str__' method
#if no '__str__' method is defined then it will look for '__repr__' method

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
p = Person('Jack',30)
print("\n")
print("OUTPUTS BEFORE '__str__' METHOD")
print("\n")
print(f"Print method : {p}")
print(f"strinng method : {str(p)}") #basicall, both of these will be the same 
#In the above case a string method is not defined. Hence it is using the __repr__ method by default.

print(f"repr method : {repr(p)}") #This will be same as the str method

#Now lets define the '__str__' method
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return f"__str_method called on {self.name}"
        
p = Person('Jack',30)
print("\n")
print("OUTPUTS AFTER '__str__' METHOD")
print("\n")
print(f"Print method : {p}") #Now these two method will use the '__str__' method, since it is defined
print(f"strinng method : {str(p)}") #It will not use the '__repr__' method
print(f"repr method : {repr(p)}") # This will again use the default '__repr__' method
print("\n")
print('The person is {} and age is {}'.format(p.name,p.age))