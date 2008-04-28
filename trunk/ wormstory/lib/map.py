# Hi I am map obj.
from blocks import redblock as r, blueblock as b, greenblock as g

class map(object):
	def __init__(self, g):
		# init the map.
		self.g = g
		self.map = [[None for i in range(0, 20)] for i in range(0,20)]
	
	def set_map_data(self):
		self.map[0][0] = g
		self.map[0][1] = r
		self.map[0][2] = b
	
	def draw(self):
		for y in range(0, 20):
			for x in range(0, 20):
				topleft = ( x * 30, y * 30 )
				if self.map[y][x] == g or \
					self.map[y][x] == r or self.map[y][x] == b:
					b = self.map[y][x](self.g)
					b.set_rect(topleft)
					self.g.block_group.add(b)
		self.g.block_group.draw(self.g.screen)