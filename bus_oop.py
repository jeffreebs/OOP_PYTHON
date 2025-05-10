class Bus:
    def __init__(self,max_passenger):
        self.max_passenger = max_passenger
        self.passengers = []
        
    

    def add_passenger(self,person):
        if len(self.passengers) < self.max_passenger:
            self.passengers.append(person)
            print ("Somebody up to the bus")
        else:
            print("The bus is already full, any body cant up  ")
class Person:
    def __init__(self):
        pass


my_bus=Bus(3)
one=Person
two=Person
three=Person
four=Person

my_bus.add_passenger(one)
my_bus.add_passenger(two)
my_bus.add_passenger(three)
my_bus.add_passenger(four)

