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
	
	def load_font(self, name):
		fullname = data.filepath(name)
		try:
			font = open(fullname, 'rb')
			pygame.font.init()
		except pygame.error, message:
			print 'Cannot load font:', name
			raise SystemExit, message
		return font
	
	def play_music(self, name):
		fullname = data.filepath(name)
		if pygame.mixer:			
			pygame.mixer.music.fadeout(1000)
			pygame.mixer.music.load(fullname)
			pygame.mixer.music.play(-1)
			pygame.mixer.music.set_volume(0.8)
