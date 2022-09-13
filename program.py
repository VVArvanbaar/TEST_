"""Testbestand voor python"""



class Person:
    """ Docstring """
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

def testcase():
    """Testfunctie"""
    print("test")

p1 = Person("Rik", 18)
print(p1.age)
print(testcase.__doc__)
