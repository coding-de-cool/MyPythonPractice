# Read & Write operation of file
file = open('file_example_1.txt')
for text in file:
    print(text, end='')

# Create a new file from existing file

newFile = open('file_example_1.txt')
outputFile = open('MyNewFile.txt', 'w')

for text in newFile:
    print(text, file = outputFile, end='')

print('\n txt file created')
# dealing with binary file

buff = 130000

newBinaryFile = open('py_tutorial.jpg', 'rb')
outputBinaryFile = open('new_py_tutorial.jpg', 'wb')

buffer = newBinaryFile.read(buff)
while len(buffer):
    outputBinaryFile.write(buffer)
    print(buffer)
    buffer  = newBinaryFile.read(buff)

print('\n jpg file created')