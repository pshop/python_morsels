from math import pi, pow

class Circle():
    def __init__(self, radius=1):
        self.__radius = radius

    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError('Radius cannot be negative')
        self.__radius = radius

    @property
    def diameter(self):
        return self.__radius * 2

    @diameter.setter
    def diameter(self, diameter):
        if diameter < 0:
            raise ValueError('Radius cannot be negative')
        self.__radius = diameter/2

    @property
    def area(self):
        return pi*pow(self.radius, 2)

    def __str__(self):
        return f'Circle({self.__radius})'

    def __repr__(self):
        return f'Circle({self.__radius})'


if __name__ == '__main__':

    circle = Circle(2)
    circle.radius = 10
    circle.diameter = 20
