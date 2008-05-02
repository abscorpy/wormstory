# I am the global object for pass to all object.

from game_utils import game_utils
from pygame import *
from driver import driver
from scene import scene
from page import page
from bigblock import bigblock
from menu import menu
from random import randint

class gobj(object):
	def __init__(self):
		
		# pygame init()
		init()
		#mixer.init()
		
		# Obj utils
		self.u = game_utils()
		self.d = driver()
		self.s = scene(self)
		self.p = page(self)
		
		
		#		self.debug = game_debug(self)
		
		# display initialized.
		self.screen_size = 800, 600
		self.screen = display.set_mode(self.screen_size)
		self.main_title = 'Worm Jumping'
		self.set_display()

		# load image
		self.playarea_image = self.u.load_image('S-3-800x600.png')
		self.playinfo_image = self.u.load_image('S-3-200x600.png')
		self.dancing_block_image = self.u.load_image('dancingblock.png', -1)
		self.key_dancing_image = self.u.load_image('keydancing.png', -1)
		self.cow_logo_image = self.u.load_image('mgamelogo.png', -1)
		
		# load sound
		self.knock_sounds = [
			self.u.load_sound('humanbomb.ogg'),
			self.u.load_sound('shotb.ogg'),
			self.u.load_sound('laserrocket.ogg')
			]

		# load fonts
		self.game_info_font = font.Font(self.u.load_font('graffiti.ttf'), 36)
		self.game_info_small_font = font.Font(self.u.load_font('station.ttf'), 24)
		self.sys_font = font.Font(None, 56) 
		
		# load music
		self.u.play_music('coco.ogg')
		
		# Sprite Group init
		self.spider_group = sprite.Group()
		self.block_group = sprite.Group()
		self.groundblock_group = sprite.Group()
		self.menu_group = sprite.Group()

		# base int set.
		self.score = 100
		self.hit_block = 0
		self.game_more = 2
		self.game_speed = 100
		self.menu_choice_id = 0
		
		# page int set.
		self.GAME_PAGE = 1
		self.CONFIGURE_PAGE = 2
		self.QUIT_PAGE = 3
		
		# init menu Obj.
		self.m = menu(self)
	
	def event_update(self):
		events = event.get()
		self.d.io.update(events)

	def set_display(self):
		display.set_caption(self.main_title)
#		display.toggle_fullscreen()

	def set_bigblock(self):
		# init the big blocks
		id = 0
		for y in range(0, 3):
			for x in range(0, 3):
				if y == 1 and x == 1:
					pass
				else:
					self.groundblock_group.add(bigblock(self, id,
						(randint(0,255),randint(0,255),randint(0,255)), (x * 200,y * 200)))
					id += 1

if __name__ == "__main__":
	g = gobj()