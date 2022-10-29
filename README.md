# Python basics course

Please see the respective lessons folders.

# Python syntax cheat sheet
https://www.w3schools.com/python/default.asp

Good concise python cheat sheet: 
https://zerotomastery.io/cheatsheets/python-cheat-sheet/

## Variables and string manipulation
```python
name = 'Alex'
print(f'my name is {name}') # text formatting with variable interpolation
'a' + 'b' == 'ab' # add text together
'a-b'.replace('-','+') == 'a+b' 
'alex'.capitalize() == 'Alex'
# escape special characters within a text using \. \n for example is a new line
print('Hello, let\'s play Rock paper scissors\n Some text on the new line.')

# strings can be written with double quotes "" or single quotes '' pick one and stick with it
my_name = "Alex"
my_age = 100
# string interpolation with %s %d - less popular, use the {} syntax
print("Hello! My name is %s and I am %d years old" %(my_name, my_age))

# python primitive types are str, int, float, bool
# variable names begin with a lower case letter and words within the name are separated by underscores
this_is_a_variable = 'some text'
# types are optional in python 
this_is_another_variable: bool = True
```

## If statements
https://www.w3schools.com/python/python_conditions.asp

```python
# example if statement
command = 'go forward'
if command == 'go forward':
    print('Oh no! You run into a spike trap! Wounded you stagger back to the entrance')
elif command == 'go left':
    print('Something interesting')
else:
    print('I do not understand the command')
# function names must begin with a lower case letter and if made up of several words they must be separated by underscores

def this_is_a_function(function_parameter: float, another_parameter: int) -> str:
    # this is a function content, notice the indentation
    # a function may return something
    return 'something'
```

## Lists

https://www.w3schools.com/python/python_lists.asp

```python
# Python lists
cars = ["Ford", "Volvo", "BMW"]

# accessing arrays with index starting at 0
print(cars[0]) #Ford
print(cars[2]) #BMW

# modify array elements via index
cars[0] = "Toyota" # ["Toyota", "Volvo", "BMW"]

print(len(cars)) # length of array is 3

cars.append("Honda") # add to the list ["Toyota", "Volvo", "BMW", "Honda"]
cars.pop(1) # remove the second element in the list ["Toyota", "BMW", "Honda"]
cars.remove("Honda") # remove specific element in the list ["Toyota", "BMW"]
```

## For loops 
https://www.w3schools.com/python/python_for_loops.asp

```python
fruits = ['Apple', 'Pear', 'Banana']
for index, fruit in enumerate(fruits):
    print(index, fruit)

for x in fruits:
  print(x)

# loop through a string
for x in "banana":
  print(x)

# break out of a loop
for x in fruits:
  print(x)
  if x == "banana":
    break

# continue skips to the next loop
for x in fruits:
  if x == "banana":
    continue
  print(x)

for x in range(6):
  print(x) # outputs 0 to 5

for x in range(2, 6): # if given 2 parameters the first one is the start
  print(x) # outputs 2 to 5

for x in range(2, 12, 3): # the last parameter is the increment value, default 1
  print(x) # outputs 2, 5, 8, 11

for x in range(6):
  print(x)
else:
  print("Finally finished!") # else after a for loop does something when it is finished

 # you can nest loops 
adj = ["red", "big", "tasty"]
for x in adj:
  for y in fruits:
    print(x, y)

# the pass statement does nothing
for x in [0, 1, 2]:
  pass
```

## While Loops
https://www.w3schools.com/python/python_while_loops.asp

```python
i = 1
while i < 6:
    print(i)
    i += 1
  # can use continue and break keywords with while loops as well 
```
## Dictionaries

https://www.w3schools.com/python/python_dictionaries.asp

```python
# Define a dict
car = {
  'brand': 'Ford',
  'model': 'Mustang',
  'year': 1964
}
print(type(car)) # dict

# access a value
car['year'] # 1964
car.get('year') # 1964

# List keys
car.keys() # ['brand', 'model', 'year']
# List values
car.values() # ['Ford', 'Mustang', 1964]
# change or add a value
car['year'] = 1966
car.update({'year': 1966})
# remove a value
car.pop('year')
del car['model']
car.clear() # empties the dictionary
```

## Tuples
https://www.w3schools.com/python/python_tuples.asp

Tuples are ways to store multiple values into a variable. As opposed to lists, they are unchangeable.
```python
# tuples are declared using rounded brackets as opposed to square brackets for lists
fruits = ("apple", "banana", "cherry")
print(len(fruits)) # 3
print(fruits[0]) # apple

# you need the comma to declare a single value tuple
fruit = ("apple",)
print(type(fruit)) # tuple

# tuples can contain any data types
fruits = ("apple", "banana", "cherry")
numbers = (1, 5, 7, 9, 3)
booleans = (True, False, False)
combo = ("abc", 34, True, 40, "male")
```

# Pygame

https://www.pygame.org/wiki/about

