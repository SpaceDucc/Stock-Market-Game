import random

day = [1]
hour = [1]
moneygoal = 2000
money = float(0)
ownedstock1 = [0]
price1change = ["="]
ownedstock2 = [0]
price2change = ["="]
ownedstock3 = [0]
price3change = ["="]
ownedstock4 = [0]
price4change = ["="]
ownedstock5 = [0]
price5change = ["="]
ownedstock6 = [0]
price6change = ["="]
ownedstock7 = [0]
price7change = ["="]
ownedstock8 = [0]
price8change = ["="]
stock1price = [150.0] #bluechip
stock2price = [30.0] #crypto
stock3price = [15.0] #medium
confidence3 = [50]
stock4price = [20.0] #medium
confidence4 = [50]
stock5price = [30.0] #medium
confidence5 = [50]
stock6price = [40.0] #medium
confidence6 = [50]
stock7price = [2.0] #penny
stock8price = [3.0] #penny
#1-100 --> 1-25 = low confidence --- 25-75 = average confidence --- 75-100 = high confidence
fakevar1 = [1] #fake variable for penny stocks
goal = 2000
command = 1
game = 0




def lowconpricechange(a,b,c) : 
    lowconrandom = random.randint(1,100)
    if lowconrandom >= 1 and lowconrandom <= 20 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 2
        c[0] = "-"
    elif lowconrandom >= 21 and lowconrandom <= 45 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - 1
        c[0] = "-"
    elif lowconrandom >= 46 and lowconrandom <= 67 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif lowconrandom >= 68 and lowconrandom <= 90 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + 1
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 2
        c[0] = "+"

def mediumconpricechange(a,b,c) :
    mediumconrandom = random.randint(1,100)
    if mediumconrandom >= 1 and mediumconrandom <= 10 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 2
        c[0] = "-"
    elif mediumconrandom >= 11 and mediumconrandom <= 30 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - 1
        c[0] = "-"
    elif mediumconrandom >= 31 and mediumconrandom <= 55 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif mediumconrandom >= 56 and mediumconrandom <= 85 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + 1
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 2
        c[0] = "+"

def highconpricechange(a,b,c) :
    highconrandom = random.randint(1,100)
    if highconrandom >= 1 and highconrandom <= 5 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 2
        c[0] = "-"
    elif highconrandom >= 6 and highconrandom <= 25 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - 1
        c[0] = "-"
    elif highconrandom >= 26 and highconrandom <= 45 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif highconrandom >= 46 and highconrandom <= 80 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + 1
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 2
        c[0] = "+"

def easylowconpricechange(a,b,c) : 
    lowconrandom = random.randint(1,100)
    if lowconrandom >= 1 and lowconrandom <= 20 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 1
        c[0] = "-"
    elif lowconrandom >= 21 and lowconrandom <= 45 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - .5
        c[0] = "-"
    elif lowconrandom >= 46 and lowconrandom <= 67 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif lowconrandom >= 68 and lowconrandom <= 90 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + 1.5
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 3
        c[0] = "+"

def easymediumconpricechange(a,b,c) :
    mediumconrandom = random.randint(1,100)
    if mediumconrandom >= 1 and mediumconrandom <= 10 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 1
        c[0] = "-"
    elif mediumconrandom >= 11 and mediumconrandom <= 30 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - .5
        c[0] = "-"
    elif mediumconrandom >= 31 and mediumconrandom <= 55 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif mediumconrandom >= 56 and mediumconrandom <= 85 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + 1.5
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 3
        c[0] = "+"

def easyhighconpricechange(a,b,c) :
    highconrandom = random.randint(1,100)
    if highconrandom >= 1 and highconrandom <= 5 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 1
        c[0] = "-"
    elif highconrandom >= 6 and highconrandom <= 25 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - .5
        c[0] = "-"
    elif highconrandom >= 26 and highconrandom <= 45 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif highconrandom >= 46 and highconrandom <= 80 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + 1.5
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 3
        c[0] = "+"

def hardlowconpricechange(a,b,c) : 
    lowconrandom = random.randint(1,100)
    if lowconrandom >= 1 and lowconrandom <= 20 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 3
        c[0] = "-"
    elif lowconrandom >= 21 and lowconrandom <= 45 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - 1.5
        c[0] = "-"
    elif lowconrandom >= 46 and lowconrandom <= 67 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif lowconrandom >= 68 and lowconrandom <= 90 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + .5
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 1
        c[0] = "+"

def hardmediumconpricechange(a,b,c) :
    mediumconrandom = random.randint(1,100)
    if mediumconrandom >= 1 and mediumconrandom <= 10 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 3
        c[0] = "-"
    elif mediumconrandom >= 11 and mediumconrandom <= 30 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - 1.5
        c[0] = "-"
    elif mediumconrandom >= 31 and mediumconrandom <= 55 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif mediumconrandom >= 56 and mediumconrandom <= 85 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + .5
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 1
        c[0] = "+"

def hardhighconpricechange(a,b,c) :
    highconrandom = random.randint(1,100)
    if highconrandom >= 1 and highconrandom <= 5 :
        a[0] = float(a[0]) * .9
        b[0] = b[0] - 3
        c[0] = "-"
    elif highconrandom >= 6 and highconrandom <= 25 :
        a[0] = float(a[0]) * .95
        b[0] = b[0] - 1.5
        c[0] = "-"
    elif highconrandom >= 26 and highconrandom <= 45 :
        a[0] = a[0]
        b[0] = b[0]
        c[0] = "="
    elif highconrandom >= 46 and highconrandom <= 80 :
        a[0] = float(a[0]) * 1.05
        b[0] = b[0] + .5
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.10
        b[0] = b[0] + 1
        c[0] = "+"

def bluechippricechange(a,c) :
    bluechiprandom = random.randint(1,100)
    if bluechiprandom >= 1 and bluechiprandom <= 10 :
        a[0] = float(a[0]) * .97
        c[0] = "-"
    elif bluechiprandom >= 11 and bluechiprandom <= 25 :
        a[0] = a[0]
        c[0] = "="
    elif bluechiprandom >= 26 and bluechiprandom <= 65 :
        a[0] = float(a[0]) * 1.02
        c[0] = "+"
    elif bluechiprandom >= 66 and bluechiprandom <= 85 :
        a[0] = float(a[0]) * 1.05
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 1.08
        c[0] = "+"
    
def cryptopricechange(a,c) :
    cryptorandom = random.randint(1,100)
    if cryptorandom >= 1 and cryptorandom <= 5 :
        a[0] = float(a[0]) * .5
        c[0] = "-"
    elif cryptorandom >= 6 and cryptorandom <= 20 :
        a[0] = float(a[0]) * .75
        c[0] = "-"
    elif cryptorandom >= 21 and cryptorandom <= 40 :
        a[0] = float(a[0]) * .9
        c[0] = "-"
    elif cryptorandom >= 41 and cryptorandom <= 60 :
        a[0] = a[0]
        c[0] = "="
    elif cryptorandom >= 61 and cryptorandom <= 80 :
        a[0] = float(a[0]) * 1.10
        c[0] = "+"
    elif cryptorandom >= 81 and cryptorandom <= 95 :
        a[0] = float(a[0]) * 1.50
        c[0] = "+"
    else :
        a[0] = float(a[0]) * 2
        c[0] = "+"

def showprice() :
    stock1priceround = str(round(stock1price[0],2))
    stock1pricelen = len(stock1priceround.split(".")[1])
    if stock1pricelen == 1 :
        print("Price of Glogel stock: $" + str(round(stock1price[0],2)) + "0", price1change[0])
    elif stock1pricelen == 2 :
        print("Price of Glogel stock: $" + str(round(stock1price[0],2)), price1change[0])
    else :
        print("error")

    stock2priceround = str(round(stock2price[0],2))
    stock2pricelen = len(stock2priceround.split(".")[1])
    if stock2pricelen == 1 :
        print("Price of Britcoin stock: $" + str(round(stock2price[0],2)) + "0", price2change[0])
    elif stock2pricelen == 2 :
        print("Price of Britcoin stock: $" + str(round(stock2price[0],2)), price2change[0])
    else :
        print("error")
    
    stock3priceround = str(round(stock3price[0],2))
    stock3pricelen = len(stock3priceround.split(".")[1])
    if stock3pricelen == 1 :
        print("Price of Silicon Mountain stock: $" + str(round(stock3price[0],2)) + "0", price3change[0])
    elif stock3pricelen == 2 :
        print("Price of Silicon Mountain stock: $" + str(round(stock3price[0],2)), price3change[0])
    else :
        print("error")
    
    stock4priceround = str(round(stock4price[0],2))
    stock4pricelen = len(stock4priceround.split(".")[1])
    if stock4pricelen == 1 :
        print("Price of Obelisk of the Dark Gods stock: $" + str(round(stock4price[0],2)) + "0", price4change[0])
    elif stock4pricelen == 2 :
        print("Price of Obelisk of the Dark Gods stock: $" + str(round(stock4price[0],2)), price4change[0])
    else :
        print("error")
    
    stock5priceround = str(round(stock5price[0],2))
    stock5pricelen = len(stock5priceround.split(".")[1])
    if stock5pricelen == 1 :
        print("Price of Corka Cola stock: $" + str(round(stock5price[0],2)) + "0", price5change[0])
    elif stock5pricelen == 2 :
        print("Price of Corka Cola stock: $" + str(round(stock5price[0],2)), price5change[0])
    else :
        print("error")

    stock6priceround = str(round(stock6price[0],2))
    stock6pricelen = len(stock6priceround.split(".")[1])
    if stock6pricelen == 1 :
        print("Price of Popsi stock: $" + str(round(stock6price[0],2)) + "0", price6change[0])
    elif stock6pricelen == 2 :
        print("Price of Popsi stock: $" + str(round(stock6price[0],2)), price6change[0])
    else :
        print("error")
    
    stock7priceround = str(round(stock7price[0],2))
    stock7pricelen = len(stock7priceround.split(".")[1])
    if stock7pricelen == 1 :
        print("Price of Super Terrifying Haunted House Emporium stock: $" + str(round(stock7price[0],2)) + "0", price7change[0])
    elif stock7pricelen == 2 :
        print("Price of Super Terrifying Haunted House Emporium stock: $" + str(round(stock7price[0],2)), price7change[0])
    else :
        print("error")
    
    stock8priceround = str(round(stock8price[0],2))
    stock8pricelen = len(stock8priceround.split(".")[1])
    if stock8pricelen == 1 :
        print("Price of Dolphin Rodeo Inc. stock: $" + str(round(stock8price[0],2)) + "0", price8change[0])
    elif stock8pricelen == 2 :
        print("Price of Dolphin Rodeo Inc. stock: $" + str(round(stock8price[0],2)), price8change[0])
    else :
        print("error")

def showowned() :
    print("Owned Glogel stock:", ownedstock1[0])
    print("Owned Britcoin stock:", ownedstock2[0])
    print("Owned Silicon Mountain stock:", ownedstock3[0])
    print("Owned Obelisk of the Dark Gods stock:", ownedstock4[0])
    print("Owned corka Cola stock:", ownedstock5[0])
    print("Owned Popsi stock:", ownedstock6[0])
    print("Owned Super Terrifying Haunted House Emporium stock:", ownedstock7[0])
    print("Owned Dolphin Rodeo Inc. stock:", ownedstock8[0])

def showwallet() :
    global money
    print("You have $" + str(round(money,2)))

def stockhelp() :
    print("You want to buy and sell stock at the correct times in order to make the most money. You do this using the different commands.")
    print("'buy' allows you to buy stocks, and 'sell' allows you to sell the your stocks.")
    print("'price' lets you see the prices of the stocks, 'owned' lets you see how much of each stock you own, 'money' lets you see how much money you have.")
    print("'end' will end the hour you are on and change the prices of the stocks, and on hour 12, the day will roll over and prices will change more signifigantly, you can see the time with the 'time' command.")

def buy() :
    global money
    mathmoney = 0
    pickstock = 0
    purchacestock = 0
    whatstock = 0
    howmuch = 0
    fakevar3 = 0
    while pickstock == 0 :
        whatstock = input("What Stock Do you want to buy?(Glogel, Britcoin, Silicon, Obelisk, Corka Cola, Popsi, Haunted House, Dolphin):")
        if whatstock.lower() == "glogel" or whatstock.lower() == "britcoin" or whatstock.lower() == "silicon" or whatstock.lower() == "obelisk" or whatstock.lower() == "corka cola" or whatstock.lower() == "popsi" or whatstock.lower() == "haunted house" or whatstock.lower() == "dolphin" :
            pickstock = 1
        else :
            print("That is not a stock")
    while purchacestock == 0 :
        if whatstock.lower() == "glogel" :
            howmuch = int(input("how many Glogel stock do you want to buy?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid number")
                    howmuch = int(input("how many Glogel stock do you want to buy?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Glogel stock do you want to buy?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock1price[0]) * howmuch
            if float(mathmoney) > money :
                print("You do not have enough money")
            else :
                ownedstock1[0] = ownedstock1[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "britcoin" :
            howmuch = int(input("how many Britcoin stock do you want to buy?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Britcoin stock do you want to buy?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Britcoin stock do you want to buy?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock2price[0]) * howmuch
            if float(mathmoney) > money :
                print("You do not have enough money")
            else :
                ownedstock2[0] = ownedstock2[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "silicon" :
            howmuch = int(input("how many Silicon Mountain stock do you want to buy?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Silicon Mountain stock do you want to buy?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Silicon Mountain stock do you want to buy?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock3price[0]) * howmuch
            if float(mathmoney) > money :
                print("You do not have enough money")
            else :
                ownedstock3[0] = ownedstock3[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "obelisk" :
            howmuch = int(input("how many Obelisk of the Dark Gods stock do you want to buy?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Obelisk of the Dark Gods stock do you want to buy?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Obelisk of the Dark Gods stock do you want to buy?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock4price[0]) * howmuch
            if float(mathmoney) > money :
                print("You do not have enough money")
            else :
                ownedstock4[0] = ownedstock4[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "corka cola" :
            howmuch = int(input("how many Corka Cola stock do you want to buy?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Corka Cola stock do you want to buy?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Corka Cola stock do you want to buy?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock5price[0]) * howmuch
            if float(mathmoney) > money :
                print("You do not have enough money")
            else :
                ownedstock5[0] = ownedstock5[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "popsi" :
            howmuch = int(input("how many Popsi stock do you want to buy?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Popsi stock do you want to buy?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Popsi stock do you want to buy?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock6price[0]) * howmuch
            if float(mathmoney) > money :
                print("You do not have enough money")
            else :
                ownedstock6[0] = ownedstock6[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "haunted house" :
            howmuch = int(input("how many Super Terrifying Haunted House Emporium stock do you want to buy?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Super Terrifying Haunted House Emporium stock do you want to buy?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Super Terrifying Haunted House Emporium stock do you want to buy?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock7price[0]) * howmuch
            if float(mathmoney) > money :
                print("You do not have enough money")
            else :
                ownedstock7[0] = ownedstock7[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        elif whatstock.lower() == "dolphin" :
            howmuch = int(input("how many Dolphin Rodeo Inc. stock do you want to buy?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Dolphin Rodeo Inc. stock do you want to buy?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Dolphin Rodeo Inc. stock do you want to buy?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock8price[0]) * howmuch
            if float(mathmoney) > money :
                print("You do not have enough money")
            else :
                ownedstock8[0] = ownedstock8[0] + howmuch
                money = money - mathmoney
                purchacestock = 1

        else :
            print("[THIS SHOULDN'T HAPPEN]")

def sell() :
    global money
    mathmoney = 0
    pickstock = 0
    sellstock = 0
    whatstock = 0
    howmuch = 0
    fakevar3 = 0
    while pickstock == 0 :
        whatstock = input("What Stock Do you want to sell?(Glogel, Britcoin, Silicon, Obelisk, Corka Cola, Popsi, Haunted House, Dolphin):")
        if whatstock.lower() == "glogel" or whatstock.lower() == "britcoin" or whatstock.lower() == "silicon" or whatstock.lower() == "obelisk" or whatstock.lower() == "corka cola" or whatstock.lower() == "popsi" or whatstock.lower() == "haunted house" or whatstock.lower() == "dolphin" :
            pickstock = 1
        else :
            print("That is not a stock")
    
    while sellstock == 0 :
        if whatstock.lower() == "glogel" :
            howmuch = int(input("how many Glogel stock do you want to sell?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Glogel stock do you want to sell?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Glogel stock do you want to sell?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock1price[0]) * howmuch
            if ownedstock1[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock1[0] = ownedstock1[0] - howmuch
                money = money + float(mathmoney)
                sellstock = 1

        if whatstock.lower() == "britcoin" :
            howmuch = int(input("how many Britcoin stock do you want to sell?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Britcoin stock do you want to sell?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Britcoin stock do you want to sell?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock2price[0]) * howmuch
            if ownedstock2[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock2[0] = ownedstock2[0] - howmuch
                money = money + float(mathmoney)
                sellstock = 1
        
        if whatstock.lower() == "silicon" :
            howmuch = int(input("how many Silicon Mountain stock do you want to sell?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Silicon Mountain stock do you want to sell?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Silicon Mountain stock do you want to sell?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock3price[0]) * howmuch
            if ownedstock3[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock3[0] = ownedstock3[0] - howmuch
                money = money + float(mathmoney)
                sellstock = 1

        if whatstock.lower() == "obelisk" :
            howmuch = int(input("how many Obelisk of the Dark Gods stock do you want to sell?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Obelisk of the Dark Gods stock do you want to sell?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Obelisk of the Dark Gods stock do you want to sell?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock4price[0]) * howmuch
            if ownedstock4[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock4[0] = ownedstock4[0] - howmuch
                money = money + float(mathmoney)
                sellstock = 1

        if whatstock.lower() == "corka cola" :
            howmuch = int(input("how many Corka Cola stock do you want to sell?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Corka Cola stock do you want to sell?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Corka Cola stock do you want to sell?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock5price[0]) * howmuch
            if ownedstock5[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock5[0] = ownedstock5[0] - howmuch
                money = money + float(mathmoney)
                sellstock = 1

        if whatstock.lower() == "popsi" :
            howmuch = int(input("how many Popsi stock do you want to sell?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Popsi stock do you want to sell?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Popsi stock do you want to sell?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock6price[0]) * howmuch
            if ownedstock6[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock6[0] = ownedstock6[0] - howmuch
                money = money + float(mathmoney)
                sellstock = 1

        if whatstock.lower() == "haunted house" :
            howmuch = int(input("how many Super Terrifying Haunted House Emporium stock do you want to sell?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Super Terrifying Haunted House Emporium stock do you want to sell?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Super Terrifying Haunted House Emporium stock do you want to sell?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock7price[0]) * howmuch
            if ownedstock7[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock7[0] = ownedstock7[0] - howmuch
                money = money + float(mathmoney)
                sellstock = 1

        if whatstock.lower() == "dolphin" :
            howmuch = int(input("how many Dolphin Rodeo Inc. stock do you want to sell?:"))
            while fakevar3 == 0 :   
                try :
                    howmuch != int(howmuch)
                except :
                    print("invalid stock")
                    howmuch = int(input("how many Dolphin Rodeo Inc. stock do you want to sell?:"))
                if howmuch < int(0) :
                    print("invalid number")
                    howmuch = int(input("how many Dolphin Rodeo Inc. stock do you want to sell?:"))
                else :
                    fakevar3 = 1
            mathmoney = float(stock8price[0]) * howmuch
            if ownedstock8[0] < howmuch :
                print("You do not have enough stock")
            else :
                ownedstock8[0] = ownedstock8[0] - howmuch
                money = money + float(mathmoney)
                sellstock = 1


def incrementtime() :
    global money
    if hour[0] != 12 :
        hour[0] = hour[0] + 1
        bluechippricechange(stock1price, price1change)
        cryptopricechange(stock2price, price2change)
        mediumconpricechange(stock7price, fakevar1, price7change)
        mediumconpricechange(stock8price, fakevar1, price8change)

        if confidence3[0] < 25 :
            lowconpricechange(stock3price, confidence3, price3change)
        elif confidence3[0] > 75 :
            highconpricechange(stock3price, confidence3, price3change)
        else :
            mediumconpricechange(stock3price, confidence3 , price3change)

        if confidence4[0] < 25 :
            lowconpricechange(stock4price, confidence4, price4change)
        elif confidence4[0] > 75 :
            highconpricechange(stock4price, confidence4, price4change)
        else :
            mediumconpricechange(stock4price, confidence4, price4change)

        if confidence5[0] < 25 :
            lowconpricechange(stock5price, confidence5, price5change)
        elif confidence5[0] > 75 :
            highconpricechange(stock5price, confidence5, price5change)
        else :
            mediumconpricechange(stock5price, confidence5, price5change)

        if confidence6[0] < 25 :
            lowconpricechange(stock6price, confidence6, price6change)
        elif confidence6[0] > 75 :
            highconpricechange(stock6price, confidence6, price6change)
        else :
            mediumconpricechange(stock6price, confidence6, price6change)

    else :
        day[0] = day[0] + 1
        fakevar2 = 0
        money = money + 20
        while fakevar2 != 5 :
            bluechippricechange(stock1price, price1change)
            cryptopricechange(stock2price, price2change)
            mediumconpricechange(stock7price, fakevar1, price7change)
            mediumconpricechange(stock8price, fakevar1, price8change)

            if confidence3[0] < 25 :
                lowconpricechange(stock3price, confidence3, price3change)
            elif confidence3[0] > 75 :
                highconpricechange(stock3price, confidence3, price3change)
            else :
                mediumconpricechange(stock3price, confidence3, price3change)

            if confidence4[0] < 25 :
                lowconpricechange(stock4price, confidence4, price4change)
            elif confidence4[0] > 75 :
                highconpricechange(stock4price, confidence4, price4change)
            else :
                mediumconpricechange(stock4price, confidence4, price4change)

            if confidence5[0] < 25 :
                lowconpricechange(stock5price, confidence5, price5change)
            elif confidence5[0] > 75 :
                highconpricechange(stock5price, confidence5, price5change)
            else :
                mediumconpricechange(stock5price, confidence5, price5change)

            if confidence6[0] < 25 :
                lowconpricechange(stock6price, confidence6, price6change)
            elif confidence6[0] > 75 :
                highconpricechange(stock6price, confidence6, price6change)
            else :
                mediumconpricechange(stock6price, confidence6, price6change)

            fakevar2 = fakevar2 + 1
        hour[0] = 1

def easyincrementtime() :
    global money
    if hour[0] != 12 :
        hour[0] = hour[0] + 1
        bluechippricechange(stock1price, price1change)
        cryptopricechange(stock2price, price2change)
        mediumconpricechange(stock7price, fakevar1, price7change)
        mediumconpricechange(stock8price, fakevar1, price8change)

        if confidence3[0] < 25 :
            easylowconpricechange(stock3price, confidence3, price3change)
        elif confidence3[0] > 75 :
            easyhighconpricechange(stock3price, confidence3, price3change)
        else :
            easymediumconpricechange(stock3price, confidence3, price3change)

        if confidence4[0] < 25 :
            easylowconpricechange(stock4price, confidence4, price4change)
        elif confidence4[0] > 75 :
            easyhighconpricechange(stock4price, confidence4, price4change)
        else :
            easymediumconpricechange(stock4price, confidence4, price4change)

        if confidence5[0] < 25 :
            easylowconpricechange(stock5price, confidence5, price5change)
        elif confidence5[0] > 75 :
            easyhighconpricechange(stock5price, confidence5, price5change)
        else :
            easymediumconpricechange(stock5price, confidence5, price5change)

        if confidence6[0] < 25 :
            easylowconpricechange(stock6price, confidence6, price6change)
        elif confidence6[0] > 75 :
            easyhighconpricechange(stock6price, confidence6, price6change)
        else :
            easymediumconpricechange(stock6price, confidence6, price6change)

    else :
        day[0] = day[0] + 1
        fakevar2 = 0
        money = money + 40
        while fakevar2 != 5 :
            bluechippricechange(stock1price, price1change)
            cryptopricechange(stock2price, price2change)
            mediumconpricechange(stock7price, fakevar1, price7change)
            mediumconpricechange(stock8price, fakevar1, price8change)

            if confidence3[0] < 25 :
                easylowconpricechange(stock3price, confidence3, price3change)
            elif confidence3[0] > 75 :
                easyhighconpricechange(stock3price, confidence3, price3change)
            else :
                easymediumconpricechange(stock3price, confidence3, price3change)

            if confidence4[0] < 25 :
                easylowconpricechange(stock4price, confidence4, price4change)
            elif confidence4[0] > 75 :
                easyhighconpricechange(stock4price, confidence4, price4change)
            else :
                easymediumconpricechange(stock4price, confidence4, price4change)

            if confidence5[0] < 25 :
                easylowconpricechange(stock5price, confidence5, price5change)
            elif confidence5[0] > 75 :
                easyhighconpricechange(stock5price, confidence5, price5change)
            else :
                easymediumconpricechange(stock5price, confidence5, price5change)

            if confidence6[0] < 25 :
                easylowconpricechange(stock6price, confidence6, price6change)
            elif confidence6[0] > 75 :
                easyhighconpricechange(stock6price, confidence6, price6change)
            else :
                easymediumconpricechange(stock6price, confidence6, price6change)

            fakevar2 = fakevar2 + 1
        hour[0] = 1

def hardincrementtime() :
    global money
    if hour[0] != 12 :
        hour[0] = hour[0] + 1
        bluechippricechange(stock1price, price1change)
        cryptopricechange(stock2price, price2change)
        mediumconpricechange(stock7price, fakevar1, price7change)
        mediumconpricechange(stock8price, fakevar1, price8change)

        if confidence3[0] < 25 :
            hardlowconpricechange(stock3price, confidence3, price3change)
        elif confidence3[0] > 75 :
            hardhighconpricechange(stock3price, confidence3, price3change)
        else :
            hardmediumconpricechange(stock3price, confidence3, price3change)

        if confidence4[0] < 25 :
            hardlowconpricechange(stock4price, confidence4, price4change)
        elif confidence4[0] > 75 :
            hardhighconpricechange(stock4price, confidence4, price4change)
        else :
            hardmediumconpricechange(stock4price, confidence4, price4change)

        if confidence5[0] < 25 :
            hardlowconpricechange(stock5price, confidence5, price5change)
        elif confidence5[0] > 75 :
            hardhighconpricechange(stock5price, confidence5, price5change)
        else :
            hardmediumconpricechange(stock5price, confidence5, price5change)

        if confidence6[0] < 25 :
            hardlowconpricechange(stock6price, confidence6, price6change)
        elif confidence6[0] > 75 :
            hardhighconpricechange(stock6price, confidence6, price6change)
        else :
            hardmediumconpricechange(stock6price, confidence6, price6change)

    else :
        day[0] = day[0] + 1
        fakevar2 = 0
        money = money + 10
        while fakevar2 != 5 :
            bluechippricechange(stock1price, price1change)
            cryptopricechange(stock2price, price2change)
            mediumconpricechange(stock7price, fakevar1, price7change)
            mediumconpricechange(stock8price, fakevar1, price8change)

            if confidence3[0] < 25 :
                hardlowconpricechange(stock3price, confidence3, price3change)
            elif confidence3[0] > 75 :
                hardhighconpricechange(stock3price, confidence3, price3change)
            else :
                hardmediumconpricechange(stock3price, confidence3, price3change)

            if confidence4[0] < 25 :
                hardlowconpricechange(stock4price, confidence4, price4change)
            elif confidence4[0] > 75 :
                hardhighconpricechange(stock4price, confidence4, price4change)
            else :
                hardmediumconpricechange(stock4price, confidence4, price4change)

            if confidence5[0] < 25 :
                hardlowconpricechange(stock5price, confidence5, price5change)
            elif confidence5[0] > 75 :
                hardhighconpricechange(stock5price, confidence5, price5change)
            else :
                hardmediumconpricechange(stock5price, confidence5, price5change)

            if confidence6[0] < 25 :
                hardlowconpricechange(stock6price, confidence6, price6change)
            elif confidence6[0] > 75 :
                hardhighconpricechange(stock6price, confidence6, price6change)
            else :
                hardmediumconpricechange(stock6price, confidence6, price6change)

            fakevar2 = fakevar2 + 1
        hour[0] = 1

def whattime() :
    print("day", day[0], "hour", hour[0])

def whatcommand() :
    command = 1
    command = input("what do you want to do?(buy,sell,price,owned,money,end,time,help)")
    print(command)
    while command.lower() != "buy" and command.lower() != "sell" and command.lower() != "price" and command.lower() != "owned" and command.lower() != "end" and command.lower() != "help" and command.lower() != "money" and command.lower() != "time" : #add more?
        if command.lower() != "buy" and command.lower() != "sell" and command.lower() != "price" and command.lower() != "owned" and command.lower() != "end" and command.lower() != "help" and command.lower() != "money" and command.lower() != "time" : #if add in above line add here
            print("invalid command")
            command = input("what do you want to do?(buy,sell,price,owned,money,end,time,help)")
        else :
            break
    if command.lower() == "buy" :
        buy()
    elif command.lower() == "sell" :
        sell()
    elif command.lower() == "price" :
        showprice()
    elif command.lower() == "owned" :
        showowned()
    elif command.lower() == "money" :
        showwallet()
    elif command.lower() == "end" :
        incrementtime()
    elif command.lower() == "time" :
        whattime()
    else : #help command
        stockhelp()

def easywhatcommand() :
    command = 1
    command = input("what do you want to do?(buy,sell,price,owned,money,end,time,help)")
    print(command)
    while command.lower() != "buy" and command.lower() != "sell" and command.lower() != "price" and command.lower() != "owned" and command.lower() != "end" and command.lower() != "help" and command.lower() != "money" and command.lower() != "time" : #add more?
        if command.lower() != "buy" and command.lower() != "sell" and command.lower() != "price" and command.lower() != "owned" and command.lower() != "end" and command.lower() != "help" and command.lower() != "money" and command.lower() != "time" : #if add in above line add here
            print("invalid command")
            command = input("what do you want to do?(buy,sell,price,owned,money,end,time,help)")
        else :
            break
    if command.lower() == "buy" :
        buy()
    elif command.lower() == "sell" :
        sell()
    elif command.lower() == "price" :
        showprice()
    elif command.lower() == "owned" :
        showowned()
    elif command.lower() == "money" :
        showwallet()
    elif command.lower() == "end" :
        easyincrementtime()
    elif command.lower() == "time" :
        whattime()
    else : #help command
        stockhelp()

def hardwhatcommand() :
    command = 1
    command = input("what do you want to do?(buy,sell,price,owned,money,end,time,help)")
    print(command)
    while command.lower() != "buy" and command.lower() != "sell" and command.lower() != "price" and command.lower() != "owned" and command.lower() != "end" and command.lower() != "help" and command.lower() != "money" and command.lower() != "time" : #add more?
        if command.lower() != "buy" and command.lower() != "sell" and command.lower() != "price" and command.lower() != "owned" and command.lower() != "end" and command.lower() != "help" and command.lower() != "money" and command.lower() != "time" : #if add in above line add here
            print("invalid command")
            command = input("what do you want to do?(buy,sell,price,owned,money,end,time,help)")
        else :
            break
    if command.lower() == "buy" :
        buy()
    elif command.lower() == "sell" :
        sell()
    elif command.lower() == "price" :
        showprice()
    elif command.lower() == "owned" :
        showowned()
    elif command.lower() == "money" :
        showwallet()
    elif command.lower() == "end" :
        hardincrementtime()
    elif command.lower() == "time" :
        whattime()
    else : #help command
        stockhelp()

def easymodegame() :
    game = 1
    global money
    moneygoal = int(1000)
    print("Welcome to the easy difficulty mode of MSMG by SPDC Technologies. In order to win, you have to get $1000. In order to start, run the 'help' command.")
    while game == 1:
        if money < moneygoal :
            easywhatcommand()
        else :
            print("you win")
            game = 0

def mediummodegame() :
    game = 1
    global money
    moneygoal = int(2000)
    print("Welcome to the medium difficulty mode of MSMG by SPDC Technologies. In order to win, you have to get $2000. In order to start, run the 'help' command")
    while game == 1:
        if money < moneygoal :
            whatcommand()
        else :
            print("you win")
            game = 0


def hardmodegame() :
    game = 1
    global money
    moneygoal = int(4000)
    print("Welcome to the medium difficulty mode of MSMG by SPDC Technologies. In order to win, you have to get $4000. In order to start, run the 'help' command")
    while game == 1:
        if money < moneygoal :
            hardwhatcommand()
        else :
            print("you win")
            game = 0
    
def startgame() :
    global money
    global game
    global goal
    goal = 0
    while game != 1 :
        print("Welcome to The Miniture Stock Market Game by SPDC Technologies.")
        difficulty = input("Please select a difficulty(easy, medium, or hard):")
        if difficulty.lower() == "easy" :
            money = 300
            easymodegame()
            game = 1
        elif difficulty.lower() == "medium" :
            money = 200
            mediummodegame()
            game = 1
        elif difficulty.lower() == "hard" :
            money = 100
            hardmodegame()
            game = 1
        else :
            print("invalid difficulty")

startgame()