# I am a bigblock
from pygame import *

class bigblock(sprite.Sprite):
	def __init__(self, g, color, topleft):
		self.g = g
		sprite.Sprite.__init__(self)
		self.image = Surface((200, 200))
		self.image.fill(color)
		self.rect = self.image.get_rect(topleft=topleft)
