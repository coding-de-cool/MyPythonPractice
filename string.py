lower = 'i am a string'
upper = 'I AM A STRING'
cash = 20

print(lower.upper())
print(upper.lower())
print(upper.capitalize())
newString = upper.swapcase()
print('new string is', newString)
print('Id of old string is {}'.format(id(upper)), 'and Id of New string is {}'.format(id(newString)))
print('my name is khan'.upper())
print('I got {}$ cash'.format(cash))
print(lower.find('am'))
print(lower.replace('am', 'will be'))

input_1 = '   I am input      '
input_2 = '   I am input 2'
input_3 = 'I am input 3    '
input_4 = 'I am input 4'

print(input_1.strip())
print(input_2.lstrip()) # Remove leading spaces
print(input_3.rstrip()) # Remove trailing spaces
print(input_4.split())

alphaNum = 'Password123'
alpha = 'passsword'
num = '1233333'
print(alphaNum.isalnum())
print(alpha.isalnum())
print(num.isdigit())

# formating of string in python 3.6

cash = 50
first_way = f'I have a {cash}$ cash.'
print(first_way)
second_way = 'I have a {}$ cash'.format(cash)
print(second_way)

str = 'top ten programming language in 2016'
splitted_str = str.split()
print(splitted_str)

for i in splitted_str:
    print(i, end=' ')

print('\n')
url = '-'.join(splitted_str)
print(url, '.html')