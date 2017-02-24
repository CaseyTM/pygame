import pygame;
# we need sys to halt the game
import sys;
from hero import Hero;
from settings import Settings;
from game_functions import check_events;
from pygame.sprite import Group, groupcollide;
from enemy import Enemy;
from button import Start_button;



pygame.init();
# screen_size = (600, 600);
# make a background color
# bg_color = (82,111,53)

# put a message on the status bar so the player knows the name of the game
pygame.display.set_caption("Monster Attack!");
# create object out of our settings class
game_settings = Settings();

screen = pygame.display.set_mode(game_settings.screen_size);
hero_group = Group();

hero = Hero(screen, game_settings);

hero_group.add(hero)
enemies = Group();
enemies.add(Enemy(screen, game_settings));
# make a start button
start_button = Start_button(screen);


while 1:
	check_events(hero, start_button, game_settings);

	screen.fill(game_settings.bg_color);
	for hero in hero_group.sprites():
		if game_settings.game_active:
			hero.update_me();
		hero.draw_me();
	# draw the hero
	# hero.update_me();

	# hero.draw_me();
	for enemy in enemies.sprites():
		if game_settings.game_active:
			enemy.update_me(hero);
		enemy.draw_me();

	hero_died = groupcollide(hero_group, enemies, True, True);
	if hero_died:
		bg_music = pygame.mixer.Sound('lose.wav');
		bg_music.play();
		print "you lost";
		game_settings.game_active = False;
	if game_settings.game_active == False:

		start_button.draw_button();

	pygame.display.flip();
