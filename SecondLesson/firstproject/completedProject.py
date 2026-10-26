joeseph = r"""
|--------|
//////////-----
|     $  |
|        |\
|        |
|/////////
"""

samuel = r"""
//////////
|     [] |\
|        | \
|        |--
|/////////
"""

def main():
    usrInventory = []
    while True:
        response = input("Do you want to talk to Joseph or Sam? [j,s] or to quit [q] or check your inventory [i]").lower()
        if response == "j":
            callJoseph(usrInventory)
        elif response == "s":
            callSamuel(usrInventory)
        elif response == "q":
            print("Exiting program. . . ")
            break
        elif response == "i":
            print(usrInventory)
        else:
            print("Invalid response.")

def callJoseph(inventory):
    print(joeseph)
    print("Hello! I am joseph. Here is a key.")
    inventory.append("key")

def callSamuel(inventory):
    print(samuel)
    print("Hello! I am sam. Here is a bag")
    inventory.append("bag")

main()