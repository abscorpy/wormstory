# Hi I am menu_choicebar_item.

from pygame import *
from menu_item import menu_item

class menu_choicebar_item(menu_item):
	def __init__(self, g, title, location, valueobj):
		self.valueobj = valueobj
		menu_item.__init__(self, g, title, location)
	def __set_mix_set_min(self, mix, min):
		self.mix = mix
		self.min = min
	def __update_addon(self):
		pass