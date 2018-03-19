# Functions in Python

print('Hello')


def my_func():
    print('My function')


my_func()


# Function with argument
def with_arg(mobile, age = None):
    if age is None:
        print('He is not allowed in party')
    else:
        print(f"My mobile number is {mobile} and age is {age}")

with_arg(980788543)
with_arg(980787878, 24)


# Function with multiple values in single argument
def with_mul_value(one, two, *args):
    print(f"The value are {one}, {two}, {args}")


with_mul_value(1, 2, 3, 4, 'nitin', 2+3)

# Keyword argument

def with_kwarg(one, two, three, *args, **kwargs):
    print(f"The values are {one}, {two}, {three}, {args}, {kwargs}, {kwargs['day_1'], kwargs['day_2']}")

with_kwarg(1, 2, 3, 4, 5, day_1 = 'Monday', day_2 = 'Tuesday')


# Return in function

def return_factorial(number):
    if number is 0:
        return 1
    else:
        return number * return_factorial(number - 1)

print(return_factorial(5))