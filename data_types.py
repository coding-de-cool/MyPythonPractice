print('111111')

'''
number, string
example of tuple, list & dictionary
'''

tup = (1, 2, 3, 4) # Immutable data types
print(tup)

list = [3, 4, 5, 6, 7] # Mutable data types
list.append(8)
print(list)
list.insert(-1, 9)
print(list)
list.insert(-1, -8)
print(list)
list.insert(100, 10)
print(list)

dict1 = {'one': 1, 'two': 2}
print(dict1)

dict2 = dict([('one', 1), ('two', 2)])
print(dict2)

dict3 = dict(one = 1, two = 2)
print(dict3['two'])
print(dict3.get('there', 'No Matches')) #if key 'there' is not found, returns No Matches