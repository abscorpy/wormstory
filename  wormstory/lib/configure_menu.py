# Hi I am configure menu

from menu import menu
from menu_items import menu_back, menu_play

class configure_menu(menu):
	def _add_item(self):						
		self.g.m_dict = { 1:menu_play(self.g, self.g.GAME_PAGE, (120,200)),
						2:menu_back(self.g, self.g.MAIN_PAGE, (120,250)) }