# Handling IO exception in python script

print('Hi there!')

try:

    file = open('file_example.txt')
    for text in file:
        print(text, end='')
except IOError as msg:
    print('Sorry! File not found', msg)

print('\n print me regardless of exception')