# Hi I am configure menu

from menu import menu
from menu_item import menu_item

class configure_game_menu(menu):
	def _add_item(self):						
		self.g.m_list = [ menu_item(self.g, 'SPEED', (10,60)),
						menu_item(self.g, 'MAX', (10,90)),
						menu_item(self.g, 'KEEP', (10,120))
						]
						