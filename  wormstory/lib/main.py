from gobj import gobj

class main_loop(object):
	def __init__(self):
		self.g = gobj()

def main():
	game = main_loop()
	game.g.set_bigblock()
	game.g.all_pages.title_page()
	game.g.all_pages.game_page()
	
if __name__ == "__main__":
	main()
