# I am spider

from pygame import *

class spider(sprite.Sprite):
	"""moves a clenched fist on the screen, following the mouse"""
	def __init__(self, g, center):
		self.g = g
		sprite.Sprite.__init__(self) #call Sprite initializer
		self.image = self.g.u.load_image('spider_s.png', -1)
		self.rect = self.image.get_rect(center=center)

	def update(self):
		pass