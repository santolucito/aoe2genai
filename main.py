from AoE2ScenarioParser.scenarios.aoe2_de_scenario import AoE2DEScenario

# The path to your scenario folder
input_file = "9villstart.aoe2scenario"

# The scenario object
scenario = AoE2DEScenario.from_file(input_file)

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

scenario.map_manager.map_size = 100
scenario.map_manager.map_color_mood = "DEFAULT"

# After writing the file, move this to C:\Users\USERNAME\Games\Age of Empires 2 DE\PATCHID\resources\_common\scenario
scenario.write_to_file("test2.aoe2scenario")
