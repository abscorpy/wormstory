# I am the background for worm walking.

#from gobj import gobj
from pygame import *

class scene(object):
	def __init__(self, g):
		self.g = g
		self.playarea_s = Surface((600, 600))
		self.playinfo_s = Surface((200, 600))
		self.menu_s = Surface((600, 350))
		
		# Set black.
		self.black_s = Surface((800,600))
		self.black_s.fill((0,0,0))
		
	def draw(self):
		self.g.screen.blit(self.playarea_s, (0,0))
		self.g.screen.blit(self.playinfo_s, (600,0))
		
		self.playarea_s.blit(self.g.playarea_image.convert_alpha(), (0,0))
		self.playinfo_s.blit(self.g.playinfo_image.convert_alpha(), (0,0))
		self.playinfo_s.blit(self.g.dancing_block_image.convert_alpha(), (10,10))
		if not joystick.get_count():
			self.playinfo_s.blit(self.g.key_dancing_image.convert_alpha(), (10,220))
		
		


	