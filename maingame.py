import random

notDead = True
startingpointPassed = False
storePurchasableItems = []
inventory = []

print("Welcome to the start point of mountaineering!")
name = input("What is your name?")
print(f"Hello, {name}! Nice to meet you! Are you ready to go on an expedition?")


while notDead == True:
    if startingpointPassed == False:
        print("Welcome to the village! Here you can get your supplies")
        villageChoice = input("Where do you wanna go, the store or the blacksmith?")
        villageChoice = villageChoice.lower()
        print(villageChoice)
        startingpointPassed == True
        if villageChoice == "store":
            print("Welcome to the store, here you can get your supplies")
            luckyDay = random.randint(1,6)
            print(luckyDay)
            if luckyDay == 4:
                print("Today is your lucky day! If you can solve this puzzle you win some extra boots!")
            else:
                storePurchase = print("What do you wanna buy?")
                
