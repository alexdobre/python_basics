print("-Welcome to Craiova. A nice city with beatiful people!")
print("-...Well maybe not but you just need to know one thing:you are in search for The Forbidden Beer!")

character = {
    "inventory": {
        "sword": False,
        "shield": False,
        "slingshot": False
    },
    "catena": "",
    "asalt_fizic": "",
    "pay": "",
    "block": "",
    "choices": {
        "Catena": False
    }
}
Arma_craioveana = input(
    "-Don't go with an empty hand!You have an option to choose a weapon.What will you choose? Sword(1) or Shield(2) or Slingshot with rocks(3)")

play = True

while play:
    if Arma_craioveana == "1":
        print("-A sword,good choice!Now you have the ability to attack at close range")
        character["inventory"]["sword"] = True
    if Arma_craioveana == "2":
        print("-A shield,good choice!Now you have the ability defend yourself by blocking attacks")
        character["inventory"]["shield"] = True
    if Arma_craioveana == "3":
        print("-A slingshot,good choice!Now you have the ability to attack at long range!")
        character["inventory"]["slingshot"] = True
    print("-On your way you encounter a skinny man.")
    character["catena"] = input("-He offers you a special medicine.Do you accept his offer? yes(y) no(n)")
    if character["catena"] == "y" and character["inventory"]["sword"]:
        print("-Oh no!You took a pill from a stranger now you have seen the secrets of the universe and decide you are not worthy of that information.So you use your sword to do that")
        play = False
        break
    if character["catena"] == "y":
        print("You accept his offer and take the pill.You get a little dizzy and now your atacks and blocks are weaker.")
    if character["catena"] == "n":
        print("-You refuse the man's offer and walk away...and he just sits there looking at you")
    print("-As you get away from the strange man you encounter another man but this time he looks more agrresive.")
    if character["inventory"]["slingshot"] == True or character["inventory"]["sword"] == True:
        character["asalt_fizic"] = input("Will you atack him with your weapon? y/n")
        if character["asalt_fizic"] == "y" and character["catena"] == "y":
            print("-You tried to attack the man with your weapon but you were a little dizzy from the medicine so you missed.The man got VERY angry and ran up to you and punched you in the face")
            play = False
            break
        elif character["asalt_fizic"] == "y" and character["catena"] == "n":
            print("-You attacked the man with your weapon in the head and he got knocked out.You continue on with your journey")
        elif character["asalt_fizic"] == "n":
            print("-You decide not to attack the man and he walks by you...calmly")
    if character["inventory"]["shield"] == True:
        character ["block"] = input("Do you block with your shield in case he tries to attack you? y/n")
        if character ["block"] == "y":
            print("You predicted that he would attack you but you blocked his attack.He hurt his hand and ran away")
        if character["block"] == "n":
            print("The man tried to hit you but you didn't block beforehand so he hurt you really bad and you need to be hospitalized")
            play = False
            break
    print("As you get away from the man you arrive at the store.The forbidden beer awaits you...")
    character["pay"] = input("You get the beer from the fridge and to the register.The lady there asks you for the money.Would you like to pay for the beer? y/n")
    if character["pay"] == "y":
            print("you pay for the beer and walk back home to consume your newly aquired beer.")
            play = False
            break
    if character["pay"] == "n" and character["inventory"]["shield"] == True:
            print("Surprisingly the lady pulls out a gun from under the register and tries to shoot you but because you chose the shield you were quick enough to block the bullet and direct it back to the lady.You take the beer and walk home victorious")
            play = False
            break
    if character["pay"] == "n" and character["inventory"]["shield"] == False:
            print("Surprisingly the lady pulls out a gun from under the register and tries to shoot you but because you did not choose the shield you got seriously hurt and you did not achieve your goal to aquire the forbidden beer... :(")
            play = False
            break






print("Game over")

