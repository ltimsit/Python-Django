import Hotbeverage
import random

class CoffeeMachine:
    def __init__(self):
        pass

    class EmptyCup(HotBeverage):
        self.name = "Empty cup"
        self.price  = 0.90
        self.description = "An empty cup?! Gimme my money back"
        def __init__(self):
            super().__init__()

    class BrokenMachineException(Exception):
        def __init__(self):
            self.description = "This coffe machine as to be repared"
            super().__init__(description)

    def repair(self):
        pass

    def serve(self, beverage):
        rand = random.randint(0, 1)
        if rand == 1:
            return beverage()
        else:
            return EmptyCup()

        
