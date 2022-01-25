import pygame
from pygame.locals import *

pygame.init()

clock = pygame.time.Clock()
fps = 30
newsize = (320,240)
w = pygame.display.Info().current_w
h = pygame.display.Info().current_h
w = int(w/3)
h = int(h/3)
print(w,h)
screen = pygame.display.set_mode((w,h), RESIZABLE)
pic = pygame.image.load("burningfield.png") 

running = True
while running:
	pygame.event.pump()
	event = pygame.event.wait()
	if event.type == QUIT:
		running = False
	elif event.type == VIDEORESIZE:
		screen.blit(pygame.transform.scale(pic, event.dict['size']),(0,0))
		newsize = screen.get_size()
		print(newsize)
		pygame.display.update()

