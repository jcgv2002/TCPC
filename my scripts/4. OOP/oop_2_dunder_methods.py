class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)
    
    def __getitem__(self, index):
        return self.cars[index]

    def __repr__(self) -> str:  # Generates a description oriented for the programmer
        return f"<Garage {self.cars}>"
    
    def __str__(self) -> str:   # Generates a description oriented for the user
        return f"Garage with {len(self)} cars" 


ford = Garage()
ford.cars.append('Fiesta')
ford.cars.append('Focus')

print(ford.cars)

print(len(ford))

# Having the dunder method __len__, we can apply the len() function to class object (ford)
print(ford[0])  # Garage.__getitem__(ford,0)

# Having the dunder method __getitem__, we can iterate over the class object (ford)
for car in ford:
    print(car)

# Having the dunder method __str__, we can use print() to get some information about the class object (ford)
print(ford)

