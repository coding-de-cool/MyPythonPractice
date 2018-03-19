# Square List without generator


def square_list(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result


my_nums = square_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(my_nums)


# Using yield
def square_list_2(nums):
    for i in nums:
        yield i*i


my_nums = square_list_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(my_nums) #otuput <generator object square_list_2 at 0x7faa5aa89ba0>
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))
print(next(my_nums))


# List comprehension

my_nums = [x * x for x in [1, 2, 3, 4, 5, 6]]
print(my_nums)