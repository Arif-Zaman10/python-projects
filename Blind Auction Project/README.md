🕶️ Blind Auction Program

A simple Python script that runs a blind auction in the console.
Each bidder secretly enters their name and bid. The program stores all bids, clears the screen after each entry, and finally announces the winner with the highest bid.



📝 How It Works

1. Bid Entry:  
    - Each participant types their name.  
    - Then types their bid (an integer).  

2. Hiding Previous Bids:  
    - After each entry, the program prints multiple blank lines (print("\n" * 20)) to clear the   console, so other bidders can’t see previous bids.

3. More Bidders:
    - After each bid, the program asks if there are more bidders
    - Type yes to add another bid.
    - Type no to end the bidding.

4. Winner Selection
    - All bids are saved to a Python dictionary {name: bid}.
    - When bidding ends, the program compares all bids.
    - The highest bidder and their bid are displayed.




🛠 Features

- Collects unlimited bids until the user types no.  
- Clears the console output after each bid for privacy.  
- Automatically finds and displays the highest bidder and their bid.  



📄 Notes

- Bid amounts must be integers.  
- If two bidders have the same highest bid, the first entered will currently win (tie handling can be added).  
- You can modify the number of newlines in print("\n" * 20) if you want more or fewer blank lines.