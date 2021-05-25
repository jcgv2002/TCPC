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

# ------------------------------------------------------------
# Coding Exercise 10
# We have a class called Club, and it is initialized like this (no need to change):
class Club:
    def __init__(self, name):
        self.name = name
        self.players = []

    # define a method that allows us to access the i-th player in the club directly via indexing.
    # for example, if some_club is an object of Club class,
    # we can access the i-th player in some_club like this (you may assume i is always valid):
    # some_club[i]
    
    def __getitem__(self, i):
        return self.players[i]

    # define a method that returns a string representation of this object,
    # which can be used to recreate this object.
    # The return value should be in such format (beware of the spacing):
    # Club {club_name}: {list_of_players}
    # the club_name and list_of_players should be replaced by the according value of current object
    
    def __repr__(self):
        return f"Club {self.name}: {self.players}"


    # define a method that returns a readable string representation of this object for the user.
    # The return value should be in such format (beware of the spacing):
    # Club {club_name} with {count_of_players} players
    # the club_name and count_of_players should be replaced by the according value of current object
    def __str__(self):
        return f"Club {self.name} with {len(self.players)} players"

