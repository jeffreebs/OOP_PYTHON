class Head:
    def __init__(self):
        self.eye= 2
        self.nose= 1
        self.mouth = 1
        self.ear = 2
        



class Torso:
    def __init__(self):
        pass
    


class Arm:
    def __init__(self,side):
        self.side = side
        pass
    


class Hand:
    def __init__(self):
        pass


class Leg:
    def __init__(self,side):
        self.side = side
        pass
    


class Feet:
    def __init__(self):
        pass
    


class Human:
    def __init__(self,name):
        self.name = name
        self.Head = Head()
        self.Torso = Torso()
        self.right_arm = Arm("right")
        self.left_arm = Arm("left")
        self.Hand = Hand()
        self.right_leg = Leg("right")
        self.left_leg = Leg("left")
        self.Feet = Feet()


    def describe(self):
        print(f"Hello my name is {person.name} and i have  1 {self.left_arm.side} arm,  and 1 one more in {self.right_arm.side} side")
        print (f"To, i have one {self.left_leg.side} leg  and another one in {self.right_leg.side} side ")


    

    


person = Human("Jeff")

person.describe()

#This is another way to print but is a "poor practice"

# print (f"Hello my name is{person.name} has one",  person.right_Arm.side,"arm")
# print (f"Hello my {person.name} has one",person.left_Arm.side,"arm")
# print (f"{person.name} has one",person.right_Leg.side,"leg")
# print (f"{person.name} has one",person.left_Leg.side,"leg")