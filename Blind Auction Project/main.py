
participants = {}
new_bids = True

while new_bids:
    name = input("what is your name: ")
    price = int(input("enter your bid: "))

    participants[name]=price
    print("\n" * 20)

    bids = input("new bids need to be added (yes or no): ").lower()
    if bids == "no":
        new_bids = False


winner = max(participants, key=participants.get)
highest_bid = participants[winner]
print(f"The winner is {winner} with a bid of {highest_bid}")
