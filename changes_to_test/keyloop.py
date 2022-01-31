import pygame
import pygame.constants

screen_height = 480
h = screen_height/4
screen_width = 640
w = screen_width - screen_width/4
white = (255,255,255)
red = (200,0,0)
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height),)

screen.fill(white)
stickfigure = pygame.image.load("corn.png").convert_alpha()
stickfigure = pygame.transform.scale(stickfigure,(50,120))
x = w
y = h
screen.blit(stickfigure,(x,y))
tr = True
print("start game")
while tr:
	pygame.display.update()
	for event in pygame.event.get():
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_q:
				tr = False
			if event.key == pygame.K_LEFT:
				screen.fill(white)
				x = x - 10
				if x <= 0:
					x = 10
				screen.blit(stickfigure, (x,y))
				print(x)

			if event.key == pygame.K_RIGHT:
				screen.fill(white)
				x = x + 10
				if x >= 600:
					x = 590
				screen.blit(stickfigure, (x,y))
				print(x)
print("Game over yeah")
