import math


class Vector:
    def __init__(self, x: float, y: float):
        self.x = x
        self.y = y

    def __radd__(self, other):
        if isinstance(other, float) or isinstance(other, int):
            return Vector(self.x + other, self.y + other)
        else:
            raise TypeError("Unsupported operand type. Expected float or int.")


    def __add__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x + other.x, self.y + other.y)

        return Vector(self.x + other, self.y + other)

    def __sub__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x - other.x, self.y - other.y)

        return Vector(self.x - other, self.y - other)

    def __mul__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x * other.x, self.y * other.y)

        return Vector(self.x * other, self.y * other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, self.__class__):
            return Vector(self.x / other.x, self.y / other.y)

        return Vector(self.x / other, self.y / other)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.x == other.x and self.y == other.y
        return self.x == other and self.y == other

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def make_int_tuple(self):
        return int(self.x), int(self.y)

    def set(self, vec):
        self.x = vec.x
        self.y = vec.y


    def dot(vec1, vec2):
        return vec1.x * vec2.x + vec1.y * vec2.y


    def angle_between(vec1, vec2):
        return math.acos(Vector.dot(vec1, vec2))


    def length_sqr(vec):
        return vec.x ** 2 + vec.y ** 2


    def dist_sqr(vec1, vec2):
        return Vector.length_sqr(vec1 - vec2)


    def length(vec):
        return math.sqrt(Vector.length_sqr(vec))


    def dist(vec1, vec2):
        return Vector.length(vec1 - vec2)


    def normalize(vec):
        vec_length = Vector.length(vec)

        if vec_length < 0.00001:
            return Vector(0, 1)

        return Vector(vec.x / vec_length, vec.y / vec_length)
    
    def arrToVec(x):
        return Vector(x[0], x[1])


    def copy(vec):
        return Vector(vec.x, vec.y)

    def __repr__(self):  
        return f"({self.x}, {self.y})"
