# Example of class in python


class Calculator:

    # Constructor in Python

    def __init__(self):
        self._default_sum = 0
        self._default_mul = 1

    def sum(self, num1=None, num2=None):
        if (num1 is None) and (num2 is None):
            print('Default sum is', self._default_sum)
        else:
            print(f"The sum of {num1} & {num2} is:", num1 + num2)

    def mul(self, num1=None, num2=None):
        if num1 is None and num2 is None:
            print('Default multplication is.', self._default_mul)
        else:
            print(f"The multiplication of {num1} & {num2} is", num1 * num2)


calc = Calculator()
calc.mul(2, 4)
calc.sum(4, 10)

print('When no argument is passed addition.')
calc.sum()

print('When no argument is passed for multiplication.')
calc.mul()