# Dictionaries in Python - Advanced Python 03 - Programming Tutorial
# https://www.youtube.com/watch?v=LTXnQdrwyrw&list=PLqnslRFeH2UqLwzS0AwKDKLrpYBKzLBy2&index=3

my_dict = {
    'name': 'Max',
    'age': 28, 
    'city': 'New York'
}
print(my_dict)

my_dict2 = dict(name='Mary', age=27, city='Boston')
print(my_dict2)

print(my_dict['name'])

my_dict['email'] = 'max@gmail.com'
print(my_dict)

my_dict.update({'name': 'Paul'})
print(my_dict)

del my_dict['email']
print(my_dict)

my_dict.pop('age')
print(my_dict)

my_dict.popitem()
print(my_dict)

print(my_dict['name']) if 'name' in my_dict else None

print(my_dict['name']) if 'Paul' in my_dict.values() else None

my_dict = {
    'name': 'Max',
    'age': 28, 
    'city': 'New York'
}
my_dict['email'] = 'max@gmail.com'
[print(key) for key in my_dict.keys()]
[print(value) for value in my_dict.values()]

my_dict2 = dict(name='Mary', age=27, city='Boston', email='mary@gmail.com')
my_dict.update(my_dict2)
print(my_dict)

my_dict = {3: 9, 6: 36, 9: 81}
print(my_dict[6])

my_tuple = (8, 7)
my_dict = {my_tuple: 15}
print(my_dict)