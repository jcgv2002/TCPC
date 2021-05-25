# The @property method decorator
''' Applicable to methods that:
1.- Only take the self argument
2.- Do not perform an action but just calculating a value out of a property value 
    (already defined in the __init__) '''


class WorkingStudent():
    def __init__(self, name, school, salary) -> None:
        self.name = name
        self.school = school
        self.marks = []
        self.salary = salary

    def average(self):
        return sum(self.marks) / len(self.marks)

    @property   # Property decorating the weekly_salary method
    def weekly_salary(self):
        return self.salary * 37.5  # Regular weekly working hours in UK are 37.5


rolf = WorkingStudent('Rolf', 'MIT', 15.5)

# the method weekly salary, once decorated with @property, 
# is accessed just like any other property
print(rolf.weekly_salary)   # instead of print(rolf.weekly_salary())
print()


# Sintax for @classmethod 
class Foo:
    @classmethod
    def hi(cls):  # cls for convention (representing the class)
        print(cls.__name__)  # takes the name of the class

my_object = Foo()
my_object.hi()


# Examples for  @classmethod 
class FixedFloat:
    def __init__(self, amount):
        self.amount = amount

    def __repr__(self) -> str:
        return f"<FixedFloat {self.amount:.2f}>"

    @classmethod
    def from_sum(cls, value1, value2):
        return cls(value1 + value2)
    

class Euro(FixedFloat):
    def __init__(self, amount):
        super().__init__(amount)
        self.symbol = '€'

    def __repr__(self) -> str:
        return f"<Euro {self.symbol}{self.amount:.2f}>"
    

number = FixedFloat.from_sum(19.575, 0.789) 
print(number)

money = Euro.from_sum(16.758, 9.999) # returns an Euro object while calling a FixedFloat method decorated with @classmethod 
print(money)

