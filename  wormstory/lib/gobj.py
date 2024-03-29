# I am the global object for pass to all object.

from game_utils import game_utils
from pygame import *
from driver import driver
from scene import scene
from page import page
from bigblock import bigblock
from main_menu import main_menu
from configure_menu import configure_menu
from configure_game_menu import configure_game_menu
#from choicebar import choicebar
from playing_menu import playing_menu
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
		self.menu_background_image = self.u.load_image('menu_background.png')
		self.menu_background2_image = self.u.load_image('menu_background2.png')
		
		# load sound
		self.knock_sounds = [
			self.u.load_sound('humanbomb.ogg'),
			self.u.load_sound('shotb.ogg'),
			self.u.load_sound('laserrocket.ogg')
			]
		
		self.click_sounds = [
			self.u.load_sound('click_1d.ogg'),
			self.u.load_sound('click_h1.ogg'),
			self.u.load_sound('clickverb.ogg')
			]
		
		self.page_sounds = [
			self.u.load_sound('book_page_f2.ogg'),
			self.u.load_sound('book_page_s.ogg'),
			self.u.load_sound('book_page_f.ogg'),
			self.u.load_sound('book_page_s2.ogg')
			]

		# load fonts
		self.game_info_font = font.Font(self.u.load_font('graffiti.ttf'), 36)
		self.menu_info_font = font.Font(self.u.load_font('graffiti.ttf'), 24)
		self.game_info_small_font = font.Font(self.u.load_font('station.ttf'), 18)
		self.sys_font = font.Font(None, 56) 
		
		# load music
		self.u.play_music('coco.ogg')
		
		# Sprite Group init
		self.spider_group = sprite.Group()
		self.block_group = sprite.Group()
		self.groundblock_group = sprite.Group()
		self.menu_group = sprite.Group()

		self.init_base_int()
		
		# Set this value for test configure menu.
		self.config_speed = 170.00
		self.config_max = 170.00
		self.config_keep = 170.00
		self.config_music = 170.00
		
		# page int set.
		self.NEW_GAME_PAGE = -1
		self.GAME_PAGE = 1
		self.CONFIGURE_PAGE = 2
		self.QUIT_PAGE = 3
		self.MAIN_PAGE = 4
		
		# init menus Obj.
		self.m_m = main_menu(self, self.s.menu_s, self.menu_background_image)
		self.c_m = configure_menu(self, self.s.menu_s, self.menu_background_image)
		self.p_m = playing_menu(self, self.s.menu_s, self.menu_background_image)
		self.c_g_m = configure_game_menu(self, self.s.menu_choicebar_s, self.menu_background2_image)
#		self.choicebar = choicebar(self, self.s.menu_choicebar_s)
		self.m_list = []
		
	def init_base_int(self):
		# base int set.
		self.score = 100
		self.hit_block = 0
		self.game_more = 2
		self.game_speed = 100
		self.can_replay = 0
		self.menu_choice_id = 0
	
	def event_update(self):
		events = event.get()
		self.d.io.update(events)

	def set_display(self):
		display.set_caption(self.main_title)
		display.toggle_fullscreen()
		
		#non-display mouse curse
		mouse.set_visible(0)

	def set_bigblock(self):
		# init the big blocks
		self.groundblock_group.empty()
		id = 0
		for y in range(0, 3):
			for x in range(0, 3):
				if y == 1 and x == 1:
					pass
				else:
					self.groundblock_group.add(bigblock(self, id,
						(randint(0,255),randint(0,255),randint(0,255)), (x * 200,y * 200)))
					id += 1
		
	def click_sound_play(self):
		sound = randint(0, 2)
		self.click_sounds[sound].play()
		
	def page_sound_play(self):
		sound = randint(0, 3)
		self.page_sounds[sound].play()


if __name__ == "__main__":
	g = gobj()