from rooms import Rooms
from characters import Characters
from rooms import Command_center


print("Welcome to My adventure game and my very first python project")
name = input("What would you like to be called>>> ")
print(
    "Hello "
    + name
    + "\nYour adventure begins at a place of horrors \ncommonly referred to as the great dungeon of Naserik"
)

ready = input("IF YOU DO NOT WISH TO PLAY, LEAVE BLANK!!")
if ready is not None:
    print("This is the layout of the dungeon")
else:
    exit()

Ghost_room = Rooms("Den of Ghosts")
Demon_room = Rooms("Hell's Paradise")
Zombie_room = Rooms("Home of the undead")
Snake_room = Rooms("Slithery Serpentine")
Dark_elves_room = Rooms("Trove of the forgotten race")
Ogres_room = Rooms("The Swamp")
Vampire_room = Rooms("The Manor")

Ghost_room.set_floor(1)
Demon_room.set_floor(1)
Zombie_room.set_floor(1)
Snake_room.set_floor(1)
Dark_elves_room.set_floor(2)
Ogres_room.set_floor(2)
Vampire_room.set_floor(2)

all_rooms = [
    Ghost_room,
    Demon_room,
    Zombie_room,
    Snake_room,
    Dark_elves_room,
    Ogres_room,
    Vampire_room,
]


for i in all_rooms:
    print("the " + i.name + " is on the " + str(i.floor) + " floor")


Demon_room.set_description("A huge room with low visibility and an erry presence")
Ghost_room.set_description(
    "small cramped moist room filled with the spirits of the departed who still have a score to settle"
)
Zombie_room.set_description(
    "Broken ceiling and tattered walls and a foul smell of rotten corpses"
)
Snake_room.set_description(
    "A warm room with no windows and curtains, only the sound of snakes all around you"
)
Dark_elves_room.set_description(
    "A library that seems to be endless with scrolls and enchantment spells at every turn \n watch out for flying books!!"
)
Ogres_room.set_description(
    "A smelly swamp with echoes of toads \n you might want to cover your nose"
)
Vampire_room.set_description(
    "Stunning yet creepy, it's not well kept and there lurks a group of bats hanging from the chandelier"
)
all_description = [
    Demon_room.describe,
    Ghost_room.describe,
    Zombie_room.describe,
    Snake_room.describe,
    Dark_elves_room.describe,
    Ogres_room.describe,
    Vampire_room.describe,
]

user_description = input(
    "Would you like to know the description of every room? \nJust to know what you're getting yourself into>>> "
)
if user_description == "yes":
    for a in all_description:
        print(a)
