# So the goal here is to have a catalog of all the items in your game
# To correctly generate a games items they need to be bundled in a list
# A list in programming terms is anything in square brackets [] to put it simply

# When a list is described its described as a list of x where x is the type of variable within it
# IE: ["apple", "pear", "grape"] is a list of strings (anything inside "" OR '' are considered strings)

# Logging = output. How you'll figure out whats going wrong
import logging

# Built in AP imports
from BaseClasses import Item, ItemClassification

# These come from the other files in this example. If you want to see the source ctrl + click the name
# You can also do that ctrl + click for any functions to see what they do
from .types import ItemData, ChapterType, APSkeletonItem, chapter_type_to_name
from .locations import get_total_locations
from typing import List, Dict, TYPE_CHECKING

# This is just making sure nothing gets confused dw about what its doing exactly
if TYPE_CHECKING:
    from . import APSkeletonWorld

NRBASE = 4918940

# If you're curious about the -> List[Item] that is a syntax to make sure you return the correct variable type
# In this instance we're saying we only want to return a list of items
# You'll see a bunch of other examples of this in other functions
# It's main purpose is to protect yourself from yourself
def create_itempool(world: "APSkeletonWorld") -> List[Item]:
    # This is the empty list of items. You'll add all the items in the game to this list
    itempool: List[Item] = []

    # In this function is where you would remove any starting items that you add in options such as starting chapter
    # This is also the place you would add dynamic amounts of items from options
    # I can point to Sly Cooper and the Thievious Raccoonus since I did that

    # This is a good place to grab anything you need from options
    starting_chapter = chapter_type_to_name[ChapterType(world.options.StartingChapter)]

    # For this example I'll make it so there is a starting chapter
    # We loop through all the chapters in the my_chapter section
    for chapter in ap_characters.keys():
        # If the starting chapter equals the chapter we're looking at skip it
        # We skip it since we dont want to add the chapter the player started with to the item pool
        print("-------------------------")
        print(starting_chapter)
        print("-------------------------")
        if starting_chapter == chapter:
            continue
        # Otherwise then we create an item with that name and add it to the item pool
        else:
            itempool.append(create_item(world, chapter))
    
    # It's up to you and how you want things organized but I like to deal with victory here
    # This creates your win item and then places it at the "location" where you win
    victory = create_item(world, "Victory")
    world.multiworld.get_location("Heolstor, the Nightlord", world.player).place_locked_item(victory)

    # Then junk items are made
    # Check out the create_junk_items function for more details
    itempool += create_junk_items(world, get_total_locations(world) - len(itempool) - 1)

    return itempool

# This is a generic function to create a singular item
def create_item(world: "APSkeletonWorld", name: str) -> Item:
    data = item_table[name]
    return APSkeletonItem(name, data.classification, data.ap_code, world.player)

# Another generic function. For creating a bunch of items at once!
def create_multiple_items(world: "APSkeletonWorld", name: str, count: int,
                          item_type: ItemClassification = ItemClassification.progression) -> List[Item]:
    data = item_table[name]
    itemlist: List[Item] = []

    for i in range(count):
        itemlist += [APSkeletonItem(name, item_type, data.ap_code, world.player)]

    return itemlist

# Finally, where junk items are created
def create_junk_items(world: "APSkeletonWorld", count: int) -> List[Item]:
    trap_chance = world.options.TrapChance.value
    junk_pool: List[Item] = []
    junk_list: Dict[str, int] = {}
    trap_list: Dict[str, int] = {}

    # This grabs all the junk items and trap items
    for name in item_table.keys():
        # Here we are getting all the junk item names and weights
        ic = item_table[name].classification
        if ic == ItemClassification.filler:
            junk_list[name] = junk_weights.get(name)

        # This is for traps if your randomization includes it
        # It also grabs the trap weights from the options page
        elif trap_chance > 0 and ic == ItemClassification.trap:
            if name == "Forcefem Trap":
                trap_list[name] = world.options.ForcefemTrapWeight.value
            elif name == "Speed Change Trap":
                trap_list[name] = world.options.SpeedChangeTrapWeight.value

    # Where all the magic happens of adding the junk and traps randomly
    # AP does all the weight management so we just need to worry about how many are created
    for i in range(count):
        if trap_chance > 0 and world.random.randint(1, 100) <= trap_chance:
            junk_pool.append(world.create_item(
                world.random.choices(list(trap_list.keys()), weights=list(trap_list.values()), k=1)[0]))
        else:
            junk_pool.append(world.create_item(
                world.random.choices(list(junk_list.keys()), weights=list(junk_list.values()), k=1)[0]))

    return junk_pool

# Time for the fun part of listing all of the items
# Watch out for overlap with your item codes
# These are just random numbers dont trust them PLEASE
# I've seen some games that dynamically add item codes such as DOOM as well
ap_memory_fragments = {
    # Memory Fragments
    "Memory Fragment - Wylder": ItemData(NRBASE + 1, ItemClassification.progression, 9),
    "Memory Fragment - Ironeye": ItemData(NRBASE + 2, ItemClassification.progression, 8),
    "Memory Fragment - Guardian": ItemData(NRBASE + 3, ItemClassification.progression, 10),
    "Memory Fragment - Duchess": ItemData(NRBASE + 4, ItemClassification.progression, 9),
    "Memory Fragment - Raider": ItemData(NRBASE + 5, ItemClassification.progression, 8),
    "Memory Fragment - Revenant": ItemData(NRBASE + 6, ItemClassification.progression, 8),
    "Memory Fragment - Recluse": ItemData(NRBASE + 7, ItemClassification.progression, 8),
    "Memory Fragment - Executor": ItemData(NRBASE + 8, ItemClassification.progression, 7),
    
    # Victory is added here since in this organization it needs to be in the default item pool
    # "Victory": ItemData(NRBASE + 9, ItemClassification.progression)
}

ap_shifting_earths = {
    "Crater Unlock": ItemData(NRBASE + 9, ItemClassification.progression),
    "Mountaintop Unlock": ItemData(NRBASE + 10, ItemClassification.progression),
    "Rotted Woods Unlock": ItemData(NRBASE + 11, ItemClassification.progression),
    "Noklateo, the Shrouded City Unlock": ItemData(NRBASE + 12, ItemClassification.progression),
}

ap_nights = {
    "Night 1": ItemData(NRBASE + 13, ItemClassification.progression),
    "Night 2": ItemData(NRBASE + 14, ItemClassification.progression),
    "Night 3": ItemData(NRBASE + 15, ItemClassification.progression),
}

ap_nightlords = {
    "Gladius, Beast of Night": ItemData(NRBASE + 16, ItemClassification.progression),
    "Adel, Baron of Night": ItemData(NRBASE + 17, ItemClassification.progression),
    "Gnoster, Wisdom of Night": ItemData(NRBASE + 18, ItemClassification.progression),
    "Maris, Fathom of Night": ItemData(NRBASE + 19, ItemClassification.progression),
    "Libra, Creature of Night": ItemData(NRBASE + 20, ItemClassification.progression),
    "Fulghor, Champion of Nightglow": ItemData(NRBASE + 21, ItemClassification.progression),
    "Caligo, Miasma of Night": ItemData(NRBASE + 22, ItemClassification.progression),
    "Heolstor, the Nightlord": ItemData(NRBASE + 23, ItemClassification.progression),
}

# Characters
ap_characters = {
    "Wylder": ItemData(NRBASE + 24, ItemClassification.useful),
    "Ironeye": ItemData(NRBASE + 25, ItemClassification.useful),
    "Guardian": ItemData(NRBASE + 26, ItemClassification.useful),
    "Duchess": ItemData(NRBASE + 27, ItemClassification.useful),
    "Raider": ItemData(NRBASE + 28, ItemClassification.useful),
    "Revenant": ItemData(NRBASE + 29, ItemClassification.useful),
    "Recluse": ItemData(NRBASE + 30, ItemClassification.useful),
    "Executor": ItemData(NRBASE + 31, ItemClassification.useful),
}

#Victory!

ap_victory = {
    "Victory": ItemData(NRBASE + 32, ItemClassification.progression),
}


# In the way that I made items, I added a way to specify how many of an item should exist
# That's why junk has a 0 since how many are created is in the create_junk_items
# There is a better way of doing this but this is my jank
junk_items = {
    # Junk
    "Murk": ItemData(NRBASE + 33, ItemClassification.filler, 0),
    "Sovreign Sigil": ItemData(NRBASE + 34, ItemClassification.filler, 0),

    # Traps
    "Invasion": ItemData(NRBASE + 35, ItemClassification.trap, 0),
    "Spawn enemies": ItemData(NRBASE + 36, ItemClassification.trap, 0)
}

# Junk weights is just how often an item will be chosen when junk is being made
# Bigger item = more likely to show up
junk_weights = {
    "Murk": 40,
    "Sovreign Sigil": 20
}

# This makes a really convenient list of all the other dictionaries
# (fun fact: {} is a dictionary)
item_table = {
    **ap_memory_fragments,
    **ap_characters,
    **ap_nights,
    **ap_nightlords,
    **ap_shifting_earths,
    **ap_victory,
    **junk_items
}