# Object in Python

from class_demo import Calculator

calc1 = Calculator()
calc1.mul(30, 10)
print(f"type of calc1 is {type(calc1)}")

calc2 = Calculator()
calc2.sum(10, 15)
print(f"type of calc2 is {type(calc2)}")

calc4 = Calculator()
calc4.sum(5, 5)
calc4.mul(3, ' test')
print(f"type of calc4 is {type(calc4)}")