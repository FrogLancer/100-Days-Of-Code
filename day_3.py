#  Day 3, Treasure Island Game

print("""Welcome to Treasure Island.
Your mission is to find the treasure.""")

choice1 = input("""You're at a crossroad.
Where do you want to go? (left or right): """)

if choice1 == 'left':
    choice2 = input("""You've come to a lake. There's an island in the middle of the lake.
    Do you wait for a boat or do you swim?
    """)
    if choice2 == 'wait':
        choice3 = input("""You arrive at the island unharmed. There is a house with 3 doors.
        One door is red, one yellow, and the other is blue.
        Which door do you choose?
        """)
        if choice3 == 'red':
            print("""The door shuts behind you and the room fills with fire.
            Game over.""")
        elif choice3 == 'yellow':
            print("""You found the treasure.
            You win!""")
        elif choice3 == 'blue':
            print("""The door closes behind you and the room fills with water.
            Game over.""")
    elif choice2 == 'swim':
        print("""You attempt to swim to the island, but freezing waters render it impossible to get there and you're too far out to return.
        Game over.""")
elif choice1 == 'right':
    print("""You take the right path and head back home.
    This could've been a funner game, but whatever. No harm, no foul.""")
