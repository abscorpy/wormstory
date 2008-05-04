# Hi I am menu_items.

from pygame import *

class menu_item(sprite.Sprite):
	def __init__(self, g, title, location, gotopage):
		sprite.Sprite.__init__(self)
		self.g = g
		self.title = title
		self.gotopage = gotopage
		self.non_active_color = (0,100,0)
		self.active_color = (0, 150, 0)
		self.message_title(self.non_active_color)
		self.rect = self.image.get_rect(topleft=location)
	def message_title(self, color):
		self.image = self.g.menu_info_font.render(self.title, 1, color)
	def update(self):
		if self.g.m_list[self.g.menu_choice_id] == self:
			self.message_title(self.active_color)
		else:
			self.message_title(self.non_active_color)

class menu_play(menu_item):
	def __init__(self, g, gotopage, location):
		menu_item.__init__(self, g, 'PLAY', location, gotopage)

class menu_configure(menu_item):
	def __init__(self, g, gotopage, location):
		menu_item.__init__(self, g, 'CONFIGURE', location, gotopage)

class menu_quit(menu_item):
	def __init__(self, g, gotopage, location):
		menu_item.__init__(self, g, 'QUIT', location, gotopage)
		
class menu_back(menu_item):
	def __init__(self, g, gotopage, location):
		menu_item.__init__(self, g, 'BACK', location, gotopage)
		
class menu_main(menu_item):
	def __init__(self, g, gotopage, location):
		menu_item.__init__(self, g, 'MAIN', location, gotopage)