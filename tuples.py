# Tuples in Python - Advanced Python 02 - Programming Tutorial
# https://www.youtube.com/watch?v=Kes8YRV73Io&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=2

import sys
import timeit

my_tuple = ('Max',)
print(type(my_tuple))

my_tuple = tuple(['Max', 28, 'Boston'])
print(my_tuple)

[print('item ->', i) if 'Max' in my_tuple else None for i in my_tuple]

my_tuple = ('a', 'b', 'c', 'c', 'd', 'e', 'f', 'g')
print(my_tuple.count('c'))
print(my_tuple.index('b'))

my_list = list(my_tuple)
print(my_list)
my_tuple = tuple(my_list)
print(my_tuple[:-1])

print(my_tuple[::2])
print(my_tuple[::-2])

my_tuple = 'Max', 28, 'Boston'
name, age, city = my_tuple
print(name)
print(age)
print(city)

my_tuple = (0, 1, 2, 3, 4)
i1, i2, *i3 = my_tuple
print(i1)
print(i2)
print(i3)

my_list = [0, 1, 2, 'hello', True]
my_tuple = (0, 1, 2, 'hello', True)
print('list() ->', sys.getsizeof(my_list), 'bytes')
print('tuple() ->', sys.getsizeof(my_tuple), 'bytes')

print('list() ->', timeit.timeit(stmt='[0, 1, 2, 3, 4, 5]', number=1000800))
print('tuple() ->', timeit.timeit(stmt='(0, 1, 2, 3, 4, 5)', number=1000800))
