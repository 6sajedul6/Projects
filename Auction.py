import os

bids={}
def finding_highest_bidder(bidding_record):
    highest_bid=0
    winner=""
    for i in bidding_record:
        bid_amount=bidding_record[i]
        if bid_amount > highest_bid:
            highest_bid=bid_amount
            winner=i
    print(f"The winner is {winner} with the highest bid of ${highest_bid}.")

bidding_ends=False
while not bidding_ends:
    name=input("What is your name?:")
    price=int(input("What is your bid?:$"))
    bids[name]=price
    should_continue=input("Are there any other bidders??? Type 'Yes' or 'No'. ").lower()
    if should_continue=="no":
        bidding_ends=True
        finding_highest_bidder(bids)
    elif should_continue=="yes":
        os.system('cls')



