#TODO: 
# Impulse System 
## (short term momentum: trade when both turn green and leave when one turns blue)
## (Catching market turns: Best trading signals not given by green or red but by the loss of green or red)
# Triple Screen
# Date in, Date out
# Easier entry for profit and or stock number

import datetime
date_obj = datetime.datetime.now()
today_date = print(date_obj.strftime("%x"))

# Anything shorter than this is daytraded and recorded later
bars = ["15 minute","30 minute","1 hour","2 hours","4 hours","Daily","Weekly","Monthly"]

class TradeJournal():
    def __init__(self):
        filename = "journal.csv"
        self.tj = open(filename, "a+")

    # Write a new entry into your csv file
    def add_entry(self, symbol, reason, timespan, method_entry, method_exit, ammount_to_invest, max_loss, stock_price, stop_loss_price, stock_num, ls, pl, take_profit=0):
        ls = "long" if ls == "l" else "short"
        self.tj.write("%s;%s;%s;%s;%s;$%s;$%s;$%s;$%s;$%s;%s;%s;%s;%s\n"%(symbol, reason, timespan, method_entry, method_exit, ammount_to_invest, max_loss, stock_price, stop_loss_price, take_profit, stock_num, pl, ls, today_date))
        self.tj.close()
        filename = "journal.csv"
        self.tj = open(filename, "a+")

class DailyChecksheet():
    def __init__(self):
        filename = "checklists/daily_checksheet.txt"
        self.cs = open(filename, "r")

    def check_it_off():
        items = self.cs.readlines()
        for item in items: 
            print(item)
            response = input("Did you do this (y/n)? ")
            if response is not "y":
                return False
        return True

class DailyTradeAblilityList():
    def __init__(self):
        filename = "checklists/trade_ability.txt"
        self.cs = open(filename, "r")

    def analyze():
        items = self.cs.readlines()
        total = 0
        for i in range(0,len(items), 3):
            for y in range(0,3):
                print(items[y+i])
            total += int(input("Score: ") - 1)
        if total < 5:
            print("Do not actively trade today")
            return False
        elif total < 7 or total > 8:
            print("Trade with Caution")
        else:
            print("Trade away!")
        return True
        
class EarningsWatchlist():
    def __init__(self):
        filename = "earnings_watchlist.csv"
        self.ew = open(filename, "a+")

    def record_earnings_date(self, stock_name, earnings_date, reason):
        self.ew.write("%s;%s;%s\n"%(stock_name, earnings_date, reason))
        self.ew.close()
        filename = "earnings_watchlist.csv"
        self.ew = open(filename, "a+")

    def check_upcoming_earnings(timeframe):
        print("I AM GOING TO UPCOMINGLY EARN")

def add_to_journal(tj):
    # Get all the string information from the files and choose the appropriate information
    reasons = open("reason.txt", "r").readlines()
    bar_num = 0
    method_entries = open("entry.txt", "r").readlines()
    method_exits = open("exit.txt", "r").readlines()

    symbol = input("\nWhat is the symbol traded? ")
    for i in range(0,len(reasons)):
        print(str(i+1) + ": " + reasons[i])
    reason = reasons[int(input("\nWhy are you entering the trade? "))-1].rstrip()
    for i in range(0,len(bars)):
        print(str(i+1) + ": " + bars[i])
    timespan_num = int(input("\nWhat bar chart are you using to exit and enter the trade? "))-1
    # bar_num = timespan-1
    longshort = input("Are you long or short? (l/s)")
    for i in range(0,len(method_entries)):
        print(str(i+1) + ": " + method_entries[i])
    enter = method_entries[int(input("\nHow are you entering the trade? "))-1].rstrip()
    for i in range(0,len(method_exits)):
        print(str(i+1) + ": " + method_exits[i])
    exit = method_exits[int(input("\nHow are you exiting the trade? "))-1].rstrip()

    print("Impulse System for %s chart:"% bars[timespan_num])
    print("1. Green (Increasing EMA and Increasing MACD)")
    print("2. Red (Decreasing EMA and Decreasing MACD)")
    print("3. Blue")
    impulse_num_1 = input("#: ")
    print("Impulse System for %s chart:"% bars[timespan_num-1])
    print("1. Green (Increasing EMA and Increasing MACD)")
    print("2. Red (Decreasing EMA and Decreasing MACD)")
    print("3. Blue")
    impulse_num_2 = input("#: ")
    if impulse_num_2 != impulse_num_1:
        print("Find a better trade option")
        return


    ok = False
    while not ok:
        # Play the numbers game
        ammount = float(input("How much are you investing? "))
        loss_max = float(input("How much are you willing to lose (no greater than 2%)? "))
        stock_price = float(input("What is the stock price? "))
        take_profit = float(input("What price do you want to take profit? "))

        stocknum = ammount/stock_price
        stop_loss_price = (stock_price-((loss_max*stock_price)/ammount))
        print("You may buy %i stocks"%(stocknum))
        print("You will sell your stock at %f"%stop_loss_price)


        #Determine Profit/Loss
        pl = 0
        while True: 
            if(longshort == "l"):
                if impulse_num_1 == 2 or impulse_num_2 == 2:
                    print("The impulse system doesn't allow you to make this trade")
                    return
                pl = (take_profit - stock_price)/(stock_price - stop_loss_price)
            elif(longshort == "s"):
                if impulse_num_1 == 1 or impulse_num_2 == 1:
                    print("The impulse system doesn't allow you to make this trade")
                    return
                pl = (stock_price - take_profit)/(stop_loss_price - stock_price)
            else:
                continue
            break

        print("P/L is %f"%pl)
        if pl < 2:
            print("Please enter a trade with at least a 2.0 PL")
            continue

        oki = input("Is this acceptable? ")
        ok = True if oki == "y" else False

        tj.add_entry(symbol, reason, timespan, enter, exit, ammount, loss_max, stock_price, stop_loss_price, stocknum, longshort, pl, take_profit)

        reasons.close()
        timespans.close()
        method_entries.close()
        method_exits.close()



def can_trade(c1, c2):
    # Do stuff based on date to check whether or not 
    return True

def run():
    tj = TradeJournal()
    dcs = DailyChecksheet()
    dtal = DailyTradeAblilityList()
    ew = EarningsWatchlist()
    trade,c1,c2 = False, False, False
    while True:
        trade = can_trade(c1, c2)
        print("Options:")
        print("1. Add to Trade Journal")
        print("2. Daily Checksheet Review")
        print("3. Determine Personal Trade Ability")
        print("4. Write off Day Trades")
        print("5. Earnings Calls sheet")
        choice = int(input())
        if choice is 1:
            add_to_journal(tj)
        if choice is 2:
            c1 = dcs.check_it_off()
        if choice is 3: 
            c2 = dtal.analyze()
        if choice is 5:
            print("Would you like to view the upcoming earnings? Or add one?")
            print("1. View")
            print("2. Add")
            choice = int(input("Choice: "))
            if choice is 1:
                ew.check_upcoming_earnings()
            if choice is 2:
                stock_name = input("Stock name? ")
                earnings_date = input("Earnings date? ")
                reason = input("Reason for following this call?")
                ew.record_earnings_date(stock_name, earnings_date, reason)

run()