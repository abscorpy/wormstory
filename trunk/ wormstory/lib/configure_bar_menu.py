# Hi I am configure menu

from menu_menu_choicebar_s import menu_menu_choicebar_s
from menu_choicebar_items import menu_speed

class configure_bar_menu(menu_menu_choicebar_s):
	def _add_item(self):						
		self.g.m_list = [ menu_speed(self.g, (10,60)) ]
						