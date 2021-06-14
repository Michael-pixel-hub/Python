from abc import ABC, abstractmethod

class Clothes(ABC): #одежда
    @abstractmethod
    def colculate(self):
        pass


class Coat(Clothes):
    def __init__(self, coat_size):
        self.coat_size = coat_size
    @property
    def colculate(self):
        return self.coat_size/6.5+0.5


class Suit(Clothes):
    def __init__(self, suit_size):
        self.suit_size = suit_size
    @property
    def colculate(self):
        return 2*self.suit_size+0.3

a = Coat(12)
b = Suit(22)
print(a.colculate+b.colculate)