# Look at init or Items.py for more information on imports
from typing import Dict, TYPE_CHECKING
import logging

from .types import LocData

if TYPE_CHECKING:
    from . import APSkeletonWorld

NRBASE = 4918940

# This is technique in programming to make things more readable for booleans
# A boolean is true or false


# This is used by ap and in Items.py
# Theres a multitude of reasons to need to grab how many locations there are
def get_total_locations(world: "APSkeletonWorld") -> int:
    # This is the total that we'll keep updating as we count how many locations there are
    total = 0
    for name in location_table:
        # If we did not turn on extra locations (see how readable it is with that thing from the top)
        # AND the name of it is found in our extra locations table, then that means we dont want to count it
        # So continue moves onto the next name in the table

        # If the location is valid though, count it
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

    

    #Field Bosses

    #Location Bosses

    #Night 1 Bosses

    "Demi-Human Queen & Demi-Human Swordmaster": LocData(NRBASE + 1, "Night 1"),
    "Bell Bearing Hunter": LocData(NRBASE + 2, "Night 1"),
    "Gaping Dragon": LocData(NRBASE + 3, "Night 1"),
    "Wormface": LocData(NRBASE + 4, "Night 1"),
    "Valiant Gargoyle": LocData(NRBASE + 5, "Night 1"),
    "The Duke's Dear Freja": LocData(NRBASE + 6, "Night 1"),
    "Night's Cavalry Duo": LocData(NRBASE + 7, "Night 1"),
    "Smelter Demon": LocData(NRBASE + 8, "Night 1"),
    "Battlefield Commander": LocData(NRBASE + 9, "Night 1"),
    "Centipede Demon": LocData(NRBASE + 10, "Night 1"),
    "Tibia Mariner": LocData(NRBASE + 11, "Night 1"),
    "Ulcerated Tree Spirit": LocData(NRBASE + 12, "Night 1"),
    "Grafted Monarch": LocData(NRBASE + 13, "Night 1"),
    "Royal Revenant": LocData(NRBASE + 14, "Night 1"),

    # Night 2 Bosses

    "Fell Omen": LocData(NRBASE + 15, "Night 2"),
    "Tree Sentinel & Royal Cavalrymen": LocData(NRBASE + 16, "Night 2"),
    "Ancient Dragon": LocData(NRBASE + 17, "Night 2"),
    "Crucible Knight & Golden Hippopotamus": LocData(NRBASE + 18, "Night 2"),
    "Outland Commander": LocData(NRBASE + 19, "Night 2"),
    "Great Wyrm": LocData(NRBASE + 20, "Night 2"),
    "Nox Dragonkin Soldier": LocData(NRBASE + 21, "Night 2"),
    "Draconic Tree Sentinel & Royal Cavalrymen": LocData(NRBASE + 22, "Night 2"),
    "Full-Grown Fallingstar Beast": LocData(NRBASE + 23, "Night 2"),
    "Godskin Duo": LocData(NRBASE + 24, "Night 2"),
    "Death Rite Bird": LocData(NRBASE + 25, "Night 2"),
    "Nameless King": LocData(NRBASE + 26, "Night 2"),
    "Dancer of the Boreal Valley": LocData(NRBASE + 27, "Night 2"),

    # Nightlords

    "Gladius, Beast of Night": LocData(NRBASE + 28, "Night 3"),
    "Adel, Baron of Night": LocData(NRBASE + 29, "Night 3"),
    "Gnoster, Wisdom of Night": LocData(NRBASE + 30, "Night 3"),
    "Maris, Fathom of Night": LocData(NRBASE + 31, "Night 3"),
    "Libra, Creature of Night": LocData(NRBASE + 32, "Night 3"),
    "Fulghor, Champion of Nightglow": LocData(NRBASE + 33, "Night 3"),
    "Caligo, Miasma of Night": LocData(NRBASE + 34, "Night 3"),
    "Heolstor, the Nightlord": LocData(NRBASE + 35, "Night 3"),

    #Evergaol Bosses

    "Omen": LocData(NRBASE + 36, "Evergaol"),
    "Grave Warden Duelist": LocData(NRBASE + 37, "Evergaol"),
    "Bloodhound Knight": LocData(NRBASE + 38, "Evergaol"),
    "Stoneskin Lords": LocData(NRBASE + 39, "Evergaol"),
    "Nox Warriors": LocData(NRBASE + 40, "Evergaol"),
    "Beastly Brigade": LocData(NRBASE + 41, "Evergaol"),
    "Beastmen of Farum Azula": LocData(NRBASE + 42, "Evergaol"),
    "Crystalians": LocData(NRBASE + 43, "Evergaol"),
    "Banished Knights": LocData(NRBASE + 44, "Evergaol"),
    "Dragonkin Soldier": LocData(NRBASE + 45, "Evergaol"),
    "Godskin Noble": LocData(NRBASE + 46, "Evergaol"),
    "Godskin Apostle": LocData(NRBASE + 47, "Evergaol"),
    "Crucible Knight (Treespear)": LocData(NRBASE + 48, "Evergaol"),
    "Crucible Knight (Sword)": LocData(NRBASE + 49, "Evergaol"),
    "Ancient Dragon": LocData(NRBASE + 50, "Evergaol"),
    "Godskin Duo": LocData(NRBASE + 51, "Evergaol"),
    "Death Rite Bird": LocData(NRBASE + 52, "Evergaol"),

    # Shifting Earth Rewards (for later?)


    # Small Jar Bazaar

    "Wylder's Goblet": LocData(NRBASE + 53, "Roundtable Hold"),
    "Spirit Shelter Grail": LocData(NRBASE + 54, "Roundtable Hold"),
    "Sacred Erdtree Grail": LocData(NRBASE + 55, "Roundtable Hold"),
    "Revenant's Goblet": LocData(NRBASE + 56, "Roundtable Hold"),
    "Recluse's Goblet": LocData(NRBASE + 57, "Roundtable Hold"),
    "Raider's Goblet": LocData(NRBASE + 58, "Roundtable Hold"),
    "Ironeye's Goblet": LocData(NRBASE + 59, "Roundtable Hold"),
    "Guardian's Goblet": LocData(NRBASE + 60, "Roundtable Hold"),
    "Giant's Cradle Grail": LocData(NRBASE + 61, "Roundtable Hold"),
    "Executor's Goblet": LocData(NRBASE + 62, "Roundtable Hold"),
    "Duchess' Goblet": LocData(NRBASE + 63, "Roundtable Hold"),

    "Scenic Flatstone": LocData(NRBASE + 64, "Roundtable Hold"),
    "Polished Tranquil Scene": LocData(NRBASE + 65, "Roundtable Hold"),
    "Polished Luminous Scene": LocData(NRBASE + 66, "Roundtable Hold"),
    "Polished Drizzly Scene": LocData(NRBASE + 67, "Roundtable Hold"),
    "Polished Burning Scene": LocData(NRBASE + 68, "Roundtable Hold"),

    "Grand Tranquil Scene": LocData(NRBASE + 69, "Roundtable Hold"),
    "Grand Luminous Scene": LocData(NRBASE + 70, "Roundtable Hold"),
    "Grand Drizzly Scene": LocData(NRBASE + 71, "Roundtable Hold"),
    "Grand Burning Scene": LocData(NRBASE + 72, "Roundtable Hold"),

    "Delicate Tranquil Scene": LocData(NRBASE + 73, "Roundtable Hold"),
    "Delicate Luminous Scene": LocData(NRBASE + 74, "Roundtable Hold"),
    "Delicate Drizzly Scene": LocData(NRBASE + 75, "Roundtable Hold"),
    "Delicate Burning Scene": LocData(NRBASE + 76, "Roundtable Hold"),

    "Deep Scenic Flatstone": LocData(NRBASE + 77, "Roundtable Hold"),
    "Besmirched Frame": LocData(NRBASE + 78, "Roundtable Hold"),

    "Prattling Pate \"You're beautiful\"": LocData(NRBASE + 79, "Roundtable Hold"),
    "Prattling Pate \"Wonderful\"": LocData(NRBASE + 80, "Roundtable Hold"),
    "Prattling Pate \"Thank You\"": LocData(NRBASE + 81, "Roundtable Hold"),
    "Prattling Pate \"Please Help\"": LocData(NRBASE + 82, "Roundtable Hold"),
    "Prattling Pate \"My beloved\"": LocData(NRBASE + 83, "Roundtable Hold"),
    "Prattling Pate \"Let's get to it\"": LocData(NRBASE + 84, "Roundtable Hold"),
    "Prattling Pate \"Hello\"": LocData(NRBASE + 85, "Roundtable Hold"),
    "Prattling Pate \"Apologies\"": LocData(NRBASE + 86, "Roundtable Hold"),

    "Gesture: What Do You Want?": LocData(NRBASE + 87, "Roundtable Hold"),
    "Gesture: Warm Welcome": LocData(NRBASE + 88, "Roundtable Hold"),
    "Gesture: Strength!": LocData(NRBASE + 89, "Roundtable Hold"),
    "Gesture: Spread Out": LocData(NRBASE + 90, "Roundtable Hold"),
    "Gesture: Sitting Sideways": LocData(NRBASE + 91, "Roundtable Hold"),
    "Gesture: Reverential Bow": LocData(NRBASE + 92, "Roundtable Hold"),
    "Gesture: Rest": LocData(NRBASE + 93, "Roundtable Hold"),
    "Gesture: Rapture": LocData(NRBASE + 94, "Roundtable Hold"),
    "Gesture: Prayer": LocData(NRBASE + 95, "Roundtable Hold"),
    "Gesture: Polite Bow": LocData(NRBASE + 96, "Roundtable Hold"),
    "Gesture: Patches' Crouch": LocData(NRBASE + 97, "Roundtable Hold"),
    "Gesture: Outer Order": LocData(NRBASE + 98, "Roundtable Hold"),
    "Gesture: My Lord": LocData(NRBASE + 99, "Roundtable Hold"),
    "Gesture: Inner Order": LocData(NRBASE + 100, "Roundtable Hold"),
    "Gesture: Hoslow's Oath": LocData(NRBASE + 101, "Roundtable Hold"),
    "Gesture: Heartening Cry": LocData(NRBASE + 102, "Roundtable Hold"),


    #Collector Signboard

}

# Also like in Items.py, this collects all the dictionaries together
# Its important to note that locations MUST be bigger than progressive item count and should be bigger than total item count
# Its not here because this is an example and im not funny enough to think of more locations
# But important to note
location_table = {
    **ap_skeleton_locations
}