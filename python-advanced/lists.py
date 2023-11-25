# Lists in Python - Advanced Python 01 - Programming Tutorial
# https://www.youtube.com/watch?v=QLTdOEn79Rc&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2

my_list = ['banana', 'cherry', 'apple']

my_list.reverse()
print('reverse() ->', my_list)

my_list.append('lemon')

my_list.insert(1, 'blueberry')

item_removed = my_list.pop()

print('Item removido ->', item_removed)

item_removed = my_list.remove('cherry')

[print(i) for i in my_list]

list_numbers = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, -1, -2, -3, -4, -5, -6, -7, -8, -9, -10]

list_numbers.sort()
print('sort() ->', list_numbers)

ordened_numbers = sorted(list_numbers)
print('sorted() ->', ordened_numbers)

print(ordened_numbers[14] * 5)

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(my_list[4:-4])
print(my_list[::-3])

original_list = ['banana', 'cherry', 'apple']

copy_list = original_list.copy()
print(copy_list)

list_numbers = [1, 2, 3, 4, 5]

print([i * i for i in list_numbers])
