# Delegating means calling a method specifically in the ancestry hierarchy (or a sibling class)
# Often when overriding methods, we need to delegate back to the parent class

#The most common example is the __ini__ method
#let's look at a naive way of overriding the __ini__ method

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
class Student(Person):
    def __init__(self,name,age,major): #Here we are overriding the __init__ method. 
        self.name = name
        self.age = age
        self.major = major
        
#This approach cannot be followed when we have lots of arguments in the init method.
#We should be able to mimic the entire arguments of the init method from the person class
#ie; we should explicitly call a method from the parent class

class Student(Person):
    def __init__(self,name,age,major):
        super().__init__(name,age) #super() function will basically allow us to get a referenc back to the parent.
        self.major = major
s1 = Student('John',30,'science')
print(s1.name)
print(s1.age)
print(s1.major)

#Let's see an overriding scenario
class Person:
    """A parent class"""
    def do_work(self):
        """A simple function in th parent class"""
        return "The person is working"
        
class Student(Person):
    """A inheriting class"""
    def do_work(self):
        """Overriding the function from the parent class"""
        return "The student is studying"
    
    def person_do_work(self):
        """An additional function to refer the do_work function from the parent class"""
        return super().do_work()
    
s1 = Student()
print(s1.do_work()) #The student is studying
print(s1.person_do_work()) #The person is working

# Hence using this method we can call even the functions that are overridden.