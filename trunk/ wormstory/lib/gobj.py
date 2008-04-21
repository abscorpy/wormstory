# I am the global object for pass to all object.

from game_utils import game_utils
from pygame import *
from jioe import jioe

class gobj(object):
	def __init__(self):
		
		# init utils
		self.u = game_utils()
		
		# pygame init()
		init()
		# display initialized.
		self.screen_size = 800, 600
		self.screen = display.set_mode(self.screen_size)
		self.main_title = 'Worm story'
		self.set_display()
		
		self.game_intro_image = self.u.load_image('block.png')
		self.playarea_image = self.u.load_image('S-3-800x600.png')
		self.playinfo_image = self.u.load_image('h12-200x600.png')
		self.red_block_image = self.u.load_image('rsblock.png')
		self.blue_block_image = self.u.load_image('bsblock.png')
		self.green_block_image = self.u.load_image('gsblock.png')
		
		self.joystick = joystick.Joystick(0)
		self.joystick.init()
		self.j = jioe()
		self.sys_font = font.Font(None, 36) 
		
	def event_update(self):
		events = event.get()
		self.j.update(events)

	def set_display(self):
		display.set_caption(self.main_title)
#		display.toggle_fullscreen()

if __name__ == "__main__":
	
#	screen = display.set_mode((800, 600))
#	pygame.display.set_caption('Warm Story')
#	pygame.mouse.set_visible(0)
	g = gobj()