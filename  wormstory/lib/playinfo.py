# I am the playinfo.

class playinfo(object):
	def __init__(self, g):
		self.g = g
	
	def draw(self):
		self.g.playinfo_image.blit(
			self.g.sys_font.render('123456'), 1,
					(255,100,100)),(5,5))