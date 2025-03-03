#CHALLENGE
"""School Management System:

1. Create a base class Person with attributes name and age.
2. Derive Student and Teacher classes.
3. Add methods for student grade calculation."""

#1. Create a base class Person with attributes name and age.
class Person:
    def  __init__(self,name,age):
        self.name = name
        self.age = age
#2. Derive Student and Teacher classes.
#3. Add methods for student grade calculation and teacher salary calculation.

class Student(Person):
    def __init__(self,name,age,*marks):
        super().__init__(name,age)
        self.marks = marks
        
    def calculate_grade(self):
        total = sum(self.marks)
        grade = None
        if total > 90:
            grade = 'A+'
        elif total > 80: 
            grade = 'A'
        elif total > 70: 
            grade = 'B+'
        elif total > 60: 
            grade = 'B'
        elif total > 50: 
            grade = 'C'
        else:
            grade = 'D'
        return f"The grade of the student {self.name} is {grade}"
    
student1 = Student("Johny",14,00,10,30,4,5)
print(student1.calculate_grade())

