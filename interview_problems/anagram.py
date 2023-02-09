#   You have a dictionary of words held in a data structure.

#   Write an algorithm that will sort the dictionary such that all anagrams appear next to each other in the resulting list.

#   We are looking for the simplest solution to this problem.

#   For example,

#   [ Act, Bug, Cat, Dog, Fish, God ]

#   Becomes:

#   [ Act, Cat, Bug, Dog, God, Fish ]

def main():
    result()


def result():
    input = ['Act', 'Bug', 'Cat', 'Dog', 'Fish', 'God']

    print("The given list is: ", input)

    solution(input)


def solution(input_list):
    # Add your solution here

    output_list = []

    print("The sorted list is: ", output_list)


if __name__ == "__main__":
    main()