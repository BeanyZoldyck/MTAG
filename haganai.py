import time
import random
import math
from functools import reduce
playerEgo = 50
playerBag = ['stick']#random even is you find money or gifts
playerBread = 35
possibleInterests = ["Lexi", "Ali", "Chuck", "Socrates"]
relations = {"Lexi": 7,
             "Ali": 12,
             "Chuck": -4,
             "Socrates": 10}
info={"Lexi": "A mean-pretty girl who is relatively popular for how unspoken they are. Better than everyone, smart, kind, pretty, and spiritual. \nLikes: Soccer, makeup, boys, texting. \nDislikes: Driving, boys, people.",
     "Ali": "A short and witty girl who seems quiet, but has a very bubbly personality when you get to know them. Strange obsession with a different celebrity or fictional character every week. \nLikes: Shows that prominently feature queer-coded characters, cats. \nDislikes: Public Speaking, Animal cruelty",
     "Chuck": "A cantankerous and egotistical individual who makes everything about himself while still finding a way to berate others. Can bench 250. \nLikes: Lifting, Video Games, Bubble Wrap. \nDislikes: Humid weather, cold showers, people (x3)",
     "Socrates": "Greek philosopher from Athens accredited as a founder of Western Pilosophy. An enigmatic figure you can only learn about from dialogue. \nLikes: Soliloquies, Debating, Public Speaking, Irony. \nDislikes: Writing, Status-quo, Hemlock"
}
items='''cabbage
rose
magazine
stick
Thrustmaster T80 Ferrari 488 GTB'''.split('\n')
prices=[2.0,
    5.0,
    20.0,
    .5,
    130.0]
descriptions='''A literal head of cabbage.
A rose flower, a woody perennial flowering plant of the genus Rosa said to represent love.
A random popular culture magazine filled with the latest celebrity gossip
a stick from outside. Why is this on the shelf?
8:10 scale replica of the genuine Ferrari 488 GTB wheel, officially licensed by Ferrari and PlayStation 4, and designed to provide total realism.'''.split('\n')
samples={}#link interests to respective sample texts
def Markov(sampleText, initial=''):
    ngrams={}
    sampleTexts=sampleText.split('\n')
    inputs=len(sampleTexts)
    length=0
    for i in sampleTexts:
        length+=len(i.split())/inputs
    length=round(length)
    sample=sampleText.split()
    for i in enumerate(sample):
        try:
            ngrams[i[1]].append(sample[i[0]+1])
        except KeyError:
            ngrams[i[1]] = []
            try:
                ngrams[i[1]].append(sample[i[0]+1])
            except IndexError:
                continue
        except IndexError:
            pass
    if not initial:
        currentgram = random.choice(sample)
    else:
        currentgram=initial
    result = currentgram
    for i in range(length):
        poss = ngrams[currentgram]
        nexT = random.choice(poss)
        result += ' '+nexT
        currentgram = random.choice(ngrams[result.split()[-1]])
    return result
def show(sample, buffer):
    print('-'*buffer)
    line=0
    for i in sample.split(' '):
        line+=len(i)+1
        if '\n' in i:
            line=len(i)+1
        if line> buffer:
            print()
            print(i, end=' ')
            line=len(i)+1
        else:
            print(i,end=' ')
    print()
    print('-'*buffer)
def printSlow(text, wpm=800):
    for i in text:
        print(i, flush=True, end='')
        time.sleep(12/wpm)
    time.sleep(1)
    print()
def displayItems(offSet):
    print('\n')
    for i in enumerate(items[offSet:]):
        print(i[0]+offSet+1,i[1])

def displaySingle():
    userItem=int(input("Enter a number to select an item: "))-1
    print(f'{descriptions[userItem]}\n{items[userItem]} costs ${prices[userItem]}.')
    
def flex(playerMoney, inventory):
    return f"Your net worth is ${playerMoney} and you have {[', '.join([str(i)+' (x'+str(inventory.count(i))+')' for i in set(inventory)]),'nothing'][inventory==[]]}"

def buyItem(playerMoney, inventory):
    userItem=int(input("Enter a number to select an item to buy: "))-1
    if playerMoney >= prices[userItem]:
        inventory.append(items[userItem])
        print(f"You bought {items[userItem]} for {prices[userItem]}, so your new balance is ${playerMoney-prices[userItem]}")
        playerMoney = playerMoney-prices[userItem]
        if userItem > 4:
            items.pop()
            prices.pop()
            descriptions.pop()
        return playerMoney
    else:
        print(f"You dont have enough money to buy {items[userItem]}!\nYou would need ${prices[userItem]-playerMoney} more.")
        return playerMoney

def sell(playerMoney, inventory):
    product=input(f"You have {[', '.join([str(i)+' (x'+str(inventory.count(i))+')' for i in set(inventory)]),'nothing'][inventory==[]]}\nWhat do you want to sell?: ")
    if product in inventory:
        price=float(input("How much do you want to sell it for?\n"))
        if price>160:
            print("That is not a reasonable price")
            return playerMoney
        else:
            inventory.remove(product)
            items.append(product)
            prices.append(price)
            descriptions.append(input("Describe the item: "))
            return playerMoney+price
    else:
        if product != 'nothing':
            print("You do not have",product)
        else:
            print("That makes sense.")
        return playerMoney
def shop(playerMoney, inventory):
    global items
    global prices
    global descriptions
    while True:
        displayItems(0)
        option=input("\nEnter 0 to buy item\nEnter 1 to display an item\nEnter 2 to display your possesions\nEnter 3 to sell\nEnter q to quit\n")
        if option=='1':
            displaySingle()
        elif option == '0':
            playerMoney=buyItem(playerMoney, inventory)
        elif option =='2':
            print(flex(playerMoney, inventory))
        elif option =='3':
            playerMoney=sell(playerMoney, inventory)
        else:
            break
    return playerMoney, inventory
def firstDate(interest):
    global playerEgo
    global playerBread
    global playerBag
    global relations
    playerDate = input(f"Are you sure you want to ask {interest} to go out? (y/n) ")
    if playerDate == "y":
        printSlow("They say yes. You pick them up from their home, and are now driving around town. After some small talk the actual content of the date is brought up.")
        converse(interest)
        playerPlace = input("Do you go to a restaurant? (y/n) ")
        if playerPlace == "y":
            printSlow("You now are at Coney Island.")
            playerRude = input("After a 15 minute wait, the staff brings you the wrong meal. You ordered the cheeseburger and they brought you nothing at all, as you are still waiting.\nThe waitress comes back around and asks how everything is going. Do you let her have it? (y/n) ")
            converse(interest)
            if playerRude == "y":
                converse(interest)
                printSlow(f"{interest} thinks less of you because the waitress was only 12 years old (it's a family business). {interest} then 'remembers' that they left their wallet in their car. Which is at their home because you drove them here and you have to pick up the tab.\n-15 RP\n-40 dollars")
                playerEgo -= 1
                playerBread -= 40
                if playerBread < 0:
                    printSlow(f"You didn't have enough money, but luckily {interest} spotted you the rest..")
                    relations[interest] -= -playerBread
                    playerBread=0
                relations[interest] -= 15
                backInBlood(interest)
                return
            else:
                converse(interest)
                printSlow(f"{interest} had a fun time, and found it to be a relaxing evening. You two split the bill.\n+10 RP\n-20 dollars")
                playerEgo += 8
                playerBread -= 20
                relations[interest] += 10
                #put code here to start the school_quest
        else:
            converse(interest)
            print(f"{interest} visibly loses some interest. They bring up an amusement park that is having a sale for $10. This may be the last chance.")#lol
            userAmuse = input("Do you go to the amusement park? (y/n) ")
            if userAmuse == "y":
                converse(interest)
                printSlow(f"{interest} had a fun time and associate you with thrills.\n+15 RP -10 dollars")
                playerEgo += 10
                playerBread -= 10
                if playerBread < 0:
                    printSlow(f"You didn't have enough money, but luckily {interest} spotted you the rest..")
                    relations[interest] -= -playerBread
                    playerBread=0
                relations[interest] += 15
                #put code here to start the school_quest
            else:
                converse(interest)
                printSlow(f"You drive around aimlessly for a while, but {interest} enjoys the time.\n+1 RP")
                relations[interest] += 1
                #put code here to start the school_quest
    else:
        userTime = input("Do You seek time with your interest? (y/n) ")
        if userTime == "y":
            printSlow(f"You find yourself near {interest} a lot.")
            userTalk = input("Do you talk to them? (y/n) ")
            if userTalk == "y":
                converse(interest)
                printSlow("You two have a lot in common.\n+7 RP")
                relations[interest] += 7
                #put code here to start the school_quest
            else:
                printSlow(f"{interest} finds it weird that you just stand near them.\n-5RP")
                converse(interest)
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
def latterDate(interest):
    global playerEgo
    global playerBread
    global playerBag
    global relations
    playerDate = input(f"Where do you want to ask {interest} to go out to? (restaurant/park/nowhere) ")
    if playerDate == "restaurant":
        printSlow(f"You now are at {random.choice('Coney Island,Bob Evans,Applebees,Chillis,McDonalds'.split(','))}.")
        playerRude = input("After a 15 minute wait, the staff brings you the wrong meal. You ordered the cheeseburger and they brought you nothing at all, as you are still waiting.\nThe waitress comes back around and asks how everything is going. Do you let her have it? (y/n) ")
        converse(interest)
        if playerRude == "y":
            converse(interest)
            printSlow(f"{interest} thinks less of you because the waitress was only 12 years old (it's a family business). {interest} then 'remembers' that they left their wallet in the car. Which is at their home because you drove them here and you have to pick up the tab.\n-15 RP\n-40 dollars")
            playerEgo -= 1
            playerBread -= 40
            if playerBread < 0:
                printSlow(f"You didn't have enough money, but luckily {interest} spotted you the rest..")
                relations[interest] -= -playerBread
                playerBread=0
            relations[interest] -= 15
            backInBlood(interest)
            return
        else:
            converse(interest)
            printSlow(f"{interest} had a fun time, and found it to be a relaxing evening. You two split the bill.\n+10 RP\n-20 dollars")
            playerEgo += 8
            playerBread -= 20
            if playerBread < 0:
                printSlow(f"You didn't have enough money, but luckily {interest} spotted you the rest..")
                relations[interest] -= -playerBread
                playerBread=0
            relations[interest] += 10
    elif playerDate=='park':
        converse(interest)
        printSlow(f"{interest} had a fun time at {random.choice('the state fair,Cedar Point,Kalahari'.split(','))} and associates you with thrills.\n+15 RP -10 dollars")
        playerEgo += 10
        playerBread -= 10
        if playerBread < 0:
            printSlow(f"You didn't have enough money, but luckily {interest} spotted you the rest..")
            relations[interest] -= -playerBread
            playerBread=0
        relations[interest] += 15
    else:
        printSlow(f"You and {interest} enjoy some time together +4 RP")
    print()
def backInBlood(interest):#the action of getting the RP back in blood
    global playerEgo
    global playerBread
    global playerBag
    global relations
    printSlow(f"Recent events have not left {interest} seeming interested in you.")
    userBuy = input("Do you solve the problem with material things? (y/n) ")
    if userBuy == 'y':
        printSlow("Entering shop.")
        playerBread, playerBag=shop(playerBread, playerBag)
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
    userPush = input("Do you seek further ? (y/n) ")
    if userPush == 'y':
        if playerEgo >= 55:
            printSlow(f'You are strangey confident in future conversations. {interest} respects someone who can talk about themselves for 10 minutes straight.')
            relations[interest] += 5
        else:
            converse(interest)
            printSlow(f"{interest} realizes that you are pretty cringe when considered in a vacuum.")
            relations[interest] -= 3
    else:
        userTalk = input(f'You give {interest} some space. Do you give them more space? (y/n) ')
        if userTalk == 'y':
            printSlow(f'It\'s been a while... {interest} starts to forget the fun date you guys had a while back.')
            relations[interest] -= 3
        else:
            converse(interest)
            printSlow(f'{interest} remembers the fun date you guys had a while back. +3 RP')
            relations[interest] += 3
def love(x):
    return 1/(1+10*(math.exp(-0.055*x)))
def like(x):
    return (2/math.pi)*(math.atan(x/14))
def finale(interest):
    printSlow(f"Today is the day. You will finally confess to {interest}")
    converse(interest)
    relationship = relations[interest]
    chance = love(relationship)
    if chance>random.random():
        printSlow("They...",100)
        printSlow("feel the same way!")
        converse(interest)
        return True
    else:
        printSlow("They...",100)
        printSlow("don't feel the same way..")
        converse(interest)
        return False
def converse(interest):
    key=interest.encode()+b':'
    with open('sources.txt','rb') as f:
        text = f.readlines()
        for i in wordList:
            if i == key:
                input(i)
        .decode('utf-8').lower()
        f.close()
    printSlow(f'{interest}: '+Markov(wordList))
def appraise(num):
    boundaries=[9,29,75]
    boundaries.append(num)
    boundaries.sort()
    indice=boundaries.index(num)
    statuses="doesn't like you,is not that familiar with you,is friends with you,is fond of you".split(',')
    return statuses[indice]

def gameOver():
    show(f"Stats -\nInterest:{interest}\nRelation Points: {relations[interest]}, Net Worth:{playerBread}, Possessions:{playerBag}", 40)
    exit()
print(', '.join(possibleInterests))
interest = input("Enter in a name to select your crush, or i to view info on an interest: ")
while interest not in possibleInterests:
    if interest == 'i':
        try:
            tempInterest=input("Type out a name to display info on them: ")
            show(info[tempInterest[0].upper()+tempInterest[1:]], 58)
        except KeyError:
            pass
        finally:
            interest = input("Enter in a name to select your crush, or i to view info on an interest: ")
    elif interest[0].upper()+interest[1:] not in possibleInterests:
        interest = input("Select someone from the list: ")
    else:
        interest = interest[0].upper()+interest[1:]
    
show("Welcome to Haganai! (or BWTGS, or \"I don't have many friends\") Haganai is a text based dating game where you try to win over non reciprocating lovers, ranging from high schoolers to ancient Greek philosophers. Actually, those are the only two options... Anyways the goal of the game is to get one of them to like you back. You can talk to them, shop, and even give them gifts. However, gifting is not an aboslute way to someones heart >:). Fondness is quantifies by Relationship Points (rp!). The more rp, the more your inscrutable LOYL likes you!",100)#information dump
print(f'You have a crush on {interest}, and {interest} {appraise(relations[interest])}')
times=0
dates=0
while 1:
    choices=f'''\nEnter s to go shopping
Enter c to talk to {interest}
Enter g to gift {interest}
Enter a to appraise your relationship'''
    print(choices,end='')
    if times > 3:
        print(f'\nEnter f to confess to {interest}')
    else:
        print()
    opt = input("").lower()
    if opt == 's':
        playerBread, playerBag = shop(playerBread, playerBag)
        print(f"After shopping, {flex(playerBread, playerBag)}")
    elif opt == 'c':
        print(f"You talk to {interest}.")
        converse(interest)
        positive = like(relations[interest])>random.random()
        rpChange=[-1,1][positive]*random.choice(range(1,5))
        print(f"\nConversation with {interest} went {['rough','smooth'][positive]}. {['','+'][positive]}{rpChange} rp!")
        relations[interest]+=rpChange
        playerEgo+=rpChange
        if positive:
            date=input(f"Do you want to on an outing with {interest}? (y/n): ")
            if date=='y' and dates==0:
                dates+=1
                firstDate(interest)
            elif date=='y' and dates>0:
                latterDate(interest)
    elif opt == 'g':
        print(f"You have {[', '.join([str(i)+' (x'+str(playerBag.count(i))+')' for i in set(playerBag)]),'nothing'][playerBag==[]]}")
        gift = input(f"What do you want to give {interest}? (\"nothing\" to exit): ")
        if gift != 'nothing':
            if gift in playerBag:
                playerBag.remove(gift)
                rpChange=random.choice(range(10))
                converse(interest)
                print(f"{interest}{[' acts like they',''][rpChange>0]} appreciated the {gift}{['...','!'][rpChange>0]} +{rpChange} rp{['.','!'][rpChange>0]}")
                relations[interest]+=rpChange
                playerEgo-=rpChange
            else:
                print("You do not have",gift)
    elif opt =='a':
        printSlow(f'I think {interest} {appraise(relations[interest])}.')
    elif opt == 'f' and times>3:
        confess=input('Continue? (y/n)')
        if confess=='y':
            pulled=finale(interest)
            if pulled:
                print(f"You and {interest} live happily ever after! What a good ending.")
                gameOver()
            else:
                printSlow(f"You fumbled {interest} bad...",100)
                print('Better luck next time')
                gameOver()
    if playerEgo<=0:
        printSlow(f"You lost all of your ego.. You have no change with {interest} anymore\nGAME OVER",100)
        gameOver()
    times+=1
