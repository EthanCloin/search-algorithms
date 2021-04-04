import pygame, sys

pygame.init()
pygame.font.init()
# setup for taking input 
screen = pygame.display.set_mode((800, 800))
screen.fill((255, 0 , 0))
font = pygame.font.Font(None, 32)
input_box = pygame.Rect(100, 100, 140, 32)

color_inactive = pygame.Color('lightskyblue3')
color_active = pygame.Color('dodgerblue2')
color = color_inactive
taking_input = False
input_string = ''



running = True
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
			for x in range(0, 800):
				for y in range(0, 800):
					print(screen.get_at((x,y)))
			pygame.quit()
			sys.exit()

		if event.type == pygame.MOUSEBUTTONDOWN:
			if input_box.collidepoint(event.pos):
				taking_input = not taking_input
			else:
				taking_input = False
			color = color_active if taking_input else color_inactive

		if event.type == pygame.KEYDOWN:
			if taking_input: 
				if event.key == pygame.K_RETURN:
					print(input_string)
					input_string = ''
				elif event.key == pygame.K_BACKSPACE:
					input_string = input_string[:-1]
				else:
					input_string += event.unicode

	screen.fill((30, 30, 30))
	text_surface = font.render(input_string, True, color)
	width = max(200, text_surface.get_width()+10)
	input_box.w = width

	screen.blit(text_surface, (input_box.x+5, input_box.y+5))

	pygame.draw.rect(screen, color, input_box, 2)
	pygame.display.flip()











