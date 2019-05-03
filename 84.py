
# Since there are no methods needed for a player a dictionary may be a better option since this is only storing data.

player_location = "start_room"

player_data = {
    "name": "none",  # This will come from input.
    # The player will always start here.
    "location": "You are at the start of the game in a small dining room in a small house.\n",
    "location_name": "start_room",
    "health": 100
}

# Create locations for the game with directions as to where a player can go in them.


class Location:
    def __init__(self, moves, actions, keys):
        self.moves = moves
        self.actions = actions
        self.keys = keys
        self.description = "You are in a small dining room in a small house. There is no furniture in this room.\n\nYou are facing a short hallway leading to a staircase.\n\nThere is an open door to your left leading to a small porch.\n\nTo your right is the living room.\n\nThe area of the room back behind you is dark.\n\nThere is a light switch on the wall.\n\n"


# ---------------------------------------------------------
# This will print at the beginning of the game and every time a player enters "help".

def help_file():

    print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")

    print("You will be exploring places and interacting with items in the game.\n")

    print("Please use words like 'forward', 'left', 'right' and 'back' for movement inside a structure.\n")

    print("Directions such as 'north' or 'n'; 'south' or 's'; 'east' or 'e'; and 'west' or 'w' will work when you are outside.\n")

    print("When you want to use an item in the game, just enter the name of the item like 'boomerang'. You will then be prompted for what you want to do with that item.\n")

    print("To see a description of where you are in a room or an area, just type 'description'.\n")

    print("To see this introductory list again, type 'help'.\n")

    print("When you are ready to continue, press the ENTER key.\n")
    input()

    print("\n- - - - - - - - - - - - - - - - - - - - - - - - -\n")


# ---------------------------------------------------------
# The starting room:

# This creates a new object based on the Location class.
# The two tuples are the moves list and the actions list for later validation.
start_room_keys = {"light": "off"}

start_room = Location(("stairs", "staircase", "forward", "porch", "left", "living room", "right", "back"),
                      ("look", "light", "light switch", "box", "open"), start_room_keys)


# Functions for a player move or action in this room:
def start_room_moves_actions(player_input):
    if player_input in start_room.moves:
        start_room_moves(player_input)
    elif player_input in start_room.actions:
        start_room_action(player_input)
    else:
        print("\nThat is not a valid request for this situation.\n")
        play_game()


def start_room_moves(player_move):

    print()

    if player_move == "stairs" or player_move == "staircase" or player_move == "forward":
        print("You walk to the bottom of the stairs. There is an old rug at the base of the stairs.")
        player_data["location"] = "At the bottom of the stairs in the small house"
        player_data["location_name"] = "house_stairs"
    elif player_move == "porch" or player_move == "left":
        print("You walk through the open door to the porch.")
        print("The view from here is spectacular. You are looking out over a wooded valley with a river far below.")
        print("There are rolling hills off in the distance.")
        print(
            "You walk to the edge of the porch and see some letters carved in the railing.")
        print()
        print("RWBL")
        print()
        print("Hmm...I wonder what that means?\n")
        player_data["location"] = "On the back porch of a small house."
        player_data["location_name"] = "house_porch"
    elif player_move == "right" or player_move == "living room":
        print("As you enter the living room you notice a large painting of a sunset scene over a wooded valley on one wall.\n")
        player_data["location"] = "You are in the living room in a small house."
        player_data["location_name"] = "house_living_room"
    elif player_move == "back":
        if start_room.keys["light"] == "off":
            print(
                "It is too dark to go in that direction. You should be more careful about where you go.\n")
        else:
            print("There is an old shoe box in the back next to the wall.\n")


def start_room_action(player_action):
    if player_action == "look":
        print("There is no furniture in this room. There is an old hanging light fixture that has a bulb in the middle of the ceiling. There is a light switch to your right on the wall. The room back behind you is dark and you cannot see what is there.\n")
    elif player_action == "light" or player_action == "light switch":
        print("\nThe hanging light in the middle of the ceiling illuminates the room. There appears to be a box back of the room where it was previously dark.\n")
        start_room.keys["light"] = "on"
    elif player_action == "box" or player_action == "open":
        if start_room.keys["light"] == "off":
            print("What are you trying to do? You need to lighten up.\n")
        else:
            print("\nThere is a brand new pair of running shoes in the box.\n")
            print("As you take them out, you see...SOMETHING.\n")


# ---------------------------------------------------------
# The porch:


# ---------------------------------------------------------
# The stairs:


# ---------------------------------------------------------
# The living room:


# -------------------------------------------------------------
# End of code/functions for individual rooms/locations.
# -------------------------------------------------------------

# Get a name from player and update player object.
print("Welcome to the game.")


def get_player_name():
    name_input = input("What is your name?")

    if len(name_input) > 10 or len(name_input) < 1:
        print("Please enter a name with 0 - 10 letters.")
        get_player_name()
    else:
        player_data["name"] = name_input


get_player_name()


# Print welcome to player using name.
print("\nWelcome, " + str(player_data["name"]) + "!")

# Print the starting story text.
# Print a description of the game with examples of valid entries.
help_file()

# Print a description of the starting room.
print(start_room.description)

# ---------------------------------------------------------
# Main game loop


def play_game():
    # Get input from player for move or interaction.
    player_input = input("What would you like to do now?\n")

    # If 'description', then print the current location's description, and then prompt again for input.
    if player_input == "description":
        current_location = player_data["location"]
        print("\n" + str(current_location))
    elif player_input == "help":
        help_file()
    elif player_input == "":
        print("Please try again.")
    else:
        # Get the name of the player's current location.
        current_location_name = player_data["location_name"]
        if current_location_name == "start_room":
            start_room_moves_actions(player_input)

        # Add elif statements here checking for rooms.

    # Check to see if the game is over at this point.
    if player_data["health"] < 1:
        print("You are dead! Too bad. You seemed like a nice person.")
    else:
        play_game()


play_game()
