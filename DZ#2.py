from abc import ABC, abstractmethod

class Abstract(ABC):
    @abstractmethod
    def fab(self):
        pass

class Coat(Abstract):
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    def fab(self):
        return self.__size / 6.5 + 0.5


class Suit(Abstract):
    def __init__(self, height):
        self.__height = height

    @property
    def height(self):
        return self.__height

    def fab(self):
        return 2 * self.__height + 0.3


coat = Coat(170)
print(coat.fab())
suit = Suit(190)
print(suit.fab())
