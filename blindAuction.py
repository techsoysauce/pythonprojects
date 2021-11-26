#Import clear function
import os
clear = lambda: os.system('clear')
clear()

logo = "----- WELCOME TO THE BLIND AUCTION SITE -----"
bidders = {}
def auctioneers():
  otherBidders = True

  while otherBidders:
    bidderName = input("What is your name?\n")
    bidderPrice = int(input("What is your bid price?\n"))
    print(bidderName + "  " + str(bidderPrice))
    bidders [bidderName] = bidderPrice
    askBidders = input("Are there other bidders? y/n \n")
    if askBidders=="y":
      otherBidders=True
      clear()
    else:
      otherBidders=False
    


print(logo)

print("Welcome to the Secret Auction Program\n")
auctioneers()

winner = max(bidders, key=bidders.get)
clear()
print(f"The silent auction winner is {winner} with a bid price of {bidders[winner]}.")

