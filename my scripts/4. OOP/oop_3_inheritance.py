class Student:
    def __init__(self, name, school) -> None:
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)


""" class WorkingStudent:
    def __init__(self, name, school, salary) -> None:
        self.name = name
        self.school = school
        self.marks = [] 
        self.salary = salary
    
    def average(self):
        return sum(self.marks) / len(self.marks)
        
    def weekly_salary(self):
        return self.salary * 37.5  # Regular weekly working hours in UK are 37.5 """ 

# Apply inheritance (WorkingStudent class is just an extension of the Student class)
class WorkingStudent(Student):
    def __init__(self, name, school, salary) -> None:
        super().__init__(name, school)
        self.salary = salary

    def weekly_salary(self):
        return self.salary * 37.5  # Regular weekly working hours in UK are 37.5


rolf = WorkingStudent('Rolf', 'MIT', 15.5)
print(rolf.salary)

rolf.marks.append(57)
rolf.marks.append(99)

print(rolf.average())

print(rolf.weekly_salary())

