

# find the biggest and the second biggest in the list
def main():
    some_list = [1, 2, 3, 4, 5, 6, 7, 87, 8, 9]
    biggest = 0
    second_biggest = 0
    for nr in some_list:
        if nr > biggest:
            second_biggest = biggest
            biggest = nr
        elif nr > second_biggest:
            second_biggest = nr
    print(f"Biggest: {biggest} - Second Biggest: {second_biggest}")


if __name__ == '__main__':
    main()
