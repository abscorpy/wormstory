# I am a bigblock
from pygame import *
from random import randint

class bigblock(sprite.Sprite):
	def __init__(self, g, id, color, topleft):
		self.g = g
		sprite.Sprite.__init__(self)
		self.image = Surface((200, 200))
		self.rect = self.image.get_rect(topleft=topleft)
		self.id = id
		self.color = color
		self.reset()
	
	def update(self):
		if not self.active:
			r = randint(0, 1000)
			if r < (self.g.game_more + (self.g.hit_block / 5)):
				self.active = 1
				self.image.fill(self.color)
				self.active_time = 0
		else:
			if self.g.j.all_buttons[self.id]['down']:
				self.reset()
				self.g.score += 100
				self.g.hit_block += 1
				sound = randint(0, 2)
				self.g.knock_sounds[sound].play()
			elif self.active_time > (self.g.game_speed - self.g.hit_block):
				self.reset()
				self.g.score -= 50
			else:
				self.active_time += 1
	
	def reset(self):
		self.active = 0
		self.image.fill((0, 0, 0))
		
				
			
			
			
		
