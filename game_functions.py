import pygame;
import sys;

def check_events(hero, start_button, game_settings):
	for event in pygame.event.get():
		# this means the user clicked on the RED X
		if event.type == pygame.QUIT:
			# stop the game, user wants out
			sys.exit();
		elif event.type == pygame.MOUSEBUTTONDOWN:
			mouse_x, mouse_y = pygame.mouse.get_pos();
			if start_button.rect.collidepoint(mouse_x, mouse_y):
				game_settings.game_active = True;
				# add sound on start of game, must be a .wav file
				bg_music = pygame.mixer.Sound('boom.wav');
				bg_music.play();
		# check for key press
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT:
				hero.moving_right = True;
			elif event.key == pygame.K_LEFT:
				hero.moving_left = True;
			elif event.key == pygame.K_UP:
				hero.moving_up = True;
			elif event.key == pygame.K_DOWN:
				hero.moving_down = True;
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_RIGHT:
				hero.moving_right = False;
			elif event.key == pygame.K_LEFT:
				hero.moving_left = False;
			elif event.key == pygame.K_UP:
				hero.moving_up = False;
			elif event.key == pygame.K_DOWN:
				hero.moving_down = False;