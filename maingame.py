import random

notDead = True
startingpointPassed = False
name = ""
foodGuess = ""
storePurchasableItems = ["oxygen bottle", "rope", "jacket"]
blacksmithPurchableItems = ["ice pick", "lamp", "gloves" ]
inventory = []

print("Welcome to the start point of mountaineering!")
while len(name) < 2:
    name = input("What is your name? \n")
print(f"Hello, {name}! Nice to meet you! Are you ready to go on an expedition?")


while notDead == True:
    if startingpointPassed == False:
        print(f"Welcome to the village, {name}! Here you can get your supplies")
        villageChoice = input("Where do you wanna go, the store, the blacksmith, or do you want to go further? \n Warning, once you go further you can't come back to the village! \n")
        villageChoice = villageChoice.lower()
        print(villageChoice)
        startingpointPassed == True
        if villageChoice == "store":
            print("Welcome to the store, here you can get your supplies")
            luckyDay = random.randint(1,6)
            print(luckyDay)
            if luckyDay == 4:
                print(f"Today is your lucky day, {name}! If you can solve this puzzle you win some extra boots!")
            else:
                print ("your lucky number is not 4, you win nothing.")
                print ("here's a list of items that can be bought here:")
                print(storePurchasableItems)
                storePurchase = input("What do you wanna buy? \n")
                storePurchase = storePurchase.lower()
                if storePurchase in storePurchasableItems:
                    inventory.append(storePurchase)
                    print(inventory)
        elif villageChoice == "blacksmith":
            print("Welcome to the blacksmith, here you can get useful climbing gear")
            luckyDay = random.randint(1,6)
            print(luckyDay)
            if luckyDay == 6:
                print(f"Today is your lucky day, {name}! If you can solve this puzzle you win some special climbing shoes!")
            else:
                print ("your lucky number is not 6, you win nothing.")
                print ("here's a list of items that can be bought here:")
                print (blacksmithPurchableItems)
                blacksmithPurchase = input("What do you wanna buy? \n")                
                blacksmithPurchase = blacksmithPurchase.lower()
                if blacksmithPurchase in blacksmithPurchableItems:
                    inventory.append(blacksmithPurchase)
                    print(inventory)
        elif villageChoice == "further": 
            startingpointPassed = True
            print("Welcome to the meadow! There's some food hidden in the shed here.. but you don't have a key")
            print("To find the key, you have to guess where on the grid the key lies... \n")
            for b in range(0,3):
                print("x", end = "\t")
                for c in range(0,2):
                    print("x", end ="\t")
                print("\n")
            foodLocation = "left middle"
            print("\n")
            while foodGuess != foodLocation:
                foodGuess = input("Guess where the key to the shed is (in english)")
            print("You've found the key, and have opened the shed to find the food.")
            
                            

