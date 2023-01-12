inGame = True
rooms = []
items = []
switches_value = "0000000"
chances = 3
lion_eat = False
code_solution = "4686"
code_tip = ""
win = False
print("""Welcome to my escape room game. You are in a room and there are 14 doors around you.
One of them is the door for your freedom. Find the correct one and enter the 4 digit password.
The digits can be found behind the other 13 doors. Find the digits and free yourself.""")
while inGame:
    room_number = input("Which door do you want to open (0-13)?\n")
    if room_number == "-1":
        print("Your story so far:")
        for i in range(len(items)):
            print("In room", rooms[i], ":", items[i])
    if room_number == "0":
        if "key" not in items:
            print("""You find a dark room here. Going around the wall you are looking for a  switch...
Finally you can turn on the light and realize that the room is empty. Only one light bulb is
hanging in the middle of the room. There seem to be something in the bulb. You unscrew the bulb
and break it. Now it is dark again so you must search between the shards. You cut yourself but find
a key on the ground. You put it in your pocket and leave the room.""")
            items.append("key")
            rooms.append(room_number)
            if "locked box" in items:
                print("Wait. You already have a box with a lock.")
                print("""You open the box and see the it is a tiny fridge with raw meat with it.
Maybe someone could it that.""")
                items.append("raw meat")
                rooms.append(room_number)
        else:
            print("You have already collected the key from the bulb. There is nothing left here.")
    if room_number == "1":
        print("""You see a creepy painting on the wall. On the left side a lion is standing on a chair
and changes a broken light bulb, while on the right side a clown is standing in front
of a board, trying to solve a complex equation.""")
        if "painting" not in items:
            items.append("painting")
            rooms.append(room_number)
    if room_number == "2":
        if "1010011" not in items:
            print("You see a series of numbers on the wall. Maybe it is good for something: 1010011")
            items.append("1010011")
            rooms.append(room_number)
        else:
            print("This is the same code as you saw before.")
    if room_number == "3":
        if "cat video" not in items:
            print("""There is a video projected on the wall. A small cat is running into a kitchen
and eat from a bowl. The bowl has a number 2 on it.""")
            items.append("cat video with number 2")
            rooms.append(room_number)
        else:
            print("""There is a video projected on the wall. A small cat is running into a kitchen
and eat from a bowl. The bowl has a number 2 on it.""")
    if room_number == "4":
        if "board with 7 light bulbs" not in items:
            print("""You step into the room to find an empty looking board on the wall with seven light
bulbs above it. Unfortunately you can't find any switches in the room. Maybe you can find the switches
somewhere else.""")
            items.append("board with 7 light bulbs")
            rooms.append(room_number)
        else:
            if switches_value == "1010011":
                print("The switches are shining nicely and a number 6 slowly appears on the board.")
                if "bulbs with digit 6" not in items:
                    items.append("bulbs with digit 6")
                    rooms.append(room_number)
    if room_number == "5":
        if "equation" not in items:
            print("""There is an equation on the wall. x = 10111 - 10001
How could that x be a one digit number?""")
            items.append("equation")
            rooms.append(room_number)
        else:
            print("The equation is x = 10111 - 10001")
    if room_number == "6":
        if room_number not in rooms:
            print("""Holy cow. There is a lion lying on the ground looking right at you.
There is something on the wall behind the lion but you can't read it.""")
            items.append("hungry looking lion")
            rooms.append(room_number)
            lion = input("Do you want to push the lion away from the wall? (yes/no)")
            if lion == "yes":
                if "raw meat" not in items:
                    print("""You tried to push the lion away with bare hands.
The lion gets a little angry and eats you.""")
                    inGame = False
                    lion_eat = True
                else:
                    print("""You throw the meat to the corner and the lion jumps after it. There is
a number 4 on the wall.""")
                    items.append("digit number 4 behind the lion")
                    rooms.append(room_number)
            else:
                print("Maybe you try it next time.")
        else:
            print("The lion is still looking at you at the wall.")
            lion = input("Do you want to push the lion away from the wall? (yes/no)")
            if lion == "yes":
                if "raw meat" not in items:
                    print("""You tried to push the lion away with bare hands.
            The lion gets a little angry and eats you.""")
                    inGame = False
                    lion_eat = True
                else:
                    print("""You throw the meat to the corner and the lion jumps after it. There is
            a number 4 on the wall.""")
                    items.append("digit number 4 behind the lion")
                    rooms.append(room_number)
            else:
                print("Maybe you try it next time.")
    if room_number == "7":
        if room_number not in rooms:
            print("You find an axe on the floor. At least your hand is not empty now.")
            items.append("axe on the floor")
            rooms.append(room_number)
        else:
            print("This room is empty now.")
    if room_number == "8":
        print("""You see a very disturbing painting on the wall. There is a burning building and two clowns are
climbing up on a ladder to a window with a question mark on it. One clown has a cat in his hand.""")
        if room_number not in rooms:
            items.append("painting with clowns and cat")
            rooms.append(room_number)
    if room_number == "9":
        print("""There is a piece of paper on the floor with a message on it: binary to decimal. It must be some clue
to another room.""")
        if room_number not in rooms:
            items.append("paper message - binary to decimal")
            rooms.append(room_number)
    if room_number == "10":
        print("""This is the room the the free world. You see another door inside with a locket on it.
The locket can be unlocked with a four digit code. Those digits must be around somewhere. There is a message next to
the door that says you have only three guesses. After that the door will be locked forever.""")
        if room_number not in rooms:
            items.append("escape door")
            rooms.append(room_number)
        guess = input("Do you want to guess now? (yes/no)")
        if guess == "yes":
            print("You have ", chances, "chances left.")
            code_tip = input("What is your guessed code?\n")
            if code_tip == code_solution:
                inGame = False
                win = True
            else:
                print("The lock remains still.")
                chances -= 1
                print("You have", chances, "lives left.")
                if chances == 0:
                    inGame = 0
        else:
            print("Maybe next time.")
    if room_number == "11":
        print("There is a clown standing in the middle of the room, holding three balloons.")
        if room_number not in rooms:
            items.append("clown with three balloons")
            rooms.append(room_number)
    if room_number == "12":
        print("You see seven switches on the wall but there are no lamps in the room.")
        if room_number not in rooms:
            items.append("7 switches on the wall")
            rooms.append(room_number)
        print("""You can change the switches by typing a 7 digits long number. Type 1 to turn on a switch 
and 0 to turn the switch off.""")
        switches_value = input("How do you turn the switches? e.g.: 0000000 -> all the switches are off\n")
        if len(switches_value) == 7:
            print("I hope this will work.")
        else:
            print("You should try with exactly 7 numbers.")
    if room_number == "13":
        if room_number not in rooms:
            items.append("damaged wooden board")
            rooms.append(room_number)
        print("""There is a wooden board on the wall. It is damaged and there is a hole on it.
You look inside and see something in the hole.""")
        if "axe on the floor" in items:
            print("You use the axe to break the wood and find a box inside.")
            items.append("locked box")
            rooms.append(room_number)
            if "key" in items:
                print("""You open the box and see that it is a tiny fridge with raw meat with it.
Maybe someone could it that.""")
                items.append("raw meat")
                rooms.append(room_number)
        else:
            print("You could probably crush the wood with some strong tool.")
if lion_eat:
    print("GAME OVER")
if win:
    print("Congratulations, you made it out!")
if chances == 0:
    print("""You tried to open the door three times but could not open it. Everything is dark now, you are 
trapped in the room forever. GAME OVER""")
