from player_wins_rock_paper_scissors import player_wins_rock_paper_scissors
from generate_random_command import generate_random_command

print('Hello, let\'s play Rock paper scissors.\nPlease input rock, paper or scissors: ')
player_input = input()
computer_input = generate_random_command()

print(f'My fist, if I had one, would be in the shape of a {computer_input}')
result: str = player_wins_rock_paper_scissors(player_input, computer_input)

# turn this into an independent function - write it's unit tests
if result == 'win':
    print('You win!')
elif result == 'loss':
    print('I win :(')
else:
    print('It is a draw')

