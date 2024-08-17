from random import choice

print("Welcome to Treasure Island. Your mission is to find the treasure!")

print("You are part of a crew that is sailing the high seas. It has been 14 days since you have been ashore.")

choice_one = input("You are tired, hungry, and dehydrated. You and your crew spot land off in the distance.\n Do you: 1. go to shore, or  2. keep sailing? ").lower()
if choice_one == "go to shore" or choice_one == str(1):
    print("When you make landfall, you are immediately set upon by the island inhabitants. \nYou are not welcome, and your fate has been sealed.")
    quit()
elif choice_one == "keep sailing" or choice_one == str(2):
    print("You and your crew continue onwards, risking possible survival for more promising lands.")

choice_two = input("Two days later, you come across another vessel in open waters. \n Do you: 1. Approach the vessel, or 2. Keep sailing? ").lower()
if choice_two== "approach the vessel" or choice_two == str(1):
    print("The members of the other vessel turn out to be pirates. They steal all of your vittles and force you to walk the plank -- bonding your fate to the bottom of the sea.")
    quit()
elif choice_two == "keep sailing" or choice_two == str(2):
    print("As you sail on by, you notice the ship has a black flag trailing in their wake. Strategic cowardice keeps you alive.")

choice_three = input("Five more days pass. You and your crew are tired and out of supplies. You spot land, but it looks somewhat familiar. Could it be the same island you passed the first time?\n Do you: 1. make landfall, or 2. continue sailing towards the horizon ").lower()
if choice_three == "make landfall" or choice_three == str(1):
    print("You made the right choice. You and your crew would not have lasted the week at sea without fresh food and water. You have made it one step closer towards the treasure, and... the glory")
    quit()
elif choice_three == "keep sailing towards the horizon" or choice_three == str(2):
    print("You continue onwards towards the horizon, not realizing that you are a figurine being played in a tabletop RPG. To you, the world is flat. You have reached the edge of the table and plummet to the floor.")
    quit()