# Hi I am configure menu

from menu import menu
from menu_item import menu_item

class configure_menu(menu):
	def _add_item(self):						
		self.g.m_list = [ menu_item(self.g, 'PLAY', (10,60), self.g.GAME_PAGE),
						menu_item(self.g, 'MAIN', (10,90), self.g.MAIN_PAGE),
						menu_item(self.g, 'QUIT', (10,120), self.g.QUIT_PAGE)
						]
						