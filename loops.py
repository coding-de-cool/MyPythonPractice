# while loop, for fibonacci sequence

print('while loop example')
first = 0
second = 1
print(first)
while second < 100:
    print(second, end=' ')
    first, second = second, first + second

# for each loop

print('\n for loop exampple')
value = 'Welcome to the python course'
for index, char in enumerate(value):
    print(index, char)

tup = ('apple', 'orange', 'banana', 'pineapple')
for i in tup:
    print(i)

my_dict = dict(maths = 98, physics = 75, chemistry = 68, english = 65)
for key in my_dict:
    print(my_dict[key])