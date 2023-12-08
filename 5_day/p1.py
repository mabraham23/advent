class SeedMaps:
    
    def __init__(self):
        self.seeds = []
        self.maps = {}
        self.map_conversions = {}

    def read_file(self, filename):
        current_map = None

        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                if line.startswith("seeds:"):
                    _, seed_nums = line.split(':')
                    self.seeds = [int(num) for num in seed_nums.split()]
                    continue

                if 'map:' in line:
                    current_map = line.split(':')[0].replace('-', '_').replace(' ', '_').lower()
                    self.maps[current_map] = []
                else:
                    if current_map:
                        self.maps[current_map].append([int(num) for num in line.split()])
                    
    def create_map_conversions(self):
        for map_name, maps in self.maps.items():
            self.map_conversions[map_name] = {}
            for map_entry in maps:
                dest_range_start = map_entry[0]
                source_range_start = map_entry[1]
                range_length = map_entry[2]

                key = (source_range_start, source_range_start + range_length)

                self.map_conversions[map_name][key] = lambda num, src=source_range_start, dest=dest_range_start: (num - src) + dest

    def get_lowest_seed_location(self):
        locations = []
        seeds = self.seeds
        for map_name, ranges in self.map_conversions.items():
            transformed_seeds = []
            for seed in seeds:
                seed_found = False
                # check if seed in in one of the maps ranges
                for ( start, stop ), transform in ranges.items():
                    if start <= seed <= stop:
                        transformed_seed = transform(seed)
                        transformed_seeds.append(transformed_seed)
                        seed_found = True
                        break
                # if the seed was not in any range add it untransformed
                if not seed_found:
                    transformed_seeds.append(seed)
            if map_name == "humidity_to_location_map":
                locations = transformed_seeds
                break
            seeds = transformed_seeds
        return min(locations)

# filename = "test_input.txt"
filename = "input.txt"
seed_maps = SeedMaps()
seed_maps.read_file(filename)
seed_maps.create_map_conversions()
print(seed_maps.get_lowest_seed_location())
