from gobj import gobj

class main_loop(object):
	def __init__(self):
		self.g = gobj()

def main():
	game = main_loop()
	game.g.set_bigblock()
	game.g.p.mark_page()
	game.g.p.title_page()
	game.g.p.game_page()
	
if __name__ == "__main__":
	main()
