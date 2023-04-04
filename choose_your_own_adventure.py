answer = input("Do you want to play? ")
if answer.lower() != "yes":
    print("Have a nice day!")
    quit()

name = input("Type your name: ")
answer = input("You are on a dirt road with your friend Ryan, it has come to an end and you can go left of right. Which way would you like to go? ")

if answer.lower() == "left":
    answer = input("You have come across a cabin with a sign of a deer on the outside, do you want to ENTER the cabin, or keep going DOWN the road? ")

    if answer.lower() == "enter":
        print('Ryan: "Oooo this cabin looks pretty freaky."')
        print("You walk up to the door \n It appears to be locked")
        print('Ryan: "Lets look around for a key!"')
        print('You see a DOORMAT, an empty POT, and a rain GUTTER.')
        while True:
            answer = input("Which do you want to check for the key? ")
            if answer.lower() == "pot":
                print("You found the key!")
                break
            elif answer.lower() == "doormat":
                print("You don't find the key.")
            elif answer.lower() == "gutter":
                print("You don't find the key.")
            else:
                print("Invalid answer, try again")
                continue
        print('Ryan: "Alright, lets do this!" \n You put the key in the lock and open the door. \n The door creaks open to reveal an empty room with 3 doors. \n The first door has a picture of a GHOST on it \n The second door has a picture of a LION \n The third door has a picture of a DEER')
        answer = input("Which door do you choose? ")
        if answer.lower() == "ghost":
            print('Ryan: "A picture of a ghost? Someone must be trying to play a prank on us!')
            print("You open the door and a Ghastly Ghoul jumps out and scares you and Ryan to death!")
            quit()
        elif answer.lower() == "lion":
            print('Ryan: "No way a Lion live in there LOL!"')
            print("You open the door, and to your surprise, a Lion in fact lives in there \n You and Ryan are both eaten by a lion")
        elif answer.lower() == "deer":
            print('Ryan: "Ahhh a deer door, like the sign on the outside of the cabin!"')
            print("You open the door and find a room filled with gold! \n You are rich!")  
    elif answer.lower() == "down":
        print("You keep going down the path, but it doesn't seem to end.")
        counter = 0
        while counter <= 10:
            answer = input("Do you want to keep FOLLOWing the path or TURN around? ")
            if answer.lower() == "turn":
                print("You turn around and keep walking, but there seems to be no end")
                counter += 1
                continue
            elif answer.lower() == "follow":
                print("You keep following the path")
                counter += 1
                continue
            else:
                print("Not a valid answer, enter TURN or FOLLOW.")
                continue
        print(f'Ryan: "I am really starting to freak out {name}, theres no end to this Road!!!')
        print("You and Ryan keep wandering the road for eternity looking for a way out")
    else:
        print("Not a valid option, you lose.")
        quit()
elif answer.lower() == "right":
    print('You come across a field of flowers and a river.')
    answer = input("Do you walk into the field of FLOWERS, or try to cross the RIVER? ")
    if answer.lower() == 'flowers':
        print('Ryan: "These flowers are so beautiful!"')
        print("As you walk into the field, you and Ryan get stuck")
        print('Ryan: "Oh no is this quicksand?!"')
        print("You and Ryan have suffocated in quicksand.")
        quit()
    elif answer.lower() == "river":
        print("You and Ryan wade out into the water.")
        print('Ryan: "Dang this water is really cold! And it just keeps getting deeper!"')
        print("Right as Ryan finishes what he's saying, he gets dragged under!")
        print("You panic and try to run back, but you get pulled under too.")
        print("You and Ryan got eaten by sharks.")
        quit()
    else:
        print("Not a valid option, you lose.")
        quit()
else:
    print("Not a valid option, you lose.")
    quit()