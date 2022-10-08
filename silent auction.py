logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
print("Welcome to the blind auction")
bidders={}
add_new_bidder="yes"
max=0
winner=""
while add_new_bidder=="yes":
    name = input("what is your name? :\n")
    bid = int(input("what is your bid? : $\n"))
    bidders[name]=bid
    if bid>max:
        max=bid
        winner=name
    add_new_bidder = input("Are there any other bidders?: type'yes' or 'no'     ")
    if add_new_bidder == "no":
        print(f"The winner is {winner} with a bid of ${max}")

