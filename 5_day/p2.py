class SeedMaps:
    def __init__(self):
        self.seed_ranges = []
        self.maps = {}

    def read_file(self, filename):
        current_map = None

        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue

                if line.startswith("seeds:"):
                    _, seed_nums = line.split(':')
                    seed_nums = seed_nums.split()
                    for i in range(0, len(seed_nums), 2):
                        start = int(seed_nums[i])
                        length = int(seed_nums[i + 1])
                        self.seed_ranges.append((start, start + length))

                elif 'map:' in line:
                    current_map = line.split(':')[0].replace('-', '_').replace(' ', '_').lower()
                    self.maps[current_map] = []
                else:
                    if current_map:
                        dest_start, source_start, length = [int(num) for num in line.split()]
                        self.maps[current_map].append((source_start, source_start + length, dest_start, dest_start + length))

    def transform_range(self, range, map):
        start, end = range
        transformed_ranges = []

        for src_start, src_end, dest_start, dest_end in map:
            if src_start <= end and src_end >= start:
                intersect_start = max(start, src_start)
                intersect_end = min(end, src_end)
                offset = dest_start - src_start
                transformed_ranges.append((intersect_start + offset, intersect_end + offset + 1))

        if not transformed_ranges:
            return [(start, end)]

        combined_ranges = []
        for r in sorted(transformed_ranges):
            if not combined_ranges or r[0] >= combined_ranges[-1][1]:
                combined_ranges.append(r)
            else:
                combined_ranges[-1] = (combined_ranges[-1][0], r[1])

        return combined_ranges

    def get_lowest_location_number(self):
        current_ranges = self.seed_ranges

        for map_name in self.maps:
            new_ranges = []
            for r in current_ranges:
                transformed_ranges = self.transform_range(r, self.maps[map_name])
                new_ranges.extend(transformed_ranges)
            current_ranges = new_ranges

        return min(start for start, end in current_ranges)

filename = "input.txt"
# filename = "test_input.txt"
seed_maps = SeedMaps()
seed_maps.read_file(filename) 
result = seed_maps.get_lowest_location_number()
print(result)

