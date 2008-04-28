# I am spider

from pygame import *

class block(sprite.Sprite):
	"""moves a clenched fist on the screen, following the mouse"""
	def __init__(self, g):
		self.g = g
		sprite.Sprite.__init__(self) #call Sprite initializer
	def set_rect(self, topleft):
		self.rect = self.image.get_rect(topleft=topleft)

class redblock(block):
	def __init__(self, g):
		block.__init__(self, g)
		self.image = self.g.red_block_image

class blueblock(block):
	def __init__(self, g):
		block.__init__(self, g)
		self.image = self.g.blue_block_image

class greenblock(block):
	def __init__(self, g):
		block.__init__(self, g)
		self.image = self.g.green_block_image