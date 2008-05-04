# Hi I am menu_items.

from pygame import *
from menu_item import menu_item

class menu_title_item(menu_item):
	def __init__(self, g, title, location, gotopage):
		self.gotopage = gotopage
		menu_item.__init__(self, g, title, location)

class menu_play(menu_title_item):
	def __init__(self, g, gotopage, location):
		menu_title_item.__init__(self, g, 'PLAY', location, gotopage)

class menu_configure(menu_title_item):
	def __init__(self, g, gotopage, location):
		menu_title_item.__init__(self, g, 'CONFIGURE', location, gotopage)

class menu_quit(menu_title_item):
	def __init__(self, g, gotopage, location):
		menu_title_item.__init__(self, g, 'QUIT', location, gotopage)
		
class menu_back(menu_title_item):
	def __init__(self, g, gotopage, location):
		menu_title_item.__init__(self, g, 'BACK', location, gotopage)
		
class menu_main(menu_title_item):
	def __init__(self, g, gotopage, location):
		menu_title_item.__init__(self, g, 'MAIN', location, gotopage)