from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario
from AoE2ScenarioParser.datasets.players import PlayerId
from AoE2ScenarioParser.datasets.units import UnitInfo
from AoE2ScenarioParser.datasets.trigger_lists import *


# The path to your scenario folder
input_file = "test2.aoe2scenario"
ouput_path = "C:/Users/neemo/Games/Age of Empires 2 DE/76561198844555824/resources/_common/scenario/" + "output.aoe2scenario"

# The scenario object
scenario = AoE2DEScenario.from_file(input_file)

trigger_manager = scenario.trigger_manager
unit_manager = scenario.unit_manager
map_manager = scenario.map_manager

# Print basic information
print("Map Size:", scenario.map_manager.map_size, "x", scenario.map_manager.map_size)
print("Map Width:", scenario.map_manager.map_width)
print("Map Height:", scenario.map_manager.map_height)

# Get and print information about the first tile
first_tile = scenario.map_manager.get_tile(0, 0)
print("\nFirst Tile Information:")
print(f"Coordinates (x,y): ({first_tile.x}, {first_tile.y})")
print(f"Terrain ID: {first_tile.terrain_id}")
print(f"Elevation: {first_tile.elevation}")
print(f"Layer: {first_tile.layer}")

scenario.map_manager.map_size = 10
scenario.map_manager.map_color_mood = "DEFAULT"

map_manager.set_elevation(elevation=3, x1=1, y1=1, x2=5, y2=5)

unit_manager.add_unit(player=PlayerId.ONE, unit_const=UnitInfo.MILITIA.ID,              x=5, y=2)

source_scenario = AoE2DEScenario.from_file(input_file)
source_trigger_manager = source_scenario.trigger_manager

hello_world_trigger = trigger_manager.add_trigger("Hello Trigger")
# Add display_instructions effect to the new trigger
hello_world_trigger.new_effect.display_instructions(
    display_time=10,
    message="Hello"
)

militia_trigger = trigger_manager.add_trigger("Militia Trigger")

# Add Time Condition
militia_trigger.new_condition.timer(timer=30)

# Add Create Object Effect
militia_trigger.new_effect.create_object(
    object_list_unit_id=UnitInfo.FLEMISH_MILITIA_MALE.ID,
    source_player=PlayerId.ONE,
    location_x=1,
    location_y=1,
)

# After writing the file, move this to C:\Users\USERNAME\Games\Age of Empires 2 DE\PATCHID\resources\_common\scenario
scenario.write_to_file(ouput_path)
