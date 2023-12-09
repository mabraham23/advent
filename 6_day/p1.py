class WaitForItP1:
    def __init__(self):
        self.file_lines = []
        self.times = []
        self.distances = []

    def read_file(self, filename):
        if not filename:
            return f"No filename provided!\n"
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                self.file_lines.append(line)
    
    def format_file_data(self):
        for line in self.file_lines:
            title, values = line.split(":")
            title = title.lower()
            if title == "time":
                values = [int(val) for val in values.split()]
                self.times = values
            if title == "distance":
                values = [int(val) for val in values.split()]
                self.distances = values

    def calculate_distance_reached(self, speed, max_travel_time):
        return speed * max_travel_time
    
    def find_num_ways_to_beat_record(self):
        race_records = []
        for race_num in range(0, len(self.times)):
            race_records.append([])
            max_race_time = self.times[race_num]
            race_record = self.distances[race_num]

            travel_time = max_race_time
            hold_button_time = 0
            while hold_button_time <= max_race_time and travel_time >= 0:
                distance_reached = self.calculate_distance_reached(hold_button_time, travel_time)
                if distance_reached > race_record:
                    race_records[race_num].append(distance_reached)

                hold_button_time += 1
                travel_time -= 1
        
        total = 1
        for records in race_records:
            total *= len(records)
        
        return total

filename = "input.txt"
# filename = "test_input.txt"

wait = WaitForItP1()
wait.read_file(filename)
wait.format_file_data()
total = wait.find_num_ways_to_beat_record()
print(total)
