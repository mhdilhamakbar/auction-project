from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo
print(logo)
print("welcome to secret auction program")


bidders = {}
bidder_auction = False
def find_highest_bidder(bidding_record):
  highest_prices = 0
  winner =""
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_prices:
      highest_prices = bid_amount
      winner = bidder
  print(f"The highest bidder is {winner} with {highest_prices}")

while not bidder_auction:
    name = input("what is ur name? ")
    bid = int(input("what is ur bid? $"))
    yes_no = input("are there any bidders? ")
    bidders[name] = bid
    if yes_no == "no":
      find_highest_bidder(bidders)
      bidder_auction = True
    else:
      clear()