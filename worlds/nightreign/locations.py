# Look at init or Items.py for more information on imports
from typing import Dict, TYPE_CHECKING
import logging

from .types import LocData

if TYPE_CHECKING:
    from . import APSkeletonWorld

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

    "A Fake Location Name": LocData(20050100),

    #Field Bosses

    #Location Bosses

    #Night 1 Bosses

    "A Fake Location Name": LocData(20050100, "Night 1"),
    "A really good restaurant": LocData(20050101, "Night 1"),
    "Nuketown": LocData(20050103, "Night 1"),
    "Nuketown 2": LocData(20050104, "Night 1"),
    "Talk to Sonic": LocData(20050105, "Night 1"),
    "Talk to Captain Price": LocData(20050106, "Night 1"),
    "TMNT Hangout Spot": LocData(20050107, "Night 1"),
    "Above TMNT Hangout Spot": LocData(20050108, "Night 1"),
    "Coughing Baby Pickup": LocData(20050109, "Night 1"),

    #Night 2 Bosses

    

    #Nightlords

    "Gladius, Beast of Night": LocData(20050100, "Night 3"),
    "Adel, Baron of Night": LocData(20050100, "Night 3"),
    "Gnoster, Wisdom of Night": LocData(20050100, "Night 3"),
    "Maris, Fathom of Night": LocData(20050100, "Night 3"),
    "Libra, Creature of Night": LocData(20050100, "Night 3"),
    "Fulghor, Champion of Nightglow": LocData(20050100, "Night 3"),
    "Caligo, Miasma of Night": LocData(20050100, "Night 3"),
    "Heolstor, the Nightlord": LocData(20050100, "Night 3"),

    #Shifting Earth Rewards (for later?)

    

    #Small Jar Bazaar
    
    "Wylder's Goblet": LocData(20050100, "Roundtable Hold"),
    "Spirit Shelter Grail": LocData(20050100, "Roundtable Hold"),
    "Sacred Erdtree Grail": LocData(20050100, "Roundtable Hold"),
    "Revenant's Goblet": LocData(20050100, "Roundtable Hold"),
    "Recluse's Goblet": LocData(20050100, "Roundtable Hold"),
    "Raider's Goblet": LocData(20050100, "Roundtable Hold"),
    "Ironeye's Goblet": LocData(20050100, "Roundtable Hold"),
    "Guardian's Goblet": LocData(20050100, "Roundtable Hold"),
    "Giant's Cradle Grail": LocData(20050100, "Roundtable Hold"),
    "Executor's Goblet": LocData(20050100, "Roundtable Hold"),
    "Duchess' Goblet": LocData(20050100, "Roundtable Hold"),

    "Scenic Flatstone": LocData(20050100, "Roundtable Hold"),
    "Polished Tranquil Scene": LocData(20050100, "Roundtable Hold"),
    "Polished Luminous Scene": LocData(20050100, "Roundtable Hold"),
    "Polished Drizzly Scene": LocData(20050100, "Roundtable Hold"),
    "Polished Burning Scene": LocData(20050100, "Roundtable Hold"),

    "Grand Tranquil Scene": LocData(20050100, "Roundtable Hold"),
    "Grand Luminous Scene": LocData(20050100, "Roundtable Hold"),
    "Grand Drizzly Scene": LocData(20050100, "Roundtable Hold"),
    "Grand Burning Scene": LocData(20050100, "Roundtable Hold"),

    "Delicate Tranquil Scene": LocData(20050100, "Roundtable Hold"),
    "Delicate Luminous Scene": LocData(20050100, "Roundtable Hold"),
    "Delicate Drizzly Scene": LocData(20050100, "Roundtable Hold"),
    "Delicate Burning Scene": LocData(20050100, "Roundtable Hold"),

    "Deep Scenic Flatstone": LocData(20050100, "Roundtable Hold"),
    "Besmirched Frame": LocData(20050100, "Roundtable Hold"),

    "Prattling Pate \"You're beautiful\"": LocData(20050100, "Roundtable Hold"),
    "Prattling Pate \"Wonderful\"": LocData(20050100, "Roundtable Hold"),
    "Prattling Pate \"Thank You\"": LocData(20050100, "Roundtable Hold"),
    "Prattling Pate \"Please Help\"": LocData(20050100, "Roundtable Hold"),
    "Prattling Pate \"My beloved\"": LocData(20050100, "Roundtable Hold"),
    "Prattling Pate \"Let's get to it\"": LocData(20050100, "Roundtable Hold"),
    "Prattling Pate \"Hello\"": LocData(20050100, "Roundtable Hold"),
    "Prattling Pate \"Apologies\"": LocData(20050100, "Roundtable Hold"),

    "Gesture: What Do You Want?": LocData(20050100, "Roundtable Hold"),
    "Gesture: Warm Welcome": LocData(20050100, "Roundtable Hold"),
    "Gesture: Strength!": LocData(20050100, "Roundtable Hold"),
    "Gesture: Spread Out": LocData(20050100, "Roundtable Hold"),
    "Gesture: Sitting Sideways": LocData(20050100, "Roundtable Hold"),
    "Gesture: Reverential Bow": LocData(20050100, "Roundtable Hold"),
    "Gesture: Rest": LocData(20050100, "Roundtable Hold"),
    "Gesture: Rapture": LocData(20050100, "Roundtable Hold"),
    "Gesture: Prayer": LocData(20050100, "Roundtable Hold"),
    "Gesture: Polite Bow": LocData(20050100, "Roundtable Hold"),
    "Gesture: Patches' Crouch": LocData(20050100, "Roundtable Hold"),
    "Gesture: Outer Order": LocData(20050100, "Roundtable Hold"),
    "Gesture: My Lord": LocData(20050100, "Roundtable Hold"),
    "Gesture: Inner Order": LocData(20050100, "Roundtable Hold"),
    "Gesture: Hoslow's Oath": LocData(20050100, "Roundtable Hold"),
    "Gesture: Heartening Cry": LocData(20050100, "Roundtable Hold"),

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