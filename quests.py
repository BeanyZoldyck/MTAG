import time
try:
    import gift_shop#this file 
except ModuleNotFoundError:
    print("(Btw this code will be used where it can access my modular gift shop code)")
playerEgo = 100
playerBag = ['stick']
playerBread = 50
possibleInterests = ["Lexi", "Ali", "Chuka", "Socrates"]
relations = {"Lexi": 10,
             "Ali": 15,
             "Chuka": -4,
             "Socrates": 10}

print('Ego:',playerEgo, '$:',playerBread, 'Interest:',relations[possibleInterests[-1]])
def printSlow(text):
    for i in text:
        print(i, flush=True, end='')
        time.sleep(.02)
    time.sleep(1)
    print()
def date(interest):
    global playerEgo
    global playerBread
    global playerBag
    global relations
    playerDate = input(f"Do you ask {interest} to go out? (y/n) ")
    if playerDate == "y":
        printSlow("They say yes. You pick them up from their home, and are now driving around town. After some small talk the actual content of the date is brought up.")
        playerPlace = input("Do you go to a restaurant? (y/n) ")
        if playerPlace == "y":
            printSlow("You now are at Coney Island.")
            playerRude = input("After a 15 minute wait, the staff brings you the wrong meal. You ordered the cheeseburger and they brought you nothing at all, as you are still waiting.\nThe waitress comes back around and asks how everything is going. Do you let her have it? (y/n) ")
            if playerRude == "y":
                printSlow(f"{interest} thinks less of you because the waitress was only 12 years old (it's a family business). {interest} then 'remembers' that they left their wallet in the car. Which is at their home because you drove them here and you have to pick up the tab.\n-15 RP\n-40 dollars")
                playerEgo -= 1
                playerBread -= 40
                relations[interest] -= 15
                backInBlood(interest)
                return
            else:
                printSlow(f"{interest} had a fun time, and found it to be a relaxing evening. You two split the bill.\n+10 RP\n-20 dollars")
                playerEgo += 8
                playerBread -= 20
                relations[interest] += 10
                #put code here to start the school_quest
        else:
            print(f"{interest} visibly loses some interest. They bring up an amusement park that is having a sale for $15. This may be the last chance.")#lol
            userAmuse = input("Do you go to the amusement park? (y/n) ")
            if userAmuse == "y":
                printSlow(f"{interest} had a fun time and associate you with thrills.\n+15 RP -10 dollars")
                playerEgo += 10
                playerBread -= 10
                relations[interest] += 15
                #put code here to start the school_quest
            else:
                printSlow(f"You drive around aimlessly for a while, but {interest} enjoys the time.\n+1 RP")
                relations[interest] += 1
                #put code here to start the school_quest
    else:
        userTime = input("Do You seek time with your interest? (y/n) ")
        if userTime == "y":
            printSlow(f"You find yourself near {interest} a lot.")
            userTalk = input("Do you talk to them? (y/n) ")
            if userTalk == "y":
                printSlow("You two have a lot in common.\n+7 RP")
                relations[interest] += 7
                #put code here to start the school_quest
            else:
                printSlow(f"{interest} finds it weird that you just stand near them.\n-5RP")
                relations[interest] -= 5
                backInBlood(interest)
                return
        else:
            printSlow(f"You don't talk to {interest} much that week.")
            user_hole = input("Do you regret it? (y/n) ")
            if user_hole == "y":
                printSlow("-10 Ego")
                playerEgo -= 10
                backInBlood(interest)
                return
            else:
                printSlow("Time with you is a privilege anyways.\n+2 Ego")
                playerEgo += 2
    print()
    goNext(interest)


def backInBlood(interest):#the action of getting the RP back in blood
    global playerEgo
    global playerBread
    global playerBag
    global relations
    printSlow(f"Recent events have not left {interest} seeming interested in you.")
    userBuy = input("Do you solve the problem with material things? (y/n) ")
    if userBuy == 'y':
        #playerBread, playerBag = gift_shop(playerBread, playerBag)
        #in the implementation this won't be commmented out
        if len(playerBag) == 1:
            userGift = input(f'Do you give {interest} "{playerBag[0]}"? (y/n) ')
            if userGift == 'y':
                userGift = playerBag[0]
        else:
            userGift = input(f"What will you give {interest}? You have {[', '.join([str(i)+' (x'+str(inventory.count(i))+')' for i in set(inventory)]),'nothing'][inventory==[]]}")
        if userGift in playerBag:
            printSlow(f'{interest} loved the gift!\n+10 RP')
            relations[interest] += 10
        else:
            printSlow("You can't do that. Nothing changes")
    else:
        userTalk = printSlow(f'Do you try to talk to {interest}? (y/n) ')
        if userTalk == 'y':
            printSlow('You come to somewhat of an understanding with them.\n+5 RP')
            relations[interest] += 5
        else:
            printSlow('No change occurs in their feelings. It may be time to go next.')

def goNext(interest):
    global playerEgo
    global playerBread
    global playerBag
    global relations
    printSlow(f"Recent events have not left {interest} hating you.")
    userPush = input("Do you pursue further ? (y/n) ")
    if userPush == 'y':
        if playerEgo >= 110:
            printSlow(f'You are strangey confident in future conversations. {interest} respects someone who can talk about themselves for 10 minutes straight. (y/n)')
            relations[interest] += 5
        else:
            printSlow(f"{interest} realizes that you are pretty cringe when considered in a vacuum.")
            relations[interest] -= 3
    else:
        userTalk = input(f'You give {interest} some space. Do you give them more space? (y/n) ')
        if userTalk == 'y':
            printSlow(f'It\'s been a while... {interest} starts to forget the fun date you guys had a while back.')
            relations[interest] -= 3
        else:
            printSlow(f'{interest} remembers the fun date you guys had a while back. +3 RP')
            relations[interest] += 3
            
date(possibleInterests[-1])

print('Ego:',playerEgo, '$:',playerBread, 'Interest:',relations[possibleInterests[-1]])
