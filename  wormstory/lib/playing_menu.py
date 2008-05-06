# Hi I am playing menu

from menu import menu
from menu_item import menu_item

class playing_menu(menu):
	def _add_item(self):						
		self.g.m_list = [ menu_item(self.g, 'BACK',  (10,60), self.g.GAME_PAGE),
						menu_item(self.g, 'CONFIGURE', (10,90), self.g.CONFIGURE_PAGE),
						menu_item(self.g, 'QUIT', (10,120), self.g.QUIT_PAGE)
						]
						