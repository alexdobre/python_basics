#Andi Safta, Razvan Mitrita, Indres Bogdan-Andrei
import random
class OregonTrail:

    def __init__(self):
        self.player_name = input("What is your name? ")
        self.player_money = 200 + round(1800 * random.random())
        self.player_health = 100
        self.player_hunger = 0
        self.player_thirst = 0
        self.player_fatigue = 0
        self.player_distance_traveled = 0
        self.player_inventory = []
        self.goods = 0
        self.bullets = 5
        self.distance_travelled_goal = 6000
        self.game_in_progress = True
        self.free_play = False

    def start_game(self):
        print("Welcome, {}! You have ${} to spend on your journey.".format(self.player_name, self.player_money))
        print("You will be traveling on the Oregon Trail, a treacherous journey of over 6,000 miles.")
        print("You will need to manage your resources and make it to Oregon alive.")
        while self.game_in_progress:
            self.display_status()
            self.make_decision()
            self.update_status()
            self.check_for_end_game()

    def display_status(self):
        print("Health: {}".format(self.player_health))
        print("Hunger: {}".format(self.player_hunger))
        print("Thirst: {}".format(self.player_thirst))
        print("Fatigue: {}".format(self.player_fatigue))
        print("Distance Traveled: {} miles".format(self.player_distance_traveled))
        print("Money: {}".format(self.player_money))
        print("Inventory: {} food".format(self.goods))
        print("Bullets: {}".format(self.bullets))

    def make_decision(self):
        decision = input("What would you like to do? (travel, rest, hunt, trade, eat, drink water) ")
        if decision == "travel":
            self.player_distance_traveled += 6000
            self.player_hunger += 5
            self.player_thirst += 5
            self.player_fatigue += 5
        elif decision == "rest":
            self.player_hunger += 2
            self.player_thirst += 2
            self.set_fatigue(self.player_fatigue - 10)
        elif decision == "hunt":
            print("You have decided to hunt for food.")
            print("You have " + str(self.bullets) + " bullets.")
            print("What would you like to hunt?")
            print("1. Deer")
            print("2. Rabbit")
            print("3. Squirrel")
            choice = input()

            def hunt_deer():
                return random.randint(0, 10) > 3

            def hunt_rabbit():
                return random.randint(0, 10) > 5

            def hunt_squirrel():
                return random.randint(0, 10) > 7
            if choice == "1":
                if self.bullets >= 3:
                    success = hunt_deer()
                    if success:
                        print("You have successfully hunted a deer and gained 50 pounds of food.")
                        self.goods += 50
                        self.bullets -= 3
                    else:
                        print("You were unsuccessful in hunting the deer. You lost 3 bullets.")
                        self.bullets -= 3
                else:
                    print("You do not have enough bullets to hunt a deer.")
            elif choice == "2":
                if self.bullets >= 2:
                    success = hunt_rabbit()
                    if success:
                        print("You have successfully hunted a rabbit and gained 20 pounds of food.")
                        self.goods += 20
                        self.bullets -= 2
                    else:
                        print("You were unsuccessful in hunting the rabbit. You lost 1 bullet.")
                        self.bullets -= 2
                else:
                    print("You do not have enough bullets to hunt a rabbit.")
            elif choice == "3":
                if self.bullets >= 1:
                    success = hunt_squirrel()
                    if success:
                        print("You have successfully hunted a squirrel and gained 10 pounds of food.")
                        self.goods += 10
                        self.bullets -= 1
                    else:
                        print("You were unsuccessful in hunting the squirrel. You lost 1 bullet.")
                        self.bullets -= 1
                else:
                    print("You do not have enough bullets to hunt a squirrel.")
            else:
                print("Invalid choice. Please choose again.")
            def hunting():
                def hunt_deer():
                    return random.randint(0, 10) > 3

                def hunt_rabbit():
                    return random.randint(0, 10) > 5

                def hunt_squirrel():
                    return random.randint(0, 10) > 7

        elif decision == "trade":
            print("You have visited a trading post.")
            print("You can buy or sell goods here.")
            print("What would you like to do?")
            print("1. Buy supplies")
            print("2. Sell goods (goods = food got from hunting)")
            choice = input()
            if choice == "1":
                print("What would you like to buy?")
                print("1.Food")
                print("2.Ammo")
                choice = input()
                if choice == "1":
                    print("How much food would you like to buy? You have $" + str(self.player_money) + ".")
                    food_to_buy = int(input())
                    price_of_food = int(food_to_buy) * 5
                    if self.check_enough_money(price_of_food):
                        self.set_hunger(self.player_hunger - food_to_buy)
                        self.player_health += round(int(food_to_buy) / 5)
                        self.player_money -= price_of_food
                elif choice == "2":
                    print("How much ammo would you like to buy? You have " + str(self.bullets) + " bullets")
                    print("You have $" + str(self.player_money))
                    ammo_to_buy = input()
                    price_of_ammo = int(ammo_to_buy) * 50
                    if self.check_enough_money(price_of_ammo):
                        self.bullets += int(ammo_to_buy)
                        self.player_money -= int(ammo_to_buy) * 50
                else:
                    print("Invalid decision. Please choose again.")
                    self.make_decision()
            elif choice == "2":
                print("How many goods would you like to sell? You have " + str(self.goods) + " goods.")
                goods_to_sell = int(input())
                if self.check_enough_goods(goods_to_sell):
                    self.goods -= int(goods_to_sell)
                    self.player_money += int(goods_to_sell) * 5
        elif decision == "eat":
            print("How much food do you want to eat? You have " + str(self.goods) + " food")
            food_to_eat = int(input())
            self.goods -= int(food_to_eat)
            self.set_hunger(round(self.player_hunger / 5))
            self.player_health += round(int(food_to_eat) / 5)
        elif decision == "drink water":
            self.set_thirst(self.player_thirst - 10)
            self.set_fatigue(self.player_fatigue + 5)
        else:
            print("Invalid decision. Please choose again.")
            self.make_decision()

    def update_status(self):
        self.player_health -= (self.player_hunger + self.player_thirst + self.player_fatigue)

    def check_enough_money(self, price):
        if self.player_money < price:
            print("You do not have enough money to do that!")
            return False
        return True

    def check_enough_goods(self, goods):
        if self.goods < goods:
            print("You do not have enough goods to do sell!")
            return False
        return True

    def set_thirst(self, thirst):
        self.player_thirst = max(thirst, 0)

    def set_fatigue(self, fatigue):
        self.player_fatigue = max(fatigue, 0)

    def set_hunger(self, hunger):
        self.player_hunger = max(hunger, 0)

    def check_for_end_game(self):
        if self.player_health <= 0:
            print("You have died on the trail. Better luck next time.")
            self.game_in_progress = False
            return
        if not self.free_play and self.player_distance_traveled > self.distance_travelled_goal:
            print("Good job. You have reached Oregon.")
            print("During your stay in Oregon you have heard of a mystical place called Ohio")
            self.do_you_want_to_continue()

    def do_you_want_to_continue(self):
        print("Do you want to embark on this adventure(freeplay)?")
        if input("yes"):
            self.free_play = True
        elif input("no"):
            print("You have decided to stay in Oregon and start a farm.")
            self.game_in_progress = False



if __name__ == "__main__":
    game = OregonTrail()
    game.start_game()
