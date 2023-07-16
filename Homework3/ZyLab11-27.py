#Sydney Ani PID: 1869076

# Initialize an empty roster dictionary
roster = {}

# Function to output the roster
def output_roster():
    print("ROSTER")
    # Sort the roster dictionary by jersey numbers and output the elements
    for jersey_number in sorted(roster.keys()):
        print("Jersey number:", jersey_number, end=", ")
        print("Rating:", roster[jersey_number])


# Function to add a player to the roster
def add_player():
    print("Enter player's jersey number:", end=" ")
    jersey_number = int(input())
    print("Enter player's rating:", end=" ")
    rating = int(input())
    roster[jersey_number] = rating

# Function to remove a player from the roster
def delete_player():
    jersey_number = int(input("Enter a jersey number:\n"))
    if jersey_number in roster:
        del roster[jersey_number]

# Function to update a player's rating
def update_player_rating():
    jersey_number = int(input("Enter a jersey number:\n"))
    if jersey_number in roster:
        new_rating = int(input("Enter a new rating for player:\n"))
        roster[jersey_number] = new_rating

# Function to output players above a rating
def output_players_above_rating():
    rating = int(input("Enter a rating:\n"))
    print("ABOVE", rating)
    for jersey_number, player_rating in roster.items():
        if player_rating > rating:
            print("Jersey number:", jersey_number, end=", ")
            print("Rating:", roster[jersey_number])

# Main program loop
for i in range(1, 6):
    print("Enter player", str(i) + "'s jersey number:")
    jersey_number = int(input())
    print("Enter player", str(i) + "'s rating:\n")
    rating = int(input())
    roster[jersey_number] = rating

output_roster()

while True:
    print("\nMENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")

    option = input("\nChoose an option:\n")

    if option == 'a':
        add_player()
    elif option == 'd':
        delete_player()
    elif option == 'u':
        update_player_rating()
    elif option == 'r':
        output_players_above_rating()
    elif option == 'o':
        output_roster()
    elif option == 'q':
        break

