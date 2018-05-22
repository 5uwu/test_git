river_region = {
    'nile': 'egypt',
    'yangtze_river': 'china',
    'henghe': 'india',
}
for k, v in river_region.items():
    print("The " + k.title() + " runs through " + v.title() + ".")

for river in river_region.keys():
    print(river.title())

for region in river_region.values():
    print(region.title())