import pygame;
# get the sprite parent class
from pygame.sprite import Sprite;


class Hero(Sprite):
	def __init__(self,screen,settings):
		super(Hero,self).__init__();
		self.image = pygame.image.load('hero.png')
		# self.image = pygame.transform.scale(self.image,(1000,200))
		self.screen = screen;
		# create a rect prop that will be the dimensions and location of its available in get rect b/c this is a pygame image
		self.rect = self.image.get_rect();
		# now that we have the screen object fom main, get the size
		self.screen_rect = screen.get_rect();
		print self.screen_rect;
		# this will put the middle of the hero at the middle of the screen
		self.rect.centery = self.screen_rect.centery;
		# this will put the left side of our hero at the left side of the screen
		self.rect.left = self.screen_rect.left;
		# set up the movement booleans that init with FALSE
		self.moving_right = False;
		self.moving_left = False;
		self.moving_up = False;
		self.moving_down = False;
		self.speed = settings.speed;
	def update_me(self):
		# if user is pushin left, move my self.rect left etc
		if self.moving_right:
			# the hero moving_right booean is true, so update the hero location
			self.rect.centerx += 10 * self.speed;
		elif self.moving_left:
			self.rect.centerx -= 10 * self.speed;
		if self.moving_up:
			self.rect.centery -= 10 * self.speed;
		elif self.moving_down:
			self.rect.centery += 10 * self.speed;


	def draw_me(self):
		self.screen.blit(source = self.image, dest = self.rect);
