# Hi I am jdriver ( higher then jioe )
from jioe import jioe

class jdriver(jioe):
	def __init__(self):
		self.SLAVE_Y = 7
		self.SLAVE_X = 4
		self.MASTER_X = 0
		self.MASTER_Y = 1
		
		# add a still logic
		self.SLAVE_Y_still = 0
		self.SLAVE_X_still = 0
		
		jioe.__init__(self) 
		
	def local_spider_move(self, rect, speed):		
		if self.all_axis[self.SLAVE_X]  and  self.all_axis[self.SLAVE_Y]: 
			self.SLAVE_X_still = self.all_axis[self.SLAVE_X]
			self.SLAVE_Y_still = self.all_axis[self.SLAVE_Y]
		elif self.all_axis[self.SLAVE_X] and not self.all_axis[self.SLAVE_Y]:
			self.SLAVE_X_still = self.all_axis[self.SLAVE_X]
			self.SLAVE_Y_still = 0
		elif not self.all_axis[self.SLAVE_X] and self.all_axis[self.SLAVE_Y]:
			self.SLAVE_X_still = 0
			self.SLAVE_Y_still = self.all_axis[self.SLAVE_Y]
			
		new_rect = rect.move(
			self.SLAVE_X_still * speed, self.SLAVE_Y_still * speed )
		return new_rect