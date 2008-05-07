# Hi I am configure_menu_items

from menu_item import menu_item
from choicebar import choicebar

class choicebar_menu_item(menu_item, choicebar):
	def __init__(self, g, title, pos, s, config_obj_value):
		menu_item.__init__(self, g, title, pos)
		choicebar.__init__(self, g, s, (pos[0] + 200, pos[1]), config_obj_value)
	def _set_configobj_value(self, v):
		objvalue = v
	def update(self):
		menu_item.update(self)
		if self.active:
			choicebar.update(self)
	
class speed_item(choicebar_menu_item):
	def __init__(self, g, pos, s):
		choicebar_menu_item.__init__(self, g, 'SPEED', pos, s, g.config_speed)
	def _set_configobj_value(self, v):
		self.g.config_speed = v
		
class max_item(choicebar_menu_item):
	def __init__(self, g, pos, s):
		choicebar_menu_item.__init__(self, g, 'MAX', pos, s, g.config_max)
	def _set_configobj_value(self, v):
		self.g.config_max = v
	
class keep_item(choicebar_menu_item):
	def __init__(self, g, pos, s):
		choicebar_menu_item.__init__(self, g, 'KEEP', pos, s, g.config_keep)
	def _set_configobj_value(self, v):
		self.g.config_keep = v