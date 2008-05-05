# Hi I am menu_choicebar_item.

from pygame import *
from menu_item import menu_item

class menu_choicebar_item(menu_item):
	def __init__(self, g, title, location, valueobj, step):
		self.valueobj = valueobj
		self.step = step
		menu_item.__init__(self, g, title, location)
	def _set_mix_set_min(self, mix, min):
		self.mix = mix
		self.min = min
	def update(self):
		if self.g.m_list[self.g.menu_choicebar_id] == self:
			self.message_title(self.active_color)
			
			draw.line(self.g.s.menu_choicebar_s, (255, 255, 255), 
				(200, self.rect.centery), (550, self.rect.centery), 3)
				
			if self.valueobj > self.min:
				if self.g.d.io.all_buttons[3]['down']:
					self.valueobj -= self.step
			if self.valueobj < self.mix:
				if self.g.d.io.all_buttons[4]['down']:
					self.valueobj += self.step			
		else:
			self.message_title(self.non_active_color)


# Now, I don't know howto handle it.
#		draw.line(self.g.s.menu_choicebar_s, (255, 255, 255), 
#			(self.rect.top - 10, self.valueobj), (550, self.rect.centery), 3)
		
class menu_speed(menu_choicebar_item):
	def __init__(self, g, location):
		menu_choicebar_item.__init__(self, g, 'SPEED', location, g.game_speed, 1)
		self._set_mix_set_min(100, 50)