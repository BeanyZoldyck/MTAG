#This is a freestlye by yah boy Chuka

def displayItems(offSet):
    print('\n')
    for i in enumerate(items[offSet:]):
        print(i[0]+offSet+1,i[1])

def displaySingle():
    userItem=int(input("Enter a number to select an item: "))-1
    print(f'{descriptions[userItem]}\n{items[userItem]} costs ${prices[userItem]}.')
    
def flex(playerMoney, inventory):
    print(f"Your net worth is ${playerMoney} and you have {[', '.join([str(i)+' (x'+str(inventory.count(i))+')' for i in set(inventory)]),'nothing'][inventory==[]]}")

def buyItem(playerMoney, inventory):
    userItem=int(input("Enter a number to select an item to buy: "))-1
    if playerMoney >= prices[userItem]:
        inventory.append(items[userItem])
        print(f"You bought {items[userItem]} for {prices[userItem]}. Your new balance is ${playerMoney-prices[userItem]}")
        return playerMoney-prices[userItem]
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
        print("You do not have",product)
        return playerMoney
if __name__ == '__main__':
    playerMoney=40.0
    items='''Head of Cabbage
    Acer Chromebook 311 CB311-10H-41M9, Military Standard (MIL-STD 810G) impact-resistant body; AMD A-Series Dual-Core A4-9120C, 11.6" HD, 4GB DDR4, 64GB eMMC, 802.11ac WiFi 5, Bluetooth 4.2, Chrome OS
    MSI GF65 Thin i7 GTX 1660Ti 8GB/512GB Gaming Laptop
    Nintendo Switch™ Fortnite Wildcat Bundle
    Bose Noise Cancelling Wireless Bluetooth Headphones 700, Black'''.split('\n')
    prices=[2.0,
    179.0,
    1_091.65,
    497.0,
    379.0]
    descriptions='''A literal head of cabbage.
    The Acer Chromebook 311 is the ideal laptop for all ages from the very young upwards. With its safety certification, state-of-the-art low-energy consuming AMD processor, military standard specs and a long battery life, it can stand up to the daily rigors and intense usage of students inside or outside the classroom.
    Play your favorite games in style and with ease with the MSI GF65 Thin i7 GTX 1660Ti 8GB/512GB Gaming Laptop. With dedicated thermal solutions for both the CPU and GPU with up to 6 heat pipes, they work harmoniously by minimizing the heat and maximizing the airflow.
    This bundle includes a uniquely designed Nintendo Switch system with special art on the system and Nintendo Switch dock, a yellow Joy-Con (L) and blue Joy-Con (R), the Fortnite game pre-installed, 2,000 V-Bucks, and a download code for The Wildcat Bundle.
    The unrivaled microphone system in the noise cancelling Bose Headphones 700 adapts to noisy and windy environments so your voice always sounds clear. The design of Bose Headphones 700 has a stainless steel headband and a comfortable fit that’s perfect for all-day listening'''.split('\n')
    inventory=["earbuds"]
    while True:
        displayItems(0)
        option=input("\nEnter 0 to buy item\nEnter 1 to display an item\nEnter 2 to display your possesions\nEnter 3 to sell\nEnter q to quit\n")
        if option=='1':
            displaySingle()
        elif option == '0':
            playerMoney=buyItem(playerMoney, inventory)
        elif option =='2':
            flex(playerMoney, inventory)
        elif option =='3':
            playerMoney=sell(playerMoney, inventory)
        else:
            break
else:
    pass#giftShop variable definition
