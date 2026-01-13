# Look at init or Items.py for more information on imports
from typing import Dict, TYPE_CHECKING
import logging

from .types import LocData

if TYPE_CHECKING:
    from . import APSkeletonWorld

NRBASE = 4918940

# This is technique in programming to make things more readable for booleans
# A boolean is true or false
def did_include_extra_locations(world: "APSkeletonWorld") -> bool:
    return bool(world.options.ExtraLocations)

# This is used by ap and in Items.py
# Theres a multitude of reasons to need to grab how many locations there are
def get_total_locations(world: "APSkeletonWorld") -> int:
    # This is the total that we'll keep updating as we count how many locations there are
    total = 0
    for name in location_table:
        # If we did not turn on extra locations (see how readable it is with that thing from the top)
        # AND the name of it is found in our extra locations table, then that means we dont want to count it
        # So continue moves onto the next name in the table
        if not did_include_extra_locations(world) and name in extra_locations:
            continue

        # If the location is valid though, count it
        if is_valid_location(world, name):
            total += 1

    return total

def get_location_names() -> Dict[str, int]:
    # This is just a fancy way of getting all the names and data in the location table and making a dictionary thats {name, code}
    # If you have dynamic locations then you want to add them to the dictionary as well
    names = {name: data.ap_code for name, data in location_table.items()}

    return names

# The check to make sure the location is valid
# I know it looks like the same as when we counted it but thats because this is an example
# Things get complicated fast so having a back up is nice
def is_valid_location(world: "APSkeletonWorld", name) -> bool:
    if not did_include_extra_locations(world) and name in extra_locations:
        return False
    
    return True

# You might need more functions as well so be liberal with them
# My advice, if you are about to type the same thing in a second time, turn it into a function
# Even if you only do it once you can turn it into a function too for organization

# Heres where you do the next fun part of listing out all those locations
# Its a lot
# My advice, zone out for half an hour listening to music and hope you wake up to a completed list
ap_skeleton_locations = {
    # You can take a peak at Types.py for more information but,
    # LocData is code, region in this instance
    # Regions will be explained more in Regions.py
    # But just know that it's mostly about organization
    # Place locations together based on where they are in the game and what is needed to get there

    #Evergaol Bosses

    #Field Bosses

    #Location Bosses

    #Night 1 Bosses

    "A Fake Location Name": LocData(NRBASE + 1, "Night 1"),
    "A really good restaurant": LocData(NRBASE + 2, "Night 1"),
    "Nuketown": LocData(NRBASE + 3, "Night 1"),
    "Nuketown 2": LocData(NRBASE + 4, "Night 1"),
    "Talk to Sonic": LocData(NRBASE + 5, "Night 1"),
    "Talk to Captain Price": LocData(NRBASE + 6, "Night 1"),
    "TMNT Hangout Spot": LocData(NRBASE + 7, "Night 1"),
    "Above TMNT Hangout Spot": LocData(NRBASE + 8, "Night 1"),
    "Coughing Baby Pickup": LocData(NRBASE + 9, "Night 1"),

    # Night 2 Bosses


    # Nightlords

    "Gladius, Beast of Night": LocData(NRBASE + 10, "Night 3"),
    "Adel, Baron of Night": LocData(NRBASE + 11, "Night 3"),
    "Gnoster, Wisdom of Night": LocData(NRBASE + 12, "Night 3"),
    "Maris, Fathom of Night": LocData(NRBASE + 13, "Night 3"),
    "Libra, Creature of Night": LocData(NRBASE + 14, "Night 3"),
    "Fulghor, Champion of Nightglow": LocData(NRBASE + 15, "Night 3"),
    "Caligo, Miasma of Night": LocData(NRBASE + 16, "Night 3"),
    "Heolstor, the Nightlord": LocData(NRBASE + 17, "Night 3"),

    # Shifting Earth Rewards (for later?)


    # Small Jar Bazaar

    "Wylder's Goblet": LocData(NRBASE + 18, "Roundtable Hold"),
    "Spirit Shelter Grail": LocData(NRBASE + 19, "Roundtable Hold"),
    "Sacred Erdtree Grail": LocData(NRBASE + 20, "Roundtable Hold"),
    "Revenant's Goblet": LocData(NRBASE + 21, "Roundtable Hold"),
    "Recluse's Goblet": LocData(NRBASE + 22, "Roundtable Hold"),
    "Raider's Goblet": LocData(NRBASE + 23, "Roundtable Hold"),
    "Ironeye's Goblet": LocData(NRBASE + 24, "Roundtable Hold"),
    "Guardian's Goblet": LocData(NRBASE + 25, "Roundtable Hold"),
    "Giant's Cradle Grail": LocData(NRBASE + 26, "Roundtable Hold"),
    "Executor's Goblet": LocData(NRBASE + 27, "Roundtable Hold"),
    "Duchess' Goblet": LocData(NRBASE + 28, "Roundtable Hold"),

    "Scenic Flatstone": LocData(NRBASE + 29, "Roundtable Hold"),
    "Polished Tranquil Scene": LocData(NRBASE + 30, "Roundtable Hold"),
    "Polished Luminous Scene": LocData(NRBASE + 31, "Roundtable Hold"),
    "Polished Drizzly Scene": LocData(NRBASE + 32, "Roundtable Hold"),
    "Polished Burning Scene": LocData(NRBASE + 33, "Roundtable Hold"),

    "Grand Tranquil Scene": LocData(NRBASE + 34, "Roundtable Hold"),
    "Grand Luminous Scene": LocData(NRBASE + 35, "Roundtable Hold"),
    "Grand Drizzly Scene": LocData(NRBASE + 36, "Roundtable Hold"),
    "Grand Burning Scene": LocData(NRBASE + 37, "Roundtable Hold"),

    "Delicate Tranquil Scene": LocData(NRBASE + 38, "Roundtable Hold"),
    "Delicate Luminous Scene": LocData(NRBASE + 39, "Roundtable Hold"),
    "Delicate Drizzly Scene": LocData(NRBASE + 40, "Roundtable Hold"),
    "Delicate Burning Scene": LocData(NRBASE + 41, "Roundtable Hold"),

    "Deep Scenic Flatstone": LocData(NRBASE + 42, "Roundtable Hold"),
    "Besmirched Frame": LocData(NRBASE + 43, "Roundtable Hold"),

    "Prattling Pate \"You're beautiful\"": LocData(NRBASE + 44, "Roundtable Hold"),
    "Prattling Pate \"Wonderful\"": LocData(NRBASE + 45, "Roundtable Hold"),
    "Prattling Pate \"Thank You\"": LocData(NRBASE + 46, "Roundtable Hold"),
    "Prattling Pate \"Please Help\"": LocData(NRBASE + 47, "Roundtable Hold"),
    "Prattling Pate \"My beloved\"": LocData(NRBASE + 48, "Roundtable Hold"),
    "Prattling Pate \"Let's get to it\"": LocData(NRBASE + 49, "Roundtable Hold"),
    "Prattling Pate \"Hello\"": LocData(NRBASE + 50, "Roundtable Hold"),
    "Prattling Pate \"Apologies\"": LocData(NRBASE + 51, "Roundtable Hold"),

    "Gesture: What Do You Want?": LocData(NRBASE + 52, "Roundtable Hold"),
    "Gesture: Warm Welcome": LocData(NRBASE + 53, "Roundtable Hold"),
    "Gesture: Strength!": LocData(NRBASE + 54, "Roundtable Hold"),
    "Gesture: Spread Out": LocData(NRBASE + 55, "Roundtable Hold"),
    "Gesture: Sitting Sideways": LocData(NRBASE + 56, "Roundtable Hold"),
    "Gesture: Reverential Bow": LocData(NRBASE + 57, "Roundtable Hold"),
    "Gesture: Rest": LocData(NRBASE + 58, "Roundtable Hold"),
    "Gesture: Rapture": LocData(NRBASE + 59, "Roundtable Hold"),
    "Gesture: Prayer": LocData(NRBASE + 60, "Roundtable Hold"),
    "Gesture: Polite Bow": LocData(NRBASE + 61, "Roundtable Hold"),
    "Gesture: Patches' Crouch": LocData(NRBASE + 62, "Roundtable Hold"),
    "Gesture: Outer Order": LocData(NRBASE + 63, "Roundtable Hold"),
    "Gesture: My Lord": LocData(NRBASE + 64, "Roundtable Hold"),
    "Gesture: Inner Order": LocData(NRBASE + 65, "Roundtable Hold"),
    "Gesture: Hoslow's Oath": LocData(NRBASE + 66, "Roundtable Hold"),
    "Gesture: Heartening Cry": LocData(NRBASE + 67, "Roundtable Hold"),

    #Collector Signboard

}

extra_locations = {
  
}

# Like in Items.py, breaking up the different locations to help with organization and if something special needs to happen to them
event_locations = {

}

# Also like in Items.py, this collects all the dictionaries together
# Its important to note that locations MUST be bigger than progressive item count and should be bigger than total item count
# Its not here because this is an example and im not funny enough to think of more locations
# But important to note
location_table = {
    **ap_skeleton_locations,
    **extra_locations,
    **event_locations
}