#! /usr/bin/env python3
with open('input.txt') as f:
	lines = f.readlines()
f.close()


# 12 red
# 13 green
# 14 blue

# id -> game
total_sum = 0
games = {}
# process the input lines
for line in lines:
    line = line.strip()
    # get the game num
    game_split = line.split(':')
    game = game_split[0]
    game_num = int(game.split(' ')[1])

    # get the pulls
    pulls = game_split[1]
    hands = pulls.split(';')
    colors = {
        'red': 0,
        'blue': 0,
        'green': 0
    }
    for hand in hands:
          draws = hand.split(',')
          for draw in draws:
                draw = draw.strip()
                draw_split = draw.split(' ')
                num_die = int(draw_split[0])
                color_die = draw_split[1]
                if num_die > colors[color_die]:
                      colors[color_die] = num_die
    
    games[game_num] = colors


for id, colors in games.items():
      total_sum += (colors['red'] * colors['green'] * colors['blue'])

print(total_sum) 

        


    
