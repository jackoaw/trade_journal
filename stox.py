
class TradeJournal():
    def __init__(self):
        filename = "journal.csv"
        self.tj = open(filename, "a+")

    # Write a new entry into your csv file
    def add_entry(self, symbol, reason, timespan, method_entry, method_exit, ammount_to_invest, max_loss, stock_price, stop_loss_price, stock_num, ls, pl, take_profit=0):
        ls = "long" if ls == "l" else "short"
        self.tj.write("%s;%s;%s;%s;%s;$%s;$%s;$%s;$%s;$%s;%s;$%s;%s\n"%(symbol, reason, timespan, method_entry, method_exit, ammount_to_invest, max_loss, stock_price, stop_loss_price, take_profit, stock_num, pl, ls))
        self.tj.close()
        __init__()

def add_to_journal(tj):
    # Get all the string information from the files and choose the appropriate information
    reasons = open("reason.txt", "r").readlines()
    timespans = open("bars.txt", "r").readlines()
    method_entries = open("entry.txt", "r").readlines()
    method_exits = open("exit.txt", "r").readlines()
    symbol = input("\nWhat is the symbol traded?")
    for i in range(0,len(reasons)):
        print(str(i+1) + ": " + reasons[i])
    reason = reasons[int(input("\nWhy are you entering the trade?"))-1].rstrip()
    for i in range(0,len(timespans)):
        print(str(i+1) + ": " + timespans[i])
    timespan = timespans[int(input("\nWhat bar chart are you using to exit and enter the trade?"))-1].rstrip()
    for i in range(0,len(method_entries)):
        print(str(i+1) + ": " + method_entries[i])
    longshort = input("Are you long or short? (l/s)")
    enter = method_entries[int(input("\nHow are you entering the trade?"))-1].rstrip()
    for i in range(0,len(method_exits)):
        print(str(i+1) + ": " + method_exits[i])
    exit = method_exits[int(input("\nHow are you exiting the trade?"))-1].rstrip()

    ok = False
    while not ok:
        # Play the numbers game
        ammount = float(input("How much are you investing?"))
        loss_max = float(input("How much are you willing to lose (no greater than 2%)?"))
        stock_price = float(input("What is the stock price?"))
        take_profit = float(input("What price do you want to take profit"))

        stocknum = ammount/stock_price
        stop_loss_price = (stock_price-((loss_max*stock_price)/ammount))
        print("You may buy %i stocks"%(stocknum))
        print("You will sell your stock at %f"%stop_loss_price)
        
        #Determine Profit/Loss
        pl = 0
        if(longshort == "l"):
            pl = (take_profit - stock_price)/(stock_price - stop_loss_price)
        elif(longshort == "s"):
            pl = (stock_price - take_profit)/(stop_loss_price - stock_price)

        print("P/L is %f"%pl)
        if pl < 2:
            print("Please enter a trade with at least a 2.0 PL")
            continue

        oki = input("Is this acceptable?")
        ok = True if oki == "y" else False

        tj.add_entry(symbol, reason, timespan, enter, exit, ammount, loss_max, stock_price, stop_loss_price, stocknum, longshort, pl, take_profit)


def run():
    tj = TradeJournal()
    while True:
        print("Options:")
        print("1. Add to Trade Journal")
        print("2. View Bid/Ask")
        choice = int(input())
        if choice is 1:
            add_to_journal(tj)
run()