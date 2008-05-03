# Hi I am configure menu

from menu import menu
from menu_items import menu_back, menu_play

class configure_menu(menu):
	def __init__(self, g):
		menu.__init__(self, g)
		print 'gid: %s' %self.g.menu_choice_id
	def _add_item(self):
		self.m.append( menu_play(self.g, 1, (120,200)) )
		self.m.append( menu_back(self.g, 2, (120,250)) )