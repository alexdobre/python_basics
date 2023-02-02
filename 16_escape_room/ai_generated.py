import time

# introduction
print("Welcome to the land of Hyrule.")
time.sleep(1)
print("You are a young hero on a quest to save the princess Zelda from the evil Ganon.")
time.sleep(1)
print("You are currently in the starting village. You can go North, South, East, or West.")

# starting point
direction = input("Which direction would you like to go? ")

# different paths
if direction == "North":
    print("You have entered a forest. You see a sword on the ground.")
    sword = input("Would you like to pick up the sword? ")
    if sword == "Yes":
        print("You have obtained the sword. You feel stronger and more confident.")
    else:
        print("You leave the sword on the ground. You may regret this later.")
elif direction == "South":
    print("You have entered a desert. You see a potion on the ground.")
    potion = input("Would you like to pick up the potion? ")
    if potion == "Yes":
        print("You have obtained the potion. You feel healthier and more energized.")
    else:
        print("You leave the potion on the ground. You may regret this later.")
elif direction == "East":
    print("You have entered a mountain. You see a shield on the ground.")
    shield = input("Would you like to pick up the shield? ")
    if shield == "Yes":
        print("You have obtained the shield. You feel more protected and secure.")
    else:
        print("You leave the shield on the ground. You may regret this later.")
elif direction == "West":
    print("You have entered a lake. You see a boat on the ground.")
    boat = input("Would you like to pick up the boat? ")
    if boat == "Yes":
        print("You have obtained the boat. You feel more mobile and adventurous.")
    else:
        print("You leave the boat on the ground. You may regret this later.")
else:
    print("Invalid direction. Please try again.")

# final message
print("You continue on your quest. Good luck on your journey.")