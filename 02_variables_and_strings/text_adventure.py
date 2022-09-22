print('Hello adventurer what is your name?')
name = input()
health = 100
gold = 0  # add another variable to track something else
print(f'Hello, {name}! Let the adventure begin!')
print(f'Your health is now {health}')
print('You are at the entrance of a dark and smelly dungeon, you see three paths open to you.'
      ' One in front, one to the left and one to the right. What do you do?')
command = input()

if command == 'go forward':
    print('Oh no! You run into a spike trap! Wounded you stagger back to the entrance')
    health -= 10
    print(f'Your health is now {health}')
    print('What do you do?')

if command == 'go left':
    print('You find a room with an old iron chest in the corner. '
          'After some effort you are able to open the chest and find some gold inside')
    gold += 100
    print(f'Your gold in now {gold}')

if command == 'go right':
    print('I wonder what will happen here?')  # add something interesting that happens
