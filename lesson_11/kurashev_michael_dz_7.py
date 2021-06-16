class Complex:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        if isinstance(other, Complex):
            return self.x + other.x
        else:
            return self.x + other

    def __mul__(self, other):
        if isinstance(other, Complex):
            return self.x * other.x
        else:
            return self.x * other


a = Complex(2)
b = Complex(4)
print(b + a)