# Hi I am jdriver ( higher then jioe )
from jioe import jioe

class jdriver(jioe):
	def __init__(self):
		self.SLAVE_Y = 4
		self.SLAVE_X = 7
		self.MASTER_X = 1
		self.MASTER_Y = 0
		jioe.__init__(self) 
		
	def local_spider_move(self, rect, speed):
		new_rect = rect.move(
			self.all_axis[self.SLAVE_X] * speed, self.all_axis[self.SLAVE_Y] * speed )
		return new_rect