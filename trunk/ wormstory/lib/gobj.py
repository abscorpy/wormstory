# I am the global object for pass to all object.

from game_utils import game_utils
from pygame import *
from jdriver import jdriver

class gobj(object):
	def __init__(self):
		
		# init utils
		self.u = game_utils()
		
		# pygame init()
		init()
		mixer.init()
		# display initialized.
		self.screen_size = 800, 600
		self.screen = display.set_mode(self.screen_size)
		self.main_title = 'Worm Jumping'
		self.set_display()

		self.playarea_image = self.u.load_image('S-3-800x600.png')
		self.playinfo_image = self.u.load_image('S-3-200x600.png')
		self.dancing_block_image = self.u.load_image('dancingblock.png', -1)
		self.knock_sounds = [
			self.u.load_sound('humanbomb.ogg'),
			self.u.load_sound('shotb.ogg'),
			self.u.load_sound('laserrocket.ogg')
			]

		self.j = jdriver()
		self.game_info_font = font.Font(self.u.load_font('graffiti.ttf'), 36)
		self.game_info_small_font = font.Font(self.u.load_font('station.ttf'), 24)
		self.sys_font = font.Font(None, 56) 
		self.u.play_music('coco.ogg')
		self.spider_group = sprite.Group()
		self.block_group = sprite.Group()
		self.groundblock_group = sprite.Group()
#		self.debug = game_debug(self)
		self.score = 100
		self.hit_block = 0
		self.game_more = 2
		self.game_speed = 100
	
	def event_update(self):
		events = event.get()
		self.j.update(events)

	def set_display(self):
		display.set_caption(self.main_title)
#		display.toggle_fullscreen()

if __name__ == "__main__":
	g = gobj()