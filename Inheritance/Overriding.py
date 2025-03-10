#Overriding

"""When we inherit from a class, we inherit its attributes including its callables."""
#We can then choose to redefine an existing callable in the subclass. THIS IS CALLED "OVERRIDING".

#Let's see an example
class Person:
    def say_hello(): # Function defined in the parent class
        print("Hello there!")
        
    def say_bye():
        print("Bye!")
        
class Student(Person):  #Student class inherits from the Person class
    def say_hello(): #Overriding the function in the child class
        print("Hello. Good Morning")
        
        
Student.say_hello() #Hello. Good Morning
Student.say_bye() #Bye!

#When we create any class we can override any method defined in the parent class, including the ones inherited by parent.
#including the one defined in the object class

#let's see this
class Person:
    def __init__(self,name): #Overriding the __init__ method defined in the object class
        self.name = name
        print(f"The {self.__class__.__name__} is {self.name}")

p1 = Person("Akash") #The name is Akash

class Student(Person): #Student class inherits the overridden __init__ method from the Person class
    pass

s1 = Student("Hari") #The name is Hari    

#HOW TO GET THE NAME OF THE CLASS AS A "STRING" ? 
print(s1.__class__.__name__) #Use __name__ on a class object
print(type(s1).__name__)

#NOW LETS SEE ANOTHER CASE
class Person:
    """A person having 4 functions : eat,sleep,work and routine"""
    def eat(self):
        print(f"Person eats")
        
    def work(self):
        print(f"Person works")
    
    def sleep(self):
        print(f"Person sleeps")
        
    def routine(self):
        self.eat()
        self.work()
        self.sleep()
        
p1 = Person()
p1.routine()

class Student(Person):
    def work(self):
        print(f"Student studies")

s1 = Student()
s1.routine() #The routine function will be callled from the person class, BUT BOUND TO s1.