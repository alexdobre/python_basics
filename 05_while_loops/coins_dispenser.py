# Please write a method that will be part of a coin dispenser machine.
# This method takes as input two parameters: the amont of money given by the customer and the amout of money necessary for the products purchased.
# The method needs to calulate, print out and return the appropriate change in british coins. The change is in coins only, no notes. The change must contain the minimum number of coins possible.
# For example 5 GBP given, 2.30 GBP purchase would be a change of:
# 1 X 2 GBP coin
# 1 X 50 p coin
# 1 X 20 p coin.


COIN_VALUES = [200, 100, 50, 20, 10, 5, 2, 1]


def produce_change(total_money: int, product_price: int) -> list[int]:
    change = []

    # calculate the total amount of change that needs to be produced and store it in a variable

    # while the change is not yet 0
        # take the largest coin and see if it can be returned
        # if the coin can be returned add it to the change list and substract it's value from the total amount of change
        # if the coin cannot be returned because it's value is higher than the change pick up the next lergest coin

    return change


def produce_change_test():
    assert produce_change(500, 230) == [200, 50, 20]
    assert produce_change(200, 1) == [100, 50, 20, 20, 5, 2, 2]
    assert produce_change(2, 1) == [1]
    assert produce_change(500, 30) == [200, 200, 50, 20]


if __name__ == '__main__':
    produce_change_test()
