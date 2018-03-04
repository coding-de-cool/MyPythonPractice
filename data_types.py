
'''
number, string(they are immutable data types)
example of tuple, list & dictionary
'''

# let's talk about Tuples(Fixed, means immutable)

tup = 'a', 'b', 'c', 'd'
print(tup)

is_a_tup = (1)
print(type(is_a_tup))
single_tup = (1,)
print(type(single_tup))
tup = tuple(range(20, 40))
print(tup)

print(2 in tup)
if 21 in tup:
    print('21 is in tup')
else:
    print('21 is not in tup')

tup = (1, 2, 3, 4) # Immutable data types
print(tup)

# let's talk about List(variable, mutable)

print('\n')
listo = list(range(20, 30))
listo.append(200)
print(listo)
listo.remove(23)
print(listo)

list = [3, 4, 5, 6, 7] # Mutable data types
list.append(8)
print(list)
list.insert(-1, 9)
print(list)
list.insert(-1, -8)
print(list)
list.insert(100, 10)
print(list)

# let's talk about Dictionary

dict1 = {'one': 1, 'two': 2}
print(dict1)

dict2 = dict([('one', 1), ('two', 2)])
print(dict2)

dict3 = dict(one = 1, two = 2)
print(dict3['two'])
print(dict3.get('there', 'No Matches')) #if key 'there' is not found, returns No Matches