# Hi I am configure menu

from menu import menu
from menu_item import menu_item

class configure_game_menu(menu):
	def _add_item(self):						
		self.g.m_list = [ menu_item(self.g, 'SPEED', (10,60), confobj=self.g.game_speed),
						menu_item(self.g, 'MAX', (10,90), confobj=self.g.game_more),
						menu_item(self.g, 'KEEP', (10,120), confobj=self.g.game_keep)
						]
						