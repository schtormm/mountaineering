
import random
import time

notDead = True
startingpointPassed = False
name = ""
foodGuess = ""
randomItems = ["food", "wooden plank", "bicycle"]
storePurchasableItems = ["oxygen bottle", "rope", "jacket"]
blacksmithPurchasableItems = ["ice pick", "lamp", "gloves" ]
tavernPurchasableItems = ["tent", "backpack", "wool hat"]
inventory = []

print("Welcome to the start point of mountaineering!")
while len(name) < 2:
    name = input("What is your name? \n")
print(f"Hello, {name}! Nice to meet you! Are you ready to go on an expedition?")


while notDead == True:
    if startingpointPassed == False:
        print(f"Welcome to the village, {name}! Here you can get your supplies")
        villageChoice = input("Where do you wanna go, the store, the blacksmith, the tavern, or do you want to go further? \n Warning, once you go further you can't come back to the village! \n")
        villageChoice = villageChoice.lower()
        print(villageChoice)
        startingpointPassed == True
        if villageChoice == "store":
            print("Welcome to the store, here you can get your supplies")
            luckyDay = random.randint(1,6)
            print(luckyDay)
            if luckyDay == 4:
                print(f"Today is your lucky day, {name}! If you can solve this puzzle you win some extra boots!")
                word = ("bear")
                tries = 0
                length = len(word)
                display = "_"*len(word)
                print("The length of the word is:", length)
                print ("You have got 5 guesses")
                for i in range(0,5):
                    guess = input("Guess a letter:")
                    list = [guess]
                    if guess in word:
                        i = word.find(guess)
                        display = display[:i] + guess + display[i + 1:] 
                        print (display) 
                        tries += 1 
                        if display == "bear" :
                            print("You guessed the word!, you have won some climbing boots!")
                            inventory.append("climbing boots")
                            break
                    else:
                        print ("That letter is not in the word")
                        tries += 1
                if tries == 5 and display != "bear":
                    final_guess = input("What is the word?") 
                    if final_guess == ("bear"):
                        print("Correct, you won some climbing boots!")
                        inventory.append("climbing boots")
                        print("Here's what's in your inventory now:" , inventory)
                    else:
                        print ("Incorrect, Try again")     


            else:
                print ("Your lucky number is not 4, you win nothing.")
                print ("Here's a list of items that can be bought here:")
                print(storePurchasableItems)
                storePurchase = input("What do you wanna buy? \n")
                storePurchase = storePurchase.lower()
                if storePurchase in storePurchasableItems:
                    inventory.append(storePurchase)
                    print("Here's what's in your inventory now:" , inventory)
                else:
                    continue
        elif villageChoice == "blacksmith":
            print("Welcome to the blacksmith, here you can get useful climbing gear")
            luckyDay = random.randint(1,6)
            print(luckyDay)
            if luckyDay == 6:
                print(f"Today is your lucky day, {name}! If you can solve this puzzle you win a sword!")
                tries = 0
                points = 0
                quizQuestion1 = ("What is the highest mountain on earth?")
                quizQuestion2 = ("Which mountain range is spread over 7 countries in Europe?")
                quizQuestion3 = ("How many mountains do the alps have? (answer in numbers)")
                answer1 = ("mount everest")
                answer2 = ("the alps")
                answer3 = ("82")
                while points == 0 and tries < 5:
                    print ("Give the right answers to win some gear!")
                    print ("You have 5 tries to get 3 right answers!")
                    print ("Question 1:")
                    print(quizQuestion1)
                    quizGuess = input("The answer to question 1:").lower()
                    if quizGuess == answer1:
                        print ("That's the right answer!")
                        points = points + 1
                        tries = tries + 1
                        print ("points:", points)
                    else:
                        print ("wrong!")
                        tries = tries +1
                while points == 1:
                    print (quizQuestion2) 
                    quizGuess = input("The answer to question 2:").lower()
                    if quizGuess == answer2:
                        print ("That's the right answer!")
                        points = points + 1
                        tries = tries + 1
                        print ("points:", points)
                    else:
                        print ("That's the wrong answer, try again")
                        tries = tries + 1
                while points == 2:
                    print ("question 3:")
                    print (quizQuestion3)
                    guess = input("The answer to question 3:").lower()
                    if guess == answer3:
                        print ("That's the right answer!")
                        points = points + 1
                        tries = tries + 1
                        print ("points:", points)
                    else: 
                        print ("That's the wrong answer, try again")
                        tries = tries + 1
                if points == 3:
                    print ("points:", points)
                    print ("You have won the quiz! you win a sword!")
                    inventory.append("sword")
                    print("Here's what's in your inventory now:" , inventory)
                if tries == 5:
                    print ("You have no tries left, game over")
            else:
                print ("Your lucky number is not 6, you win nothing.")
                print ("Here's a list of items that can be bought here:")
                print (blacksmithPurchasableItems)
                blacksmithPurchase = input("What do you wanna buy? \n")                
                blacksmithPurchase = blacksmithPurchase.lower()
                if blacksmithPurchase in blacksmithPurchasableItems:
                    inventory.append(blacksmithPurchase)
                    print("Here's what's in your inventory now:" , inventory)
        elif villageChoice == "tavern":
            print("Welcome to the tavern, here you can get useful camping equipment")
            print ("Here's a list of items that can be bought here: \n" , tavernPurchasableItems)
            luckyDay = random.randint(1,6)
            print(luckyDay)
            if luckyDay == 6:
                chosenItem = random.randint(0,2)
                print (f"Today is your lucky day, {name}! If you can solve this puzzle you win one of the random items, {randomItems[chosenItem]}" )
                win = 0
                number = 36
                while win < 1:
                    numberGuess = int(input("Enter a number:"))
                    if numberGuess < number:
                        print("Higher")
                    elif numberGuess > number:

                        print ("Lower")
                    else:
                        numberGuess == number
                        print("That's the right number!")
                        print ("You win:", randomItems[chosenItem])
                        inventory.append(randomItems[chosenItem])
                        print("Here's what's in your inventory now:" , inventory)
                        win = win + 1
            tavernPurchase = input("What do you wanna buy? \n")                
            tavernPurchase = tavernPurchase.lower()
            if tavernPurchase in tavernPurchasableItems:
                inventory.append(tavernPurchase)
                print("Here's what's in your inventory now:" , inventory)
        elif villageChoice == "further": 
            startingpointPassed = True
            print("Welcome to the meadow! There's some food hidden in the shed here.. but you don't have a key")
            print("To find the key, you have to guess where on the grid the key lies... \n")
            for b in range(0,3):
                print("x", end = "\t")
                for c in range(0,2):
                    print("x", end ="\t")
                print("\n")
            foodLocations =["middle left", "left middle"]
            while foodGuess not in foodLocations:
                foodGuess = input("Guess where the key to the shed is (in english, for example; right middle)")
                print("You've entered:", foodGuess)
            print("You've found the key, and have opened the shed to find the food.")
            inventory.append(randomItems[0])
            print("Here's what's in your inventory now:" , inventory)
            time.sleep(5)
            print("You've walked from the meadow into the woods.. \n There's something lurking in the shadows..")
            time.sleep(4)
            print("It's a WOLF!")
            time.sleep(3)
            if "sword" in inventory:
                print("You pull out your sword, and fight off the wolf with a few intimidating swings of the sword.")
            elif "ice pick" in inventory:
                print("You grab your ice pick, and stab the wolf in its heart. You're safe.")
            else: 
                print("You get attacked by the wolf, and try to find something to defend yourself with. \n Unfortunately, you can't find anything useful and the wolf mauls you to death.")
                print("Restart the game to try again.")
                notDead = False
                quit()
            time.sleep(4)
            print("You grab a piece of wood from a tree and walk further towards the mountain")
            inventory.append(randomItems[1])
            print("Here's what's in your inventory now:" , inventory)
            time.sleep(4)
            print ("You walk towards the mountain..")
            time.sleep(4)
            if "tent" in inventory:
                print("You arrive at the basecamp, from here you will start climbing the mountain")
                print("You set up your tent, and go to sleep")
                time.sleep(4)
                print("Tomorrow your climb begins..")
            else:
                print("You arrive at the basecamp, but you don't have a tent, so you must sleep outside in the cold weather..")
                time.sleep(4)
                print("You froze to death")
                time.sleep(4)
                print("Restart the game to try again")
                notDead = False
            if not "climbing boots" in inventory:
                print("You try to start climbing the mountain, but you struggle because you haven't got the proper gear, so you have to go back to the village to get climbing boots")
                print("You can win the climbing boots by solving a puzzle at the village store")
                startingpointPassed = False                
                continue
            else:
                print("You start climbing..")
                time.sleep(3)
                print ("In the distance, you see a old bridge..")
                time.sleep(3)
                print ("The bridge is broken, to repair it, you need a wooden plank and rope.")
                time.sleep(3)           
            if not ("rope" and "wooden plank" in inventory):
                print ("You do not have the required items to repair the bridge, you have got to go back to the village.")
                print ("You can buy rope at the village store")
                startingpointPassed = False
            else:
                print("You fix the old bridge by using your rope and wooden plank")
                inventory.remove("wooden plank")
                inventory.remove("rope")
                print("Here's what's in your inventory now:" , inventory)
            time.sleep(3)
            print ("You start climbing further..")
            time.sleep(3)
            print ("While climbing toward the top of the mountain, you come across a cave..")
            time.sleep(3)
            print("You hear something growling in the cave, do you want to enter?")
            enter = input("Do you want to enter the cave? (yes or no) \n ").lower()
            if enter == "yes":
                print ("You enter the cave")
                if "lamp" in inventory:
                    print("You use your lamp to bring light into the darkness of the cave")
                    time.sleep(3)
                    print("you see something in the corner, its a bear")
                    time.sleep(3)
                    print("you run walk away as fast as you can, not looking back.")
                    time.sleep(3)
                    chance = random.randint(1,6)
                    if chance == 4 or 5:
                         print("You escaped")
                         print("you continue your journey towards the top")
                    else:
                        print("The bear got to you and killed you, game over")
                        notDead = False
                else:
                    print("The cave is too dark and you dont have a lamp")
                    time.sleep(3)
                    print("You go back to the entrance of the cave and continue your journey")
            elif enter == "no":
                print ("you walk past the cave, continuing your journey towards the top")
            print("You've reached the glacier, this is the last point before the summit of the mountain!")
            if "ice pick" in inventory:
                print("You try to reach the summit, but the way to the summit is a bit unclear, so you must climb a bit with the ice pick.")
                print("To climb, you must solve a maths problem")
                oplossing = 98.5
                klimInput = float(input("What is the result of the calculation 12.4 + 24.6 *3.5 (please use . instead of ,)"))
                if klimInput != oplossing:
                    print("You have not managed to climb to the summit, try again ")
                    quit()
                else: 
                    print("Congratiulations, you've managed to climb to the summit and have completed this game. You can gaze here for a few more moments")
                    time.sleep(20)
                    print("There are more possible ways to win the game, try again if you want!")
                    break
            else:
                 print("You didn't get the ice pick, and thus can't get to across the glacier, you slip and fall all the way down the mountain and die")
                 print("Restart the game to try again.")
                 notDead = False
        elif villageChoice == "inventory":
            print("Here's what's in your inventory now:" , inventory)