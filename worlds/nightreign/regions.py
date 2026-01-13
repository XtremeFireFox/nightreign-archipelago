from BaseClasses import Region
from .types import APSkeletonLocation
from .locations import location_table
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from . import APSkeletonWorld

# This is where you will create your imaginary game world
# IE: connect rooms and areas together
# This is NOT where you'll add requirements for how to get to certain locations thats in Rules.py
# This is also long and tediouos
def create_regions(world: "APSkeletonWorld"):
    # The functions that are being used here will be located at the bottom to view
    # The important part is that if its not a dead end and connects to another place then name it
    # Otherwise you can just create the connection. Not that naming it is bad
    menu = create_region(world, "Menu")
    # You can technically name your connections whatever you want as well
    # You'll use those connection names in Rules.py
    roundtable_hold = create_region_and_connect(world, "Roundtable Hold", "Menu -> Roundtable Hold", menu)
    night_1 = create_region_and_connect(world, "Night 1", "Roundtable Hold -> Night 1", roundtable_hold)
    night_2 = create_region_and_connect(world, "Night 2", "Night 1 -> Night 2", night_1)
    night_3 = create_region_and_connect(world, "Night 3", "Night 2 -> Night 3", night_2)

def create_region(world: "APSkeletonWorld", name: str) -> Region:
    reg = Region(name, world.player, world.multiworld)

    # When we create the region we go through all the locations we made and check if they are in that region
    # If they are and are valid, we attach it to the region
    for (key, data) in location_table.items():
        if data.region == name:
            location = APSkeletonLocation(world.player, key, data.ap_code, reg)
            reg.locations.append(location)
    world.multiworld.regions.append(reg)
    return reg

# This runs the create region function while also connecting to another region
# Just simplifies process since you woill be connecting a lot of regions
def create_region_and_connect(world: "APSkeletonWorld",
                               name: str, entrancename: str, connected_region: Region) -> Region:
    reg: Region = create_region(world, name)
    connected_region.connect(reg, entrancename)
    return reg