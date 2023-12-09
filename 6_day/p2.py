class WaitForItP2:
    def __init__(self):
        self.file_lines = []
        self.time = 0
        self.distance = 0

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
                self.time = int(values.replace(" ", ""))
            if title == "distance":
                self.distance = int(values.replace(" ", ""))

    def calculate_distance_reached(self, speed, max_travel_time):
        return speed * max_travel_time
    
    def find_num_ways_to_beat_record(self):
        race_records = []

        travel_time = self.time
        hold_button_time = 0
        while hold_button_time <= self.time and travel_time >= 0:
            distance_reached = self.calculate_distance_reached(hold_button_time, travel_time)
            if distance_reached > self.distance:
                race_records.append(distance_reached)

            hold_button_time += 1
            travel_time -= 1
        
        return len(race_records)

filename = "input.txt"
# filename = "test_input.txt"

wait = WaitForItP2()
wait.read_file(filename)
wait.format_file_data()
print(wait.find_num_ways_to_beat_record())
