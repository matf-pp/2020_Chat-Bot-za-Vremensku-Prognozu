from typing import Union, List

class Test:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
t1 = [Test(1,2), Test(2,3), Test(3,4), Test(4,5)]

print(isinstance (t1, List) )