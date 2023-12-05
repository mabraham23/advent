class Engine:

    def __init__(self, filename):
        self.matrix = self.read_file(filename)
        self.height = len(self.matrix)
        self.width = len(self.matrix[0])
        self.symbols = self.find_symbols()

    def read_file(self, filename):
        with open(filename, 'r') as file:
            return [line.strip() for line in file]

    def find_symbols(self):
        symbols = set()
        for line in self.matrix:
            for char in line:
                if not char.isdigit() and char != '.':
                    symbols.add(char)
        return symbols

    def is_adjacent_to_symbol(self, x, y):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.width and 0 <= ny < self.height:
                if self.matrix[ny][nx] in self.symbols:
                    return True
        return False

    def sum_part_numbers(self):
        total_sum = 0
        for y in range(self.height):
            x = 0
            while x < self.width:
                if self.matrix[y][x].isdigit():
                    start_x = x
                    while x < self.width and self.matrix[y][x].isdigit():
                        x += 1
                    number = int(self.matrix[y][start_x:x])
                    if any(self.is_adjacent_to_symbol(ix, y) for ix in range(start_x, x)):
                        total_sum += number
                else:
                    x += 1
        return total_sum

filename = 'input.txt'
engine = Engine(filename)
print(engine.sum_part_numbers())