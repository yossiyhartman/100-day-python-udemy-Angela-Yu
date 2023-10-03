import math

def paint_calculator(width: float, height: float, coverage: float):

    surface = width * height

    nr_paint_cans = math.ceil(surface / coverage)

    print(f'You need {nr_paint_cans} of cans')


t_height = int(input('Height of wall: '))
t_width = int(input('width of wall: '))
t_coverage = 5

paint_calculator(height = t_height, width = t_width, coverage = t_coverage)