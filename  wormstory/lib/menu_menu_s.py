from menu import menu

class menu_menu_s(menu):
	def __init__(self, g):
		self.s = g.s.menu_s
		menu.__init__(self, g)