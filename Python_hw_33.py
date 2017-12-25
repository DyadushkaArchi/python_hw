class Godzilla:

    def __init__(self, stomach_volume):
        self.stomach_volume = stomach_volume
        self.free_stomach_space = stomach_volume

    def eat(self, weight):
        self.free_stomach_space = self.stomach_volume - weight
        return self.free_stomach_space

    def is_full(self):
        return self.free_stomach_space < (self.stomach_volume // 10)

#(main.py)
#from Python_hw_33 import Godzilla
#g = Godzilla(100)
#print(g.is_full())
#g.eat(93)
#print(g.is_full())