import random
from reference_data import *


def generate_random_command() -> str:
    zero_one_or_two: int = random.randint(0, 2)
    return [ROCK, PAPER, SCISSORS][zero_one_or_two]


def test():
    for i in range(1000):
        random_command: str = generate_random_command()
        assert random_command in [ROCK, PAPER, SCISSORS]
    print('Tests passed')


test()
