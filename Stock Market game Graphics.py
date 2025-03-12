import random
from graphics import *

day = [1]
hour = [1]
moneygoal = 2000
money = float(0)
dummystock = [0]
dummystockprice = [0]
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
fakevar2 = 0
fakevar3 = 0
fakevar4 = 0
fakevar5 = 0
fakevar6 = 0
fakevar7 = 0
howmuch = 0
purchacestock = 0
mathmoney = 0
goal = 2000
command = 1
game = 0
win1 = GraphWin("MSMG", 1200, 700)

buypt1 = Point(50,50)
buypt2 = Point(250,150)
buyrec = Rectangle(buypt1,buypt2)
buyrec.setFill(color_rgb(0,0,0))

buypt3 = Point(150,100)
buytext = Text(buypt3, "Buy Stock")
buytext.setTextColor(color_rgb(255,255,255))
buytext.setSize(24)

sellpt1 = Point(50,200)
sellpt2 = Point(250,300)
sellrec = Rectangle(sellpt1,sellpt2)
sellrec.setFill(color_rgb(0,0,0))

sellpt3 = Point(150,250)
selltext = Text(sellpt3, "Sell Stock")
selltext.setTextColor(color_rgb(255,255,255))
selltext.setSize(24)

statuspt1 = Point(50,350)
statuspt2 = Point(250,450)
statusrec = Rectangle(statuspt1,statuspt2)
statusrec.setFill(color_rgb(0,0,0))

statuspt3 = Point(150,400)
statustext = Text(statuspt3, "Information")
statustext.setTextColor(color_rgb(255,255,255))
statustext.setSize(24)

timept1 = Point(50,500)
timept2 = Point(250,600)
timerec = Rectangle(timept1,timept2)
timerec.setFill(color_rgb(0,0,0))

timept3 = Point(150,550)
timetext = Text(timept3, "Next Hour")
timetext.setTextColor(color_rgb(255,255,255))
timetext.setSize(24)

clockpt1 = Point(1000,25)
clockpt2 = Point(1100,75)
clockrec = Rectangle(clockpt1,clockpt2)
clockrec.setFill(color_rgb(0,0,0))

clockpt3 = Point(1050,50)
clocktexttext = ["Day", str(day[0]), "Hour", str(hour[0])]
clocktext = Text(clockpt3, clocktexttext)
clocktext.setTextColor(color_rgb(255,255,255))
clocktext.setSize(12)

moneypt1 = Point(1000,100)
moneypt2 = Point(1100,150)
moneyrec = Rectangle(moneypt1,moneypt2)
moneyrec.setFill(color_rgb(0,0,0))

moneypt3 = Point(1050,125)
moneytexttext = ["$",str(money)]
moneytext = Text(moneypt3, moneytexttext)
moneytext.setTextColor(color_rgb(255,255,255))
moneytext.setSize(16)

stock1pt1 = Point(120,200)
stock1pt2 = Point(320,350)
stock1rec = Rectangle(stock1pt1,stock1pt2)
stock1rec.setFill(color_rgb(0,0,0))

stock1pt3 = Point(220,275)
stock1text = Text(stock1pt3,"Glogel Stock")
stock1text.setTextColor(color_rgb(255,255,255))
stock1text.setSize(24)

stock2pt1 = Point(360,200)
stock2pt2 = Point(560,350)
stock2rec = Rectangle(stock2pt1,stock2pt2)
stock2rec.setFill(color_rgb(0,0,0))

stock2pt3 = Point(460,275)
stock2text = Text(stock2pt3,"Britcoin Stock")
stock2text.setTextColor(color_rgb(255,255,255))
stock2text.setSize(24)

stock3pt1 = Point(620,200)
stock3pt2 = Point(820,350)
stock3rec = Rectangle(stock3pt1,stock3pt2)
stock3rec.setFill(color_rgb(0,0,0))

stock3pt3 = Point(720,245)
stock3text1 = Text(stock3pt3,"Silicon")
stock3text1.setTextColor(color_rgb(255,255,255))
stock3text1.setSize(24)

stock3pt4 = Point(720,275)
stock3text2 = Text(stock3pt4,"Mountain")
stock3text2.setTextColor(color_rgb(255,255,255))
stock3text2.setSize(24)

stock3pt5 = Point(720,305)
stock3text3 = Text(stock3pt5,"Stock")
stock3text3.setTextColor(color_rgb(255,255,255))
stock3text3.setSize(24)

stock4pt1 = Point(880,200)
stock4pt2 = Point(1080,350)
stock4rec = Rectangle(stock4pt1,stock4pt2)
stock4rec.setFill(color_rgb(0,0,0))

stock4pt3 = Point(980,245)
stock4text1 = Text(stock4pt3,"Obelisk of")
stock4text1.setTextColor(color_rgb(255,255,255))
stock4text1.setSize(22)

stock4pt4 = Point(980,275)
stock4text2 = Text(stock4pt4,"the Dark Gods")
stock4text2.setTextColor(color_rgb(255,255,255))
stock4text2.setSize(22)

stock4pt5 = Point(980,305)
stock4text3 = Text(stock4pt5,"Stock")
stock4text3.setTextColor(color_rgb(255,255,255))
stock4text3.setSize(22)

stock5pt1 = Point(120,450)
stock5pt2 = Point(320,600)
stock5rec = Rectangle(stock5pt1,stock5pt2)
stock5rec.setFill(color_rgb(0,0,0))

stock5pt3 = Point(220,525)
stock5text = Text(stock5pt3,"Corka Cola Stock")
stock5text.setTextColor(color_rgb(255,255,255))
stock5text.setSize(18)

stock6pt1 = Point(360,450)
stock6pt2 = Point(560,600)
stock6rec = Rectangle(stock6pt1,stock6pt2)
stock6rec.setFill(color_rgb(0,0,0))

stock6pt3 = Point(460,525)
stock6text = Text(stock6pt3,"Popsi Stock")
stock6text.setTextColor(color_rgb(255,255,255))
stock6text.setSize(24)

stock7pt1 = Point(620,450)
stock7pt2 = Point(820,600)
stock7rec = Rectangle(stock7pt1,stock7pt2)
stock7rec.setFill(color_rgb(0,0,0))

stock7pt3 = Point(720,495)
stock7text1 = Text(stock7pt3,"Super Terrifying")
stock7text1.setTextColor(color_rgb(255,255,255))
stock7text1.setSize(20)

stock7pt4 = Point(720,525)
stock7text2 = Text(stock7pt4,"Haunted House")
stock7text2.setTextColor(color_rgb(255,255,255))
stock7text2.setSize(20)

stock7pt5 = Point(720,555)
stock7text3 = Text(stock7pt5,"Emporium Stock")
stock7text3.setTextColor(color_rgb(255,255,255))
stock7text3.setSize(20)

stock8pt1 = Point(880,450)
stock8pt2 = Point(1080,600)
stock8rec = Rectangle(stock8pt1,stock8pt2)
stock8rec.setFill(color_rgb(0,0,0))

stock8pt3 = Point(980,510)
stock8text1 = Text(stock8pt3,"Dolphin Rodeo")
stock8text1.setTextColor(color_rgb(255,255,255))
stock8text1.setSize(24)

stock8pt4 = Point(980,540)
stock8text2 = Text(stock8pt4,"Inc. Stock")
stock8text2.setTextColor(color_rgb(255,255,255))
stock8text2.setSize(24)

stockamountpt1 = Point(400,250)
stockamountpt2 = Point(800,500)
stockamountrec = Rectangle(stockamountpt1,stockamountpt2)
stockamountrec.setFill(color_rgb(0,0,0))

stockamountpt3 = Point(600,300)
buystockamounttext1 = Text(stockamountpt3, "How many stocks do you wish to buy?")
buystockamounttext1.setTextColor(color_rgb(255,255,255))
buystockamounttext1.setSize(18)

stockamountpt4 = Point(600,400)
stockamountentry = Entry(stockamountpt4,4)
stockamountentry.setTextColor(color_rgb(255,255,255))
stockamountentry.setSize(24)

stockamountpt5 = Point(600,330)
stockamounttext1 = Text(stockamountpt5, "Click to confirm entry")
stockamounttext1.setTextColor(color_rgb(255,255,255))
stockamounttext1.setSize(18)

stockamountpt3 = Point(600,300)
sellstockamounttext1 = Text(stockamountpt3, "How many stocks do you wish to sell?")
sellstockamounttext1.setTextColor(color_rgb(255,255,255))
sellstockamounttext1.setSize(18)

invalidnumberpt1 = Point(600,450)
invalidnumbertext = Text(invalidnumberpt1,"Invalid number,try again")
invalidnumbertext.setTextColor(color_rgb(255,255,255))
invalidnumbertext.setSize(18)

showinfopt1 = Point(100,50)
showinfopt2 = Point(1000,650)
showinforec = Rectangle(showinfopt1, showinfopt2)
showinforec.setFill(color_rgb(0,0,0))

showinfopt3 = Point(550,80)
showinfopt4 = Point(550,155)
showinfopt5 = Point(550,230)
showinfopt6 = Point(550,305)
showinfopt7 = Point(550,390)
showinfopt8 = Point(550,470)
showinfopt9 = Point(550,545)
showinfopt10 = Point(550,620)

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

def showinfo() :
    global showinfopt3
    global showinfopt4
    global showinfopt5
    global showinfopt6
    global showinfopt7
    global showinfopt8
    global showinfopt9
    global showinfopt10
    global showinforec
    global ownedstock1
    global ownedstock2
    global ownedstock3
    global ownedstock4
    global ownedstock5
    global ownedstock6
    global ownedstock7
    global ownedstock8
    global stock1price
    global stock2price
    global stock3price
    global stock4price
    global stock5price
    global stock6price
    global stock7price
    global stock8price
    global price1change
    global price2change
    global price3change
    global price4change
    global price5change
    global price6change
    global price7change
    global price8change

    stock1priceround = str(round(stock1price[0],2))
    stock1pricelen = len(stock1priceround.split(".")[1])
    if stock1pricelen == 1 :
        stock1text = "Glogel stock: $" + str(round(stock1price[0],2)) + "0", price1change[0], "owned:", ownedstock1[0]
    elif stock1pricelen == 2 :
        stock1text = "Glogel stock: $" + str(round(stock1price[0],2)), price1change[0], "owned:", ownedstock1[0]
    else :
        print("error")

    stock2priceround = str(round(stock2price[0],2))
    stock2pricelen = len(stock2priceround.split(".")[1])
    if stock2pricelen == 1 :
        stock2text = "Britcoin stock: $" + str(round(stock2price[0],2)) + "0", price2change[0], "owned:", ownedstock2[0]
    elif stock2pricelen == 2 :
        stock2text = "Britcoin stock: $" + str(round(stock2price[0],2)), price2change[0], "owned:", ownedstock2[0]
    else :
        print("error")
    
    stock3priceround = str(round(stock3price[0],2))
    stock3pricelen = len(stock3priceround.split(".")[1])
    if stock3pricelen == 1 :
        stock3text = "Silicon Mountain stock: $" + str(round(stock3price[0],2)) + "0", price3change[0], "owned:", ownedstock3[0]
    elif stock3pricelen == 2 :
        stock3text = "Silicon Mountain stock: $" + str(round(stock3price[0],2)), price3change[0], "owned:", ownedstock3[0]
    else :
        print("error")
    
    stock4priceround = str(round(stock4price[0],2))
    stock4pricelen = len(stock4priceround.split(".")[1])
    if stock4pricelen == 1 :
        stock4text = "Obelisk of the Dark Gods stock: $" + str(round(stock4price[0],2)) + "0", price4change[0], "owned:", ownedstock4[0]
    elif stock4pricelen == 2 :
        stock4text = "Obelisk of the Dark Gods stock: $" + str(round(stock4price[0],2)), price4change[0], "owned:", ownedstock4[0]
    else :
        print("error")
    
    stock5priceround = str(round(stock5price[0],2))
    stock5pricelen = len(stock5priceround.split(".")[1])
    if stock5pricelen == 1 :
        stock5text = "Corka Cola stock: $" + str(round(stock5price[0],2)) + "0", price5change[0], "owned:", ownedstock5[0]
    elif stock5pricelen == 2 :
        stock5text = "Corka Cola stock: $" + str(round(stock5price[0],2)), price5change[0], "owned:", ownedstock5[0]
    else :
        print("error")

    stock6priceround = str(round(stock6price[0],2))
    stock6pricelen = len(stock6priceround.split(".")[1])
    if stock6pricelen == 1 :
        stock6text = "Popsi stock: $" + str(round(stock6price[0],2)) + "0", price6change[0], "owned:", ownedstock6[0]
    elif stock6pricelen == 2 :
        stock6text = "Popsi stock: $" + str(round(stock6price[0],2)), price6change[0], "owned:", ownedstock6[0]
    else :
        print("error")
    
    stock7priceround = str(round(stock7price[0],2))
    stock7pricelen = len(stock7priceround.split(".")[1])
    if stock7pricelen == 1 :
        stock7text = "Super Terrifying Haunted House Emporium stock: $" + str(round(stock7price[0],2)) + "0", price7change[0], "owned:", ownedstock7[0]
    elif stock7pricelen == 2 :
        stock7text = "Super Terrifying Haunted House Emporium stock: $" + str(round(stock7price[0],2)), price7change[0], "owned:", ownedstock7[0]
    else :
        print("error")
    
    stock8priceround = str(round(stock8price[0],2))
    stock8pricelen = len(stock8priceround.split(".")[1])
    if stock8pricelen == 1 :
        stock8text = "Dolphin Rodeo Inc. stock: $" + str(round(stock8price[0],2)) + "0", price8change[0], "owned:", ownedstock8[0]
    elif stock8pricelen == 2 :
        stock8text = "Dolphin Rodeo Inc. stock: $" + str(round(stock8price[0],2)), price8change[0], "owned:", ownedstock8[0]
    else :
        print("error")

    showinfotext1 = Text(showinfopt3, stock1text)
    showinfotext1.setTextColor(color_rgb(255,255,255))
    showinfotext1.setSize(20)
    showinfotext2 = Text(showinfopt4, stock2text)
    showinfotext2.setTextColor(color_rgb(255,255,255))
    showinfotext2.setSize(20)
    showinfotext3 = Text(showinfopt5, stock3text)
    showinfotext3.setTextColor(color_rgb(255,255,255))
    showinfotext3.setSize(20)
    showinfotext4 = Text(showinfopt6, stock4text)
    showinfotext4.setTextColor(color_rgb(255,255,255))
    showinfotext4.setSize(20)
    showinfotext5 = Text(showinfopt7, stock5text)
    showinfotext5.setTextColor(color_rgb(255,255,255))
    showinfotext5.setSize(20)
    showinfotext6 = Text(showinfopt8, stock6text)
    showinfotext6.setTextColor(color_rgb(255,255,255))
    showinfotext6.setSize(20)
    showinfotext7 = Text(showinfopt9, stock7text)
    showinfotext7.setTextColor(color_rgb(255,255,255))
    showinfotext7.setSize(20)
    showinfotext8 = Text(showinfopt10, stock8text)
    showinfotext8.setTextColor(color_rgb(255,255,255))
    showinfotext8.setSize(20)

    showinforec.draw(win1)
    showinfotext1.draw(win1)
    showinfotext2.draw(win1)
    showinfotext3.draw(win1)
    showinfotext4.draw(win1)
    showinfotext5.draw(win1)
    showinfotext6.draw(win1)
    showinfotext7.draw(win1)
    showinfotext8.draw(win1)

    win1.getMouse()

    showinforec.undraw()
    showinfotext1.undraw()
    showinfotext2.undraw()
    showinfotext3.undraw()
    showinfotext4.undraw()
    showinfotext5.undraw()
    showinfotext6.undraw()
    showinfotext7.undraw()
    showinfotext8.undraw()

    

def buymath(a,b) :
    global mathmoney
    global money
    global howmuch
    global fakevar4
    global fakevar7
    global purchacestock
    global stockamountentry
    global buystockamounttext1
    global stockamounttext1
    global stockamountrec
    global win1
    mathmoney = float(a[0]) * howmuch
    if float(mathmoney) > money :
        fakevar4 = 0
        purchacestock = 0
        fakevar7 = 1
        stockamountentry.undraw()
        buystockamounttext1.undraw()
        stockamounttext1.undraw()
        stockamountrec.undraw()
    else :
        b[0] = b[0] + howmuch
        money = money - mathmoney
        purchacestock = 1
        fakevar4 = 0
        stockamountentry.undraw()
        buystockamounttext1.undraw()
        stockamounttext1.undraw()
        stockamountrec.undraw()


def buy() :
    global money
    global mathmoney
    pickstock = 0
    global howmuch
    howmuch = 0
    global buyrec
    global buytext
    global sellrec
    global selltext
    global statusrec
    global statustext
    global timerec
    global timetext
    global moneyrec
    global moneytext
    global moneytexttext
    global win1
    global stock1rec
    global stock1text
    global stock2rec
    global stock2text
    global stock3rec
    global stock3text1
    global stock3text2
    global stock3text3
    global stock4rec
    global stock4text1
    global stock4text2
    global stock4text3
    global stock5rec
    global stock5text
    global stock6rec
    global stock6text
    global stock7rec
    global stock7text1
    global stock7text2
    global stock7text3
    global stock8rec
    global stock8text1
    global stock8text2
    global stockamountrec
    global buystockamounttext1
    global stockamounttext1
    global stockamountentry
    global invalidnumbertext
    global fakevar2
    global fakevar3
    global fakevar4
    global fakevar5
    global fakevar6
    global fakevar7
    global purchacestock
    purchacestock = 0
    fakevar7 = 0
    mathmoney = 0

    stock1rec.draw(win1)
    stock1text.draw(win1)

    stock2rec.draw(win1)
    stock2text.draw(win1)

    stock3rec.draw(win1)
    stock3text1.draw(win1)
    stock3text2.draw(win1)
    stock3text3.draw(win1)

    stock4rec.draw(win1)
    stock4text1.draw(win1)
    stock4text2.draw(win1)
    stock4text3.draw(win1)

    stock5rec.draw(win1)
    stock5text.draw(win1)

    stock6rec.draw(win1)
    stock6text.draw(win1)

    stock7rec.draw(win1)
    stock7text1.draw(win1)
    stock7text2.draw(win1)
    stock7text3.draw(win1)

    stock8rec.draw(win1)
    stock8text1.draw(win1)
    stock8text2.draw(win1)

    pickstock = 0
    whatstock = 0

    while pickstock == 0 :
        mouse = win1.getMouse()
        mousex = mouse.getX()
        mousey = mouse.getY()
        
        if mousex >= 120 and mousex <= 320 and mousey >= 200 and mousey <= 350 :
            whatstock = 1
            pickstock = 1

        elif mousex >= 360 and mousex <= 560 and mousey >= 200 and mousey <= 350 :
            whatstock = 2
            pickstock = 1
        
        elif mousex >= 620 and mousex <= 820 and mousey >= 200 and mousey <= 350 :
            whatstock = 3
            pickstock = 1

        elif mousex >= 880 and mousex <= 1080 and mousey >= 200 and mousey <= 350 :
            whatstock = 4
            pickstock = 1

        elif mousex >= 120 and mousex <= 320 and mousey >= 450 and mousey <= 600 :
            whatstock = 5
            pickstock = 1

        elif mousex >= 360 and mousex <= 560 and mousey >= 450 and mousey <= 600 :
            whatstock = 6
            pickstock = 1

        elif mousex >= 620 and mousex <= 820 and mousey >= 450 and mousey <= 600 :
            whatstock = 7
            pickstock = 1

        elif mousex >= 880 and mousex <= 1080 and mousey >= 450 and mousey <= 600 :
            whatstock = 8
            pickstock = 1
        else :
            pass
    
    stock1rec.undraw()
    stock1text.undraw()
    stock2rec.undraw()
    stock2text.undraw()
    stock3rec.undraw()
    stock3text1.undraw()
    stock3text2.undraw()
    stock3text3.undraw()
    stock4rec.undraw()
    stock4text1.undraw()
    stock4text2.undraw()
    stock4text3.undraw()
    stock5rec.undraw()
    stock5text.undraw()
    stock6rec.undraw()
    stock6text.undraw()
    stock7rec.undraw()
    stock7text1.undraw()
    stock7text2.undraw()
    stock7text3.undraw()
    stock8rec.undraw()
    stock8text1.undraw()
    stock8text2.undraw()
    
    purchacestock = 0

    while purchacestock == 0 :
        stockamountrec.undraw()
        stockamountrec.draw(win1)

        buystockamounttext1.undraw()
        buystockamounttext1.draw(win1)

        stockamounttext1.undraw()
        stockamounttext1.draw(win1)

        stockamountentry.undraw()
        stockamountentry.draw(win1)
        
        if fakevar7 == 1 :
            invalidnumbertext.draw(win1)

        fakevar3 = 0
        fakevar4 = 0
        fakevar5 = 0
        fakevar6 = 0
        fakevar7 = 0
        
        while fakevar6 == 0 :
            while fakevar3 == 0 :
                win1.getMouse()
                invalidnumbertext.undraw()
                howmuch = stockamountentry.getText()
                try :
                    howmuch = int(stockamountentry.getText())
                except ValueError :
                    invalidnumbertext.draw(win1)
                else :
                    fakevar3 = 1

            while fakevar5 == 0 :
                if int(howmuch) < int(0) :
                    invalidnumbertext.undraw()
                    invalidnumbertext.draw(win1)
                    fakevar5 = 1
                    fakevar3 = 0
                else :
                    howmuch = int(howmuch)
                    fakevar3 = 1
                    fakevar4 = 1
                    fakevar5 = 1
                    fakevar6 = 1
        
        while fakevar4 == 1 :
            mathmoney = 0
            if whatstock == 1 :
                buymath(stock1price,ownedstock1)

            elif whatstock == 2 :
                buymath(stock2price,ownedstock2)
            
            elif whatstock == 3 :
                buymath(stock3price,ownedstock3)

            elif whatstock == 4 :
                buymath(stock4price,ownedstock4)
            
            elif whatstock == 5 :
                buymath(stock5price,ownedstock5)

            elif whatstock == 6 :
                buymath(stock6price,ownedstock6)

            elif whatstock == 7 :
                buymath(stock7price,ownedstock7)

            elif whatstock == 8 :
                buymath(stock8price,ownedstock8)

def sellmath(a,b) :
    global mathmoney
    global money
    global howmuch
    global fakevar4
    global fakevar7
    global purchacestock
    global stockamountentry
    global sellstockamounttext1
    global stockamounttext1
    global stockamountrec
    global win1
    mathmoney = float(a[0]) * howmuch
    if a[0] < howmuch:
        fakevar4 = 0
        purchacestock = 0
        fakevar7 = 1
        stockamountentry.undraw()
        sellstockamounttext1.undraw()
        stockamounttext1.undraw()
        stockamountrec.undraw()
    else :
        b[0] = b[0] - howmuch
        money = money + mathmoney
        purchacestock = 1
        fakevar4 = 0
        stockamountentry.undraw()
        buystockamounttext1.undraw()
        stockamounttext1.undraw()
        stockamountrec.undraw()


def sell() :
    global money
    global mathmoney
    pickstock = 0
    global howmuch
    howmuch = 0
    global buyrec
    global buytext
    global sellrec
    global selltext
    global statusrec
    global statustext
    global timerec
    global timetext
    global moneyrec
    global moneytext
    global moneytexttext
    global win1
    global stock1rec
    global stock1text
    global stock2rec
    global stock2text
    global stock3rec
    global stock3text1
    global stock3text2
    global stock3text3
    global stock4rec
    global stock4text1
    global stock4text2
    global stock4text3
    global stock5rec
    global stock5text
    global stock6rec
    global stock6text
    global stock7rec
    global stock7text1
    global stock7text2
    global stock7text3
    global stock8rec
    global stock8text1
    global stock8text2
    global stockamountrec
    global sellstockamounttext1
    global stockamounttext1
    global stockamountentry
    global invalidnumbertext
    global fakevar2
    global fakevar3
    global fakevar4
    global fakevar5
    global fakevar6
    global fakevar7
    global purchacestock
    purchacestock = 0
    fakevar7 = 0
    mathmoney = 0

    stock1rec.draw(win1)
    stock1text.draw(win1)

    stock2rec.draw(win1)
    stock2text.draw(win1)

    stock3rec.draw(win1)
    stock3text1.draw(win1)
    stock3text2.draw(win1)
    stock3text3.draw(win1)

    stock4rec.draw(win1)
    stock4text1.draw(win1)
    stock4text2.draw(win1)
    stock4text3.draw(win1)

    stock5rec.draw(win1)
    stock5text.draw(win1)

    stock6rec.draw(win1)
    stock6text.draw(win1)

    stock7rec.draw(win1)
    stock7text1.draw(win1)
    stock7text2.draw(win1)
    stock7text3.draw(win1)

    stock8rec.draw(win1)
    stock8text1.draw(win1)
    stock8text2.draw(win1)

    pickstock = 0
    whatstock = 0

    while pickstock == 0 :
        mouse = win1.getMouse()
        mousex = mouse.getX()
        mousey = mouse.getY()
        
        if mousex >= 120 and mousex <= 320 and mousey >= 200 and mousey <= 350 :
            whatstock = 1
            pickstock = 1

        elif mousex >= 360 and mousex <= 560 and mousey >= 200 and mousey <= 350 :
            whatstock = 2
            pickstock = 1
        
        elif mousex >= 620 and mousex <= 820 and mousey >= 200 and mousey <= 350 :
            whatstock = 3
            pickstock = 1

        elif mousex >= 880 and mousex <= 1080 and mousey >= 200 and mousey <= 350 :
            whatstock = 4
            pickstock = 1

        elif mousex >= 120 and mousex <= 320 and mousey >= 450 and mousey <= 600 :
            whatstock = 5
            pickstock = 1

        elif mousex >= 360 and mousex <= 560 and mousey >= 450 and mousey <= 600 :
            whatstock = 6
            pickstock = 1

        elif mousex >= 620 and mousex <= 820 and mousey >= 450 and mousey <= 600 :
            whatstock = 7
            pickstock = 1

        elif mousex >= 880 and mousex <= 1080 and mousey >= 450 and mousey <= 600 :
            whatstock = 8
            pickstock = 1
        else :
            pass
    
    stock1rec.undraw()
    stock1text.undraw()
    stock2rec.undraw()
    stock2text.undraw()
    stock3rec.undraw()
    stock3text1.undraw()
    stock3text2.undraw()
    stock3text3.undraw()
    stock4rec.undraw()
    stock4text1.undraw()
    stock4text2.undraw()
    stock4text3.undraw()
    stock5rec.undraw()
    stock5text.undraw()
    stock6rec.undraw()
    stock6text.undraw()
    stock7rec.undraw()
    stock7text1.undraw()
    stock7text2.undraw()
    stock7text3.undraw()
    stock8rec.undraw()
    stock8text1.undraw()
    stock8text2.undraw()
    
    purchacestock = 0

    while purchacestock == 0 :
        stockamountrec.undraw()
        stockamountrec.draw(win1)

        sellstockamounttext1.undraw()
        sellstockamounttext1.draw(win1)

        stockamounttext1.undraw()
        stockamounttext1.draw(win1)

        stockamountentry.undraw()
        stockamountentry.draw(win1)
        
        if fakevar7 == 1 :
            invalidnumbertext.undraw()
            invalidnumbertext.draw(win1)

        fakevar3 = 0
        fakevar4 = 0
        fakevar5 = 0
        fakevar6 = 0
        fakevar7 = 0
        
        while fakevar6 == 0 :
            while fakevar3 == 0 :
                win1.getMouse()
                invalidnumbertext.undraw()
                howmuch = stockamountentry.getText()
                try :
                    howmuch = int(stockamountentry.getText())
                except ValueError :
                    invalidnumbertext.draw(win1)
                else :
                    fakevar3 = 1

            while fakevar5 == 0 :
                if int(howmuch) < int(0) :
                    invalidnumbertext.undraw()
                    invalidnumbertext.draw(win1)
                    fakevar5 = 1
                    fakevar3 = 0
                else :
                    howmuch = int(howmuch)
                    fakevar3 = 1
                    fakevar4 = 1
                    fakevar5 = 1
                    fakevar6 = 1

        while fakevar4 == 1 :
            mathmoney = 0
            if whatstock == 1 :
                if int(howmuch) > int(ownedstock1[0]) :
                    invalidnumbertext.draw(win1)
                    sellmath(dummystockprice,dummystock)
                else :
                    sellmath(stock1price,ownedstock1)

            elif whatstock == 2 :
                if int(howmuch) > int(ownedstock2[0]) :
                    invalidnumbertext.draw(win1)
                    sellmath(dummystockprice,dummystock)
                else :
                    sellmath(stock2price,ownedstock2)
            
            elif whatstock == 3 :
                if int(howmuch) > int(ownedstock3[0]) :
                    invalidnumbertext.draw(win1)
                    sellmath(dummystockprice,dummystock)
                else :
                    sellmath(stock3price,ownedstock3)

            elif whatstock == 4 :
                if int(howmuch) > int(ownedstock4[0]) :
                    invalidnumbertext.draw(win1)
                    sellmath(dummystockprice,dummystock)
                else :
                    sellmath(stock4price,ownedstock4)
            
            elif whatstock == 5 :
                if int(howmuch) > int(ownedstock5[0]) :
                    invalidnumbertext.draw(win1)
                    sellmath(dummystockprice,dummystock)
                else :
                    sellmath(stock5price,ownedstock5)

            elif whatstock == 6 :
                if int(howmuch) > int(ownedstock6[0]) :
                    invalidnumbertext.draw(win1)
                    sellmath(dummystockprice,dummystock)
                else :
                    sellmath(stock6price,ownedstock6)

            elif whatstock == 7 :
                if int(howmuch) > int(ownedstock7[0]) :
                    invalidnumbertext.draw(win1)
                    sellmath(dummystockprice,dummystock)
                else :
                    sellmath(stock7price,ownedstock7)

            elif whatstock == 8 :
                if int(howmuch) > int(ownedstock8[0]) :
                    invalidnumbertext.draw(win1)
                    sellmath(dummystockprice,dummystock)
                else :
                    sellmath(stock8price,ownedstock8)

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

def whatcommand() :
    global day
    global hour
    global money
    global buyrec
    global buytext
    global sellrec
    global selltext
    global statusrec
    global statustext
    global timerec
    global timetext
    global clockrec
    global clocktext
    global clocktexttext
    global moneyrec
    global moneytext
    global moneytexttext
    
    buyrec.undraw()
    buytext.undraw()
    buyrec.draw(win1)
    buytext.draw(win1)

    sellrec.undraw()
    selltext.undraw()
    sellrec.draw(win1)
    selltext.draw(win1)

    statusrec.undraw()
    statustext.undraw()
    statusrec.draw(win1)
    statustext.draw(win1)

    timerec.undraw()
    timetext.undraw()
    timerec.draw(win1)
    timetext.draw(win1)
    
    clockrec.undraw()
    clocktext.undraw()
    clockrec.draw(win1)
    clocktext.draw(win1)
    
    moneyrec.undraw()
    moneytext.undraw()
    moneyrec.draw(win1)
    moneytext.draw(win1)

    mouse = 0
    mouse = win1.getMouse()
    mousex = mouse.getX()
    mousey = mouse.getY()

    if mousex >=50 and mousex <= 250 and mousey >= 50 and mousey <= 150 :
        buyrec.undraw()
        buytext.undraw()
        sellrec.undraw()
        selltext.undraw()
        statusrec.undraw()
        statustext.undraw()
        timerec.undraw()
        timetext.undraw()
        stockamountentry.setText("")
        buy()
        moneyrec.undraw()
        moneytext.undraw()
        clockrec.undraw()
        clocktext.undraw()
    elif mousex >= 50 and mousex <= 250 and mousey >= 200 and mousey <= 300 :
        buyrec.undraw()
        buytext.undraw()
        sellrec.undraw()
        selltext.undraw()
        statusrec.undraw()
        statustext.undraw()
        timerec.undraw()
        timetext.undraw()
        stockamountentry.setText("")
        sell()
        moneyrec.undraw()
        moneytext.undraw()
        clockrec.undraw()
        clocktext.undraw()
    elif mousex >=50 and mousex <= 250 and mousey >= 350 and mousey <= 450 :
        buyrec.undraw()
        buytext.undraw()
        sellrec.undraw()
        selltext.undraw()
        statusrec.undraw()
        statustext.undraw()
        timerec.undraw()
        timetext.undraw()
        showinfo()
        moneyrec.undraw()
        moneytext.undraw()
        clockrec.undraw()
        clocktext.undraw()
    elif mousex >=50 and mousex <= 250 and mousey >= 500 and mousey <= 600 :
        incrementtime()
        buyrec.undraw()
        buytext.undraw()
        sellrec.undraw()
        selltext.undraw()
        statusrec.undraw()
        statustext.undraw()
        timerec.undraw()
        timetext.undraw()
        clocktext.undraw()
        moneyrec.undraw()
        moneytext.undraw()
        clockrec.undraw()
        clocktexttext = ["Day", str(day[0]), "Hour", str(hour[0]) ]
        clocktext = Text(clockpt3, clocktexttext)
        clocktext.setTextColor(color_rgb(255,255,255))
        clocktext.setSize(12)
    else :
        pass

def easywhatcommand() :
    global day
    global hour
    global money
    global buyrec
    global buytext
    global sellrec
    global selltext
    global statusrec
    global statustext
    global timerec
    global timetext
    global clockrec
    global clocktext
    global clocktexttext
    global moneyrec
    global moneytext
    global moneytexttext
    
    buyrec.undraw()
    buytext.undraw()
    buyrec.draw(win1)
    buytext.draw(win1)

    sellrec.undraw()
    selltext.undraw()
    sellrec.draw(win1)
    selltext.draw(win1)

    statusrec.undraw()
    statustext.undraw()
    statusrec.draw(win1)
    statustext.draw(win1)

    timerec.undraw()
    timetext.undraw()
    timerec.draw(win1)
    timetext.draw(win1)
    
    clockrec.undraw()
    clocktext.undraw()
    clockrec.draw(win1)
    clocktext.draw(win1)
    
    moneyrec.undraw()
    moneytext.undraw()
    moneyrec.draw(win1)
    moneytext.draw(win1)

    mouse = 0
    mouse = win1.getMouse()
    mousex = mouse.getX()
    mousey = mouse.getY()

    if mousex >=50 and mousex <= 250 and mousey >= 50 and mousey <= 150 :
        buyrec.undraw()
        buytext.undraw()
        sellrec.undraw()
        selltext.undraw()
        statusrec.undraw()
        statustext.undraw()
        timerec.undraw()
        timetext.undraw()
        stockamountentry.setText("")
        buy()
        moneyrec.undraw()
        moneytext.undraw()
        clockrec.undraw()
        clocktext.undraw()
    elif mousex >= 50 and mousex <= 250 and mousey >= 200 and mousey <= 300 :
        buyrec.undraw()
        buytext.undraw()
        sellrec.undraw()
        selltext.undraw()
        statusrec.undraw()
        statustext.undraw()
        timerec.undraw()
        timetext.undraw()
        stockamountentry.setText("")
        sell()
        moneyrec.undraw()
        moneytext.undraw()
        clockrec.undraw()
        clocktext.undraw()
    elif mousex >=50 and mousex <= 250 and mousey >= 350 and mousey <= 450 :
        buyrec.undraw()
        buytext.undraw()
        sellrec.undraw()
        selltext.undraw()
        statusrec.undraw()
        statustext.undraw()
        timerec.undraw()
        timetext.undraw()
        showinfo()
        moneyrec.undraw()
        moneytext.undraw()
        clockrec.undraw()
        clocktext.undraw()
    elif mousex >=50 and mousex <= 250 and mousey >= 500 and mousey <= 600 :
        easyincrementtime()
        buyrec.undraw()
        buytext.undraw()
        sellrec.undraw()
        selltext.undraw()
        statusrec.undraw()
        statustext.undraw()
        timerec.undraw()
        timetext.undraw()
        clocktext.undraw()
        moneyrec.undraw()
        moneytext.undraw()
        clockrec.undraw()
        clocktexttext = ["Day", str(day[0]), "Hour", str(hour[0]) ]
        clocktext = Text(clockpt3, clocktexttext)
        clocktext.setTextColor(color_rgb(255,255,255))
        clocktext.setSize(12)
    else :
        pass

def hardwhatcommand() :
    global day
    global hour
    global money
    global buyrec
    global buytext
    global sellrec
    global selltext
    global statusrec
    global statustext
    global timerec
    global timetext
    global clockrec
    global clocktext
    global clocktexttext
    global moneyrec
    global moneytext
    global moneytexttext
    
    buyrec.undraw()
    buytext.undraw()
    buyrec.draw(win1)
    buytext.draw(win1)

    sellrec.undraw()
    selltext.undraw()
    sellrec.draw(win1)
    selltext.draw(win1)

    statusrec.undraw()
    statustext.undraw()
    statusrec.draw(win1)
    statustext.draw(win1)

    timerec.undraw()
    timetext.undraw()
    timerec.draw(win1)
    timetext.draw(win1)
    
    clockrec.undraw()
    clocktext.undraw()
    clockrec.draw(win1)
    clocktext.draw(win1)
    
    moneyrec.undraw()
    moneytext.undraw()
    moneyrec.draw(win1)
    moneytext.draw(win1)

    mouse = 0
    mouse = win1.getMouse()
    mousex = mouse.getX()
    mousey = mouse.getY()

    if mousex >=50 and mousex <= 250 and mousey >= 50 and mousey <= 150 :
        buyrec.undraw()
        buytext.undraw()
        sellrec.undraw()
        selltext.undraw()
        statusrec.undraw()
        statustext.undraw()
        timerec.undraw()
        timetext.undraw()
        stockamountentry.setText("")
        buy()
        moneyrec.undraw()
        moneytext.undraw()
        clockrec.undraw()
        clocktext.undraw()
    elif mousex >= 50 and mousex <= 250 and mousey >= 200 and mousey <= 300 :
        buyrec.undraw()
        buytext.undraw()
        sellrec.undraw()
        selltext.undraw()
        statusrec.undraw()
        statustext.undraw()
        timerec.undraw()
        timetext.undraw()
        stockamountentry.setText("")
        sell()
        moneyrec.undraw()
        moneytext.undraw()
        clockrec.undraw()
        clocktext.undraw()
    elif mousex >=50 and mousex <= 250 and mousey >= 350 and mousey <= 450 :
        buyrec.undraw()
        buytext.undraw()
        sellrec.undraw()
        selltext.undraw()
        statusrec.undraw()
        statustext.undraw()
        timerec.undraw()
        timetext.undraw()
        showinfo()
        moneyrec.undraw()
        moneytext.undraw()
        clockrec.undraw()
        clocktext.undraw()
    elif mousex >=50 and mousex <= 250 and mousey >= 500 and mousey <= 600 :
        hardincrementtime()
        buyrec.undraw()
        buytext.undraw()
        sellrec.undraw()
        selltext.undraw()
        statusrec.undraw()
        statustext.undraw()
        timerec.undraw()
        timetext.undraw()
        clocktext.undraw()
        moneyrec.undraw()
        moneytext.undraw()
        clockrec.undraw()
        clocktexttext = ["Day", str(day[0]), "Hour", str(hour[0]) ]
        clocktext = Text(clockpt3, clocktexttext)
        clocktext.setTextColor(color_rgb(255,255,255))
        clocktext.setSize(12)
    else :
        pass

def easymodegame() :
    game = 1
    global money
    global moneypt3
    global moneytext
    global moneytexttext
    moneygoal = int(1000)
    moneytexttext = ["$",str(money)]
    moneytext = Text(moneypt3, moneytexttext)
    moneytext.setTextColor(color_rgb(255,255,255))
    moneytext.setSize(16)
    while game == 1:
        if money < moneygoal :
            moneyround = str(round(money,2))
            moneylen = len(moneyround.split("."))
            if moneylen == 1 :
                moneytexttext = "$",str(round(money,2)),"0"
            elif moneylen == 2 :
                moneytexttext = "$",str(round(money,2))
            else :
                print("error")
            moneytext = Text(moneypt3, moneytexttext)
            moneytext.setTextColor(color_rgb(255,255,255))
            moneytext.setSize(16)
            easywhatcommand()
        else :
            print("you win")
            game = 0


def mediummodegame() :
    game = 1
    global money
    global moneypt3
    global moneytext
    global moneytexttext
    moneygoal = int(2000)
    moneytexttext = ["$",str(money)]
    moneytext = Text(moneypt3, moneytexttext)
    moneytext.setTextColor(color_rgb(255,255,255))
    moneytext.setSize(16)
    while game == 1:
        if money < moneygoal :
            moneyround = str(round(money,2))
            moneylen = len(moneyround.split("."))
            if moneylen == 1 :
                moneytexttext = "$",str(round(money,2)),"0"
            elif moneylen == 2 :
                moneytexttext = "$",str(round(money,2))
            else :
                print("error")
            moneytext = Text(moneypt3, moneytexttext)
            moneytext.setTextColor(color_rgb(255,255,255))
            moneytext.setSize(16)
            whatcommand()
        else :
            print("you win")
            game = 0


def hardmodegame() :
    game = 1
    global money
    global moneypt3
    global moneytext
    global moneytexttext
    moneygoal = int(4000)
    moneytexttext = ["$",str(money)]
    moneytext = Text(moneypt3, moneytexttext)
    moneytext.setTextColor(color_rgb(255,255,255))
    moneytext.setSize(16)
    while game == 1:
        if money < moneygoal :
            moneyround = str(round(money,2))
            moneylen = len(moneyround.split("."))
            if moneylen == 1 :
                moneytexttext = "$",str(round(money,2)),"0"
            elif moneylen == 2 :
                moneytexttext = "$",str(round(money,2))
            else :
                print("error")
            moneytext = Text(moneypt3, moneytexttext)
            moneytext.setTextColor(color_rgb(255,255,255))
            moneytext.setSize(16)
            hardwhatcommand()
        else :
            print("you win")
            game = 0

def startgame() :
    global money
    global game
    global goal
    global win1
    win1.setBackground(color_rgb(255,255,255)) #3 boxes ---> easy medium or hard
    intropt = Point(600,300)
    introtext = Text(intropt, "Welcome to The Miniture Stock Market Game by SPDC Technologies.")
    introtext.setTextColor(color_rgb(0,0,0))
    introtext.setSize(24)
    introtext.draw(win1)
    intropt2 = Point(600,450)
    introtext2 = Text(intropt2, "Click to Continue")
    introtext2.setTextColor(color_rgb(0,0,0))
    introtext2.setSize(16)
    introtext2.draw(win1)
    win1.getMouse()
    introtext.undraw()
    introtext2.undraw()
    easypt1 = Point(80,150)
    easypt2 = Point(380,550)
    easypt3 = Point(230,350)
    easyrec = Rectangle(easypt1, easypt2)
    easyrec.setFill(color_rgb(0,0,0))
    easyrec.draw(win1)
    easytext = Text(easypt3,"Easy Mode")
    easytext.setTextColor(color_rgb(255,255,255))
    easytext.setSize(36)
    easytext.draw(win1)
    mediumpt1 = Point(450,150)
    mediumpt2 = Point(750,550)
    mediumpt3 = Point(600,350)
    mediumrec = Rectangle(mediumpt1, mediumpt2)
    mediumrec.setFill(color_rgb(0,0,0))
    mediumrec.draw(win1)
    mediumtext = Text(mediumpt3, "Normal Mode")
    mediumtext.setTextColor(color_rgb(255,255,255))
    mediumtext.setSize(36)
    mediumtext.draw(win1)
    hardpt1 = Point(820,150)
    hardpt2 = Point(1120,550)
    hardpt3 = Point(970,350)
    hardrec = Rectangle(hardpt1, hardpt2)
    hardrec.setFill(color_rgb(0,0,0))
    hardrec.draw(win1)
    hardtext = Text(hardpt3, "Hard Mode")
    hardtext.setTextColor(color_rgb(255,255,255))
    hardtext.setSize(36)
    hardtext.draw(win1)
    gamemode = win1.getMouse()
    gamemodex = gamemode.getX()
    gamemodey = gamemode.getY()
    goal = 0
    while game != 1 :
        if gamemodex <= 380 and gamemodex >= 80 and gamemodey <= 550 and gamemodey >= 150 :
            easyrec.undraw()
            easytext.undraw()
            mediumrec.undraw()
            mediumtext.undraw()
            hardrec.undraw()
            hardtext.undraw()
            money = float(300)
            easymodegame()
            game = 1
        elif gamemodex <= 750 and gamemodex >= 450 and gamemodey <= 550 and gamemodey >= 150 :
            easyrec.undraw()
            easytext.undraw()
            mediumrec.undraw()
            mediumtext.undraw()
            hardrec.undraw()
            hardtext.undraw()
            money = float(200)
            mediummodegame()
            game = 1
        elif gamemodex <= 1120 and gamemodex >= 820 and gamemodey <= 550 and gamemodey >= 150 :
            easyrec.undraw()
            easytext.undraw()
            mediumrec.undraw()
            mediumtext.undraw()
            hardrec.undraw()
            hardtext.undraw()
            money = float(100)
            hardmodegame()
            game = 1
        else :
            gamemode = win1.getMouse()
            gamemodex = gamemode.getX()
            gamemodey = gamemode.getY()


startgame()
win1.getMouse