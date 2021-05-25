my_student = {
    'name': 'Rolf Smith',
    'grades': [70, 88, 90, 99],
    'average': None  #  Something here!!! --> IMPOSSIBE!!! ---> CLASS
}


def average_grade(student):
    return sum(student['grades']) / len(student['grades'])

# -----------------------------------------------------------------------------------------
#   - OOP motivation
class Student:
    def __init__(self, new_name, new_grades):   # Class Properties  
        self.name = new_name
        self.grades = new_grades

    
    def average(self):  # A Class Method
        return sum(self.grades) / len(self.grades)

student_one = Student('Rolf Smith', [70, 88, 90, 99])
student_two = Student('Jose', [50, 60, 99, 100])

print(student_one.name)
print(student_two.grades)

print(student_one.average())    # print(Student.average(student_one))
print(student_two.average())

# ------------------------------------------------------------------------------
'''
So that's what a class is, and that's what an object is.
A way to store some data (properties that define the object)
and store some actions (methods that handle the object) that relate to it.

That allows us to encapsulate and hold all relevant functionality
in the same structure, as opposed to having it split over two separate
structures like we did up here (a dictionary to store data and
a function to manage them).
'''
# -------------------------------------------------------------------------------
'''
For Built-in functions list:
https://docs.python.org/3.7/library/functions.html
'''

