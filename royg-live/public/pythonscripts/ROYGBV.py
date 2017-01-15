import math, random, time, pygame, sys
from pygame.locals import *

init_grid_size = 1
window_size = 1024
num_iterations = 8

color_map = {
	'R': (209, 0, 0),
	'O': (255, 102, 34),
	'Y': (255, 218, 33),
	'G': (51, 221, 0),
	'B': (17, 51, 204),
	'V': (51, 0, 68)}

color_model = {
	'R': {'R': .3, 'O': .2, 'Y': .1, 'G': .1, 'B': .1, 'V': .2},
	'O': {'R': .2, 'O': .3, 'Y': .2, 'G': .1, 'B': .1, 'V': .1},
	'Y': {'R': .1, 'O': .2, 'Y': .3, 'G': .2, 'B': .1, 'V': .1},
	'G': {'R': .1, 'O': .1, 'Y': .2, 'G': .3, 'B': .2, 'V': .1},
	'B': {'R': .1, 'O': .1, 'Y': .1, 'G': .2, 'B': .3, 'V': .2},
	'V': {'R': .2, 'O': .1, 'Y': .1, 'G': .1, 'B': .2, 'V': .3}}

def random_select(distribution):
    random_value = random.uniform(0, 1)
    sum_value = 0.0
    for key, value in distribution.iteritems():
        sum_value += value
        if (random_value < sum_value): 
            output = key
            break
    return (output)

def generate_color(input_color):
	return (random_select(color_model[input_color]))

def display_grid(grid_colors):
	grid_size = len(grid_colors)
	tile_size = window_size / grid_size
	for i in range(grid_size):
		for j in range(grid_size):
			pygame.draw.rect(DISPLAYSURF, color_map[grid_colors[i][j]], (i * tile_size, j * tile_size, tile_size, tile_size))
	pygame.display.update()

valid_input = False
grid_colors = []

init_grid_colors = raw_input('Type in a string of ' + str(init_grid_size ** 2) + ' color character(s) (R, O, Y, G, B, or V): ')

if(init_grid_colors != ' '):
    valid_input = True

if(valid_input):
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((window_size, window_size), FULLSCREEN)
    for i in range(init_grid_size):
            row_colors = []
            for j in range(init_grid_size):
                    row_colors.append(init_grid_colors[0])
                    init_grid_colors = init_grid_colors[1::]
            grid_colors.append(row_colors)
    display_grid(grid_colors)
    time.sleep(1)
    print ('5...')
    time.sleep(1)
    print ('4...')
    time.sleep(1)
    print ('3...')
    time.sleep(1)
    print ('2...')
    time.sleep(1)
    print ('1...')

    for i in range(num_iterations):
            new_grid_colors = []
            for j in range(len(grid_colors) * 2):
                    row_colors = []
                    for k in range(len(grid_colors) * 2):
                            row_colors.append(generate_color(grid_colors[j / 2][k / 2]))
                    new_grid_colors.append(row_colors)
            grid_colors = new_grid_colors
            display_grid(grid_colors)
            time.sleep(.1 / math.log(i + 8, 8))
