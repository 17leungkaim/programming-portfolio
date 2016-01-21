#The Game of Pig

import random

def roll_die(sides):
	r = random.randrange(1, sides+1)
	return r