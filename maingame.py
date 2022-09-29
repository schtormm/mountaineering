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
                if tries == 5:
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
                    numberGuess = input("Enter a number:")
                    numberGuess = int(numberGuess)
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
            foodLocation = "left middle" or "middle left"
            while foodGuess != foodLocation:
                foodGuess = input("Guess where the key to the shed is (in english, for example; right middle)")
                print("You've entered:", foodGuess)
            print("You've found the key, and have opened the shed to find the food.")
            inventory.append(randomItems[0])
            print("Here's what's in your inventory now:" , inventory)
            time.sleep(5)
            print("You've walked from the meadow into the woods.. \n There's something lurking in the shadows..")
            time.sleep(2)
            print("It's a WOLF!")
            if "sword" in inventory:
                print("You pull out your sword, and fight off the wolf with a few intimidating swings of the sword.")
            elif "ice pick" in inventory:
                print("You grab your ice pick, and stab the wolf in its heart. You're safe.")
            else: 
                print("You get attacked by the wolf, and try to find something to defend yourself with. \n Unfortunately, you can't find anything useful and the wolf mauls you to death.")
                print("Restart the game to try again.")
                notDead = False