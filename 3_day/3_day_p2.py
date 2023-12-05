class Engine:

    def __init__(self, filename):
        self.matrix = self.read_file(filename)
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])
        self.gear = '*'

    def read_file(self, filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file]

    def adjacent_to_two_numbers_gear_ratio(self, x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        visited = set()
        adj_nums = []

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height and (nx,ny) not in visited and self.matrix[ny][nx].isdigit():
                lx, rx = nx, nx

                while lx > 0 and (lx - 1, ny) not in visited and self.matrix[ny][lx - 1].isdigit():
                    lx -= 1
                    visited.add((lx, ny))

                while rx < self.width - 1 and (rx + 1, ny) not in visited and self.matrix[ny][rx + 1].isdigit():
                    rx += 1
                    visited.add((rx, ny))

                number = int(self.matrix[ny][lx:rx + 1])
                adj_nums.append(number)
        if len(adj_nums) == 2:
            return adj_nums[0] * adj_nums[1]
        else:
            return 0


    def sum_gear_part_numbers(self):
        total_sum = 0
        for y in range(self.height):
            x = 0
            while x < self.width:
                if self.matrix[y][x] == self.gear:
                    total_sum += self.adjacent_to_two_numbers_gear_ratio(x, y)
                x += 1
        return total_sum

filename = 'input.txt'
# filename = 'test_input.txt'
engine = Engine(filename)
print(engine.sum_gear_part_numbers())