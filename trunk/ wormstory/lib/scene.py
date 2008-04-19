# I am the background for worm walking.

from gobj import gobj
from pygame import *

class scene(object):
	def __init__(self, g):
		self.g = g
		self.g.screen.blit(self.g.playarea_image.convert_alpha(), (0,0))
		self.g.screen.blit(self.g.playinfo_image.convert_alpha(), (600,0))
		self.g.screen.blit(self.g.red_block_image.convert_alpha(), (100,20))
		display.flip()
		while True:
			self.g.u.base_event()
	
if __name__ == "__main__":
	g = gobj()
	s = scene(g)
	