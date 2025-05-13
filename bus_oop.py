class Bus:
    def __init__(self,max_passenger):
        self.max_passenger = max_passenger
        self.passengers = []
        
    

    def add_passenger(self,person):
        if len(self.passengers) < self.max_passenger:
            self.passengers.append(person)
            print (f"{person.name} up to the bus")
        else:
            print(f"The bus is already full, any body cant up, so sorry for {person.name}  ")
class Person:
    def __init__(self, name):
        self.name=name
        pass


my_bus=Bus(3)
one=Person("Luis")
two=Person("Carlos")
three=Person("Horacio")
four=Person("Pedro")

my_bus.add_passenger(one)
my_bus.add_passenger(two)
my_bus.add_passenger(three)
my_bus.add_passenger(four)

