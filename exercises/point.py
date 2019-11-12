class Point():
    def __init__(self,x ,y ,z ):
        self.x = x
        self.y = y
        self.z = z


    def __str__(self):
        return f"Point(x={self.x}, y={self.y}, z={self.z})"

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        if self.x != other.x or self.y != other.y or self.z != other.z :
            return False
        return True

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if type(other) == int:
            return Point(self.x * other, self.y * other, self.z * other)

    __rmul__ = __mul__

    def __getitem__(self, item):
        values = [self.x, self.y, self.z]
        return values[item]

if __name__ == '__main__':
    pass