# Hi I am menu_items.

from pygame import *

class menu_item(sprite.Sprite):
	def __init__(self, g, title, location, gotopage=None):
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
			self._active()
		else:
			self._non_active()
	def _active(self):
		self.active = 1
		self.message_title(self.active_color)
		self._post_active()
	def _non_active(self):
		self.active = 0
		self.message_title(self.non_active_color)
		self._post_non_active()
	def _post_active(self):
		pass
	def _post_non_active(self):
		pass