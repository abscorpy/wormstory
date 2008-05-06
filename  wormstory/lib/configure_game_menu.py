# Hi I am configure menu

from menu import menu
from configure_menu_items import speed_item, max_item, keep_item

class configure_game_menu(menu):
	def _add_item(self):						
		self.g.m_list = [ speed_item(self.g, (10,60), self.s),
						max_item(self.g, (10,90), self.s),
						keep_item(self.g, (10,120), self.s)
						]
						