class Godzilla:

    def __init__(self, stomach_volume):
        self.stomach_volume = stomach_volume

    def eat(self, weight):
        self.current_stomach_volume = self.stomach_volume - weight
        return self.current_stomach_volume

    def is_full(self):
        if not self.current_stomach_volume < self.stomach_volume // 10:
            return False
        else:
            return True


#(main.py)
#from Python_hw_33 import Godzilla

#Godzilla.__init__(Godzilla, 100)
#Godzilla.eat(Godzilla, 93)
#print(Godzilla.is_full(Godzilla))