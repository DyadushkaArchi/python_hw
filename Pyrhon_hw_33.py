class Godzilla:

    stomach_volume = 100000

    def eat(self, weight):
        self.stomach_volume -= weight
        return self.stomach_volume

    def is_full(self):
        if not self.stomach_volume < 10000:
            return False
        else:
            return True

