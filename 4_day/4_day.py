class Game:

    def __init__(self, filename):
        self.cards = {}
        self.read_file(filename)

    def read_file(self, filename):
        with open(filename, 'r') as file:
            for line in file:
                line = line.strip()
                card_num, winning_list, my_list = self.format_data(line)
                self.cards[card_num] = {'winning_nums': winning_list, 'my_nums': my_list, 'count': 1}

    def format_data(self, line):
        card_part, numbers_part = line.split(':')
        card_num = int(card_part.split()[1])

        left_numbers, right_numbers = numbers_part.split('|')
        left_list = [int(num) for num in left_numbers.split() if num.strip()]
        right_list = [int(num) for num in right_numbers.split() if num.strip()]

        return card_num, left_list, right_list

    def calculate_card_total(self):
        total = 0
        for key, value in self.cards.items():
            set1 = set(value['winning_nums'])
            set2 = set(value['my_nums'])
            matches = len(set1.intersection(set2))
            self.cards[key]['matches'] = matches
        for key, value in self.cards.items():
            total += self.cards[key]['count']
            if self.cards[key]['matches'] > 0:
                for i in range(key+1, key+self.cards[key]['matches']+1):
                    self.cards[i]['count'] += ( 1 * value['count'])
        return total

filename = 'input.txt'
# filename = 'test_input.txt'
game = Game(filename)
print(game.calculate_card_total())