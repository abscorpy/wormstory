# I am the global object for pass to all object.

from utils import load_image, load_sound
import pygame

class gobj(object):
	def __init__(self):
		self.game_intro_image = load_image('block.png')
		self.playarea_image = load_image('S-3-800x600.png')
		self.playinfo_image = load_image('h12-200x600.png')
		self.red_block_image = load_image('rsblock.png')
		self.blue_block_image = load_image('bsblock.png')
		self.green_block_image = load_image('gsblock.png')

if __name__ == "__main__":
	pygame.init()
	screen = pygame.display.set_mode((800, 600))
	pygame.display.set_caption('Warm Story')
#	pygame.mouse.set_visible(0)
	g = gobj()