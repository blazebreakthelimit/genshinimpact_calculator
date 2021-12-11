# def main ():
#     username = str(input("Please enter your name: "))
#     usernamelength = len(username)
# primo = 90
# genesis = 10
# amonth = 30    
# def function(usernamelength):
#     if usernamelength > 20 or usernamelength < 3:
#         print("Invalid name. Exiting program...")
#     else:
#         userid = input("Please enter your user ID: ")
#         useridlength = len(userid)
#         if useridlength > 9 or useridlength < 9:
#             print("Invalid user ID. Exiting program...")


from os import name

items = []
prices = []
new_item = ""
new_price = ""
primo = 90
genesis = 10
amonth = 30 
username = ""

def main():
    menu_input = ""
    print("=================================")
    print("Welcome to Daniel's Gaming Store!")
    print("=================================")
    print()
    username = input("Please enter your username: ")
    print("=============================================")
    print(f"Welcome to Daniel's Gaming Store, {username}")
    print("=============================================")
    print()
    while menu_input != "quit":
        print("========================================")
        print("1. Add item")
        print("2. View Cart")
        print("3. Remove Item")
        print("4. Calculate Primogems per Month")
        print("5. Checkout")
        print("6. Quit")
        print("========================================")
        menu_input = input("Please select one of the following menu:")
        if menu_input == "1":
            AddItem()
            print()
        elif menu_input == "2":
            ViewCart()
            print()
        elif menu_input == "3":
            removeItems()
            print()
        elif menu_input == "4":
            calculation()
            print()
        elif menu_input == "5":
            payment()
            print()
        elif menu_input == "6":
            print("Thank You, Goodbye.")
            break
        elif menu_input == "7":
            egg()
        else:
            print("Error. Please enter the number on the menu")
            print()
            
def calculation():
    buy = int(input("How many month(s) do you want to calculate?: "))
    if buy > 12 or buy < 1:
        print("Invalid amount of months. Please try again")
    else:
        totalprimo = (primo + genesis) * amonth * buy
        print(f"Hello {username}. You'll get {totalprimo} primogem(s) for buying {buy} month(s) of Blessing of The Welkin Moon")

def AddItem ():
    f = open("list_primo_price.txt", "r")
    print(f.read())
    new_item = input("What item would you like to add? ")
    new_price = float(input(f"Please enter the price to confirm '{new_item}'? $"))
    items.append(new_item)
    prices.append(new_price)
    print(f"{new_item} has been added to the cart.")
    print()

def ViewCart():
    print("Your order contains: ")
    # count = 0
    i =+ 1
    for i in range (len(items)):
         item = items[i]
         price = prices[i]
        #  count = count + 1
         print(f"{i}. {item} - ${price}")

def removeItems ():
    remove_items = input("Which item would you like to remove? ")
    try:
        if len(remove_items) >= 0:
            del items[int(remove_items)]
            del prices[int(remove_items)]
            print("Item Removed.")
    except:
        print("Sorry, that is not a valid item number.")

def payment():
    print("1. PayPal")
    print("2. VISA")
    print("3. Mastercard")
    print("4. Carrier")
    payments = str(input("What payment methods do you want? "))
    if payments == "1":
        paypal = input("Please input your PayPal email: ")
        print(f"Thanks for purchasing. {paypal} on PayPal has been charged ${sum(prices):.2f} \n")
    elif payments == "2" or payments == "3":
        cardnum = int(input("Please input your card number: "))
        cardcvv = int(input("Please input your CVV number: "))
        while True:
            try:
                cardcvvstr = str(cardcvv)
                if (len (cardcvvstr) >= 3 or (cardcvvstr) <= 3):
                    raise ValueError()
                    break
            except ValueError:
                print (f'Thanks for purchasing. Your credit card has been charged ${sum(prices):.2f} \n')
            else:
                print ('Invalid Input')
    elif payments == "4":
        carrier = str(input("What carrier do you use? \n 1. T-Mobile \n 2. Verizon \n 3. AT&T \n : "))
        phonenum = input("Please enter your phone number with your area code: ")
        print(f"Thank you for purchasing. {phonenum} on your carrier service has been charged ${sum(prices):.2f} \n")
        
def egg():
    print("hi")
    

# print("=================================")
# print("Welcome to Daniel's Gaming Store!")
# print("=================================")
# print()
# username = input("Please enter your username: ")
# print("=============================================")
# print(f"Welcome to Daniel's Gaming Store, {username}")
# print("=============================================")
# print()
# while menu_input != "quit":
#     print("========================================")
#     print("1. Add item")
#     print("2. View Cart")
#     print("3. Remove Item")
#     print("4. Calculate Primogems per Month")
#     print("5. Checkout")
#     print("6. Quit")
#     print("========================================")
#     menu_input = input("Please select one of the following menu:")
#     if menu_input == "1":
#         AddItem()
#         print()
#     elif menu_input == "2":
#         ViewCart()
#         print()
#     elif menu_input == "3":
#         removeItems()
#         print()
#     elif menu_input == "4":
#         calculation()
#         print()
#     elif menu_input == "5":
#         payment()
#         print()
#     elif menu_input == "6":
#         print("Thank You, Goodbye.")
#         break
#     elif menu_input == "7":
#         egg()
#     else:
#         print("Error. Please enter the number on the menu")
#         print()

main()
