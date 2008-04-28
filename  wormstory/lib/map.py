# Hi I am map obj.
from blocks import empty, redblock, blueblock, greenblock

class map(object):
	def __init__(self):
		# init the map.
		self.e = empty()
		self.r = redblock()
		self.b = blueblock()
		self.g = greenblock()
		# e is block Object, and this is empty.
		self.line_blocks = [self.e for i in range(0, 20)]
		self.map = [self.line_blocks for i in range(0,20)]
