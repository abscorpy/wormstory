# Hi I am menu_items.

from pygame import *

class menu_item(sprite.Sprite):
	def __init__(self, g, title, location):
		sprite.Sprite.__init__(self)
		self.g = g
		self.title = title
		self.non_active_color = (0,100,0)
		self.active_color = (0, 150, 0)
		self.message_title(self.non_active_color)
		self.rect = self.image.get_rect(topleft=location)
	def message_title(self, color):
		self.image = self.g.game_info_font.render(self.title, 1, color)
	def update(self):
		if self.g.menu_choice_id == self.id:
			self.message_title(self.active_color)
		else:
			self.message_title(self.non_active_color)

class menu_play(menu_item):
	def __init__(self, g, id, location):
		self.id = id
		menu_item.__init__(self, g, 'PLAY', location)

class menu_configure(menu_item):
	def __init__(self, g, id, location):
		self.id = id
		menu_item.__init__(self, g, 'CONFIGURE', location)

class menu_quit(menu_item):
	def __init__(self, g, id, location):
		self.id = id
		menu_item.__init__(self, g, 'QUIT', location)
		
class menu_back(menu_item):
	def __init__(self, g, id, location):
		self.id = id
		menu_item.__init__(self, g, 'BACK', location)