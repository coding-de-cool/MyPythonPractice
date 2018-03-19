# Example of class in python


class Calculator:
    def sum(self, num1=None, num2=None):
        print(type(self))
        print(f"The sum of {num1} & {num2} is:", num1 + num2)

    def mul(self, num1=None, num2=None):
        print(f"The multiplication of {num1} & {num2} is", num1 * num2)


calc = Calculator()
calc.mul(2, 4)
calc.sum(4, 10)