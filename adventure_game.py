def show_instructions():
    """Display the game instructions to the player."""
    print("""
Text Adventure Game
-------------------
Commands:
  go [direction]
  get [item]
""")

def show_status():
    """Display the current status of the player."""
    print(f"---------------------")
    print(f"You are in the {current_room}.")
    print(f"Inventory: {inventory}")
    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}.")
    print(f"---------------------")

# A dictionary linking rooms to other rooms
rooms = {
    'Hall': {'south': 'Kitchen', 'east': 'Dining Room', 'item': 'key'},
    'Kitchen': {'north': 'Hall', 'item': 'monster'},
    'Dining Room': {'west': 'Hall', 'south': 'Garden', 'item': 'potion'},
    'Garden': {'north': 'Dining Room'}
}

# Start the player in the Hall
current_room = 'Hall'
inventory = []

show_instructions()

# Main game loop
while True:
    show_status()

    # Get the player's next action
    move = input("> ").lower().split()

    # Handle movement
    if move[0] == 'go':
        direction = move[1]
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way!")

    # Handle picking up an item
    elif move[0] == 'get':
        item = move[1]
        if "item" in rooms[current_room] and item == rooms[current_room]['item']:
            inventory.append(item)
            print(f"{item} got!")
            del rooms[current_room]['item']
        else:
            print("Can't get that!")

    # Player encounters a monster
    if 'item' in rooms[current_room] and rooms[current_room]['item'] == 'monster':
        print("A monster has got you... GAME OVER!")
        break

    # Player wins by reaching the garden with all items
    if current_room == 'Garden' and 'key' in inventory and 'potion' in inventory:
        print("You escaped the house with the key and potion... YOU WIN!")
        break