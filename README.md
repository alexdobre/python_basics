# Python basics course

Please see the respective lessons folders.

# Python syntax cheat sheet


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