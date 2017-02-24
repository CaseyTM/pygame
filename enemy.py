import pygame;
from pygame.sprite import Sprite;
import math;

class Enemy(Sprite):
	def __init__(self, screen, game_settings):
		super(Enemy, self).__init__();
		self.image = pygame.image.load('monster.png');
		self.speed = 2;
		# find the location and size of the image just loaded
		self.rect = self.image.get_rect();
		# find the loc ans size of the screen
		self.screen_rect = screen.get_rect();
		self.screen = screen;
		# set the center of the image
		self.rect.centery = self.screen_rect.centery;
		self.rect.right = self.screen_rect.right;
	def draw_me(self):
		self.screen.blit(self.image, self.rect);
	def update_me(self, hero):
		dx = self.rect.x - hero.rect.x;
		dy = self.rect.y - hero.rect.y;
		dist = math.hypot(dx, dy);
		dx = dx / dist;
		dy = dy / dist;
		self.rect.x -= dx * self.speed;
		self.rect.y -= dy * self.speed;

	def draw_me(self):
		self.screen.blit(self.image, self.rect);