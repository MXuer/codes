from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

class Cal:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def div(self):
        return self.a / self.b

    def mul(self):
        return self.a * self.b

    def mod(self):
        return self.a % self.b


if __name__=="__main__":
    c  = Cal(1,2)
    print(c.add())