#Extending

#we can extend functionality of a class by adding more methods in the child class
#Thereby creating a more specialised class

# Let's see an example
class Person:
    """base classs"""
    pass

class Student(Person):
    """Extending the base class and adding study() method"""
    def study(self): #define a new method in the child class
        print(f"Study Hard!")
        
s1 = Student() #Create an instance of the Student class
s1.study() #Study Hard!