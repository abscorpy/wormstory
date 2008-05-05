from menu import menu

class menu_menu_choicebar_s(menu):
	def __init__(self, g):
		self.s = g.s.menu_choicebar_s
		menu.__init__(self, g)