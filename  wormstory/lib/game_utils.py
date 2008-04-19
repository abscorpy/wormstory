# I am the utils for game.

import pygame, data, sys
from pygame.locals import *

## functions
#load sound stolen from chimp tutorial
class game_utils(object):
	def __init__(self):
		pass

	def load_sound(self, name):
		class NoneSound:
			def play(self): pass
		if not pygame.mixer:
			return NoneSound()
		fullname = data.filepath(name)
		try:
			sound = pygame.mixer.Sound(fullname)
		except pygame.error, message:
			print 'Cannot load sound:', fullname
			raise SystemExit, message
		return sound

	def load_image(self, name, colorkey=None):
		fullname = data.filepath(name)
		try:
			image = pygame.image.load(fullname)
		except pygame.error, message:
			print 'Cannot load image:', name
			raise SystemExit, message
		image = image.convert()
		if colorkey is not None:
			if colorkey is -1:
				colorkey = image.get_at((0,0))
			image.set_colorkey(colorkey, RLEACCEL)
		return image

	def base_event(self):
		for e in pygame.event.get():
			if e.type == KEYDOWN:
				if e.key == K_ESCAPE:
					sys.exit()
#				elif e.key == K_h:
#					self._show_help()
#				elif e.key == K_SPACE:
#					return 1
#				elif e.key == K_k:
#					self.si.keyboard_h = 1;
#					return 1
				elif e.key == K_s:
					self._screen_save()