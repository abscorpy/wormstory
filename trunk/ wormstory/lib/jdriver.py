# Hi I am jdriver ( higher then jioe )
from jioe import jioe

class jdriver(jioe):
	def __init__(self):
		self.SLAVE_Y = 7
		self.SLAVE_X = 4
		self.MASTER_X = 0
		self.MASTER_Y = 1
		
		self.SLAVE_X_still = self.SLAVE_Y_still = 0
		
		jioe.__init__(self)
		
	def reset_still(self, x_button, y_button, x_still, y_still):
		if self.all_axis[x_button]  and  self.all_axis[y_button]: 
			x_still = self.all_axis[x_button]
			y_still = self.all_axis[y_button]
		elif self.all_axis[x_button] and not self.all_axis[y_button]:
			x_still = self.all_axis[x_button]
			y_still = 0
		elif not self.all_axis[x_button] and self.all_axis[y_button]:
			x_still = 0
			y_still = self.all_axis[y_button]
		return x_still, y_still
		
	def local_spider_move(self, rect, speed):
		self.SLAVE_X_still, self.SLAVE_Y_still = self.reset_still(
			self.SLAVE_X, self.SLAVE_Y, self.SLAVE_X_still, self.SLAVE_Y_still)
		new_rect = rect.move(
			self.SLAVE_X_still * speed, self.SLAVE_Y_still * speed )
		return new_rect