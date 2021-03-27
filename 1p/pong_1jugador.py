


import pygame, sys, random
pygame.init()





tamaño = (600, 600)
ventana = pygame.display.set_mode(tamaño)
reloj = pygame.time.Clock()

# ----- pelota -----

# color 
blanco = (255, 255, 255)
negro = (0, 0 ,0)
rojo = (255, 0 , 0)

# cordenadas
pel_x = 300
pel_y = 0 

# velocidad 

pel_x_vel = 5
pel_y_vel = 5


pygame.mouse.set_visible(0)

# barra

barra_x = 300
barra_y = 500

barra_x_vel = 0 





while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				barra_x_vel = -6
			if event.key == pygame.K_RIGHT:
				barra_x_vel = 6
				
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				barra_x_vel = 0
			if event.key == pygame.K_RIGHT:
				barra_x_vel = 0

	# barra
	barra_x += barra_x_vel

	# logica
	pel_x += pel_x_vel
	pel_y += pel_y_vel


	if pel_x > 580 or pel_x < 0:
		pel_x_vel *= -1	

	if pel_y < 0:
		pel_y_vel *= -1

	if pel_y > 580:
		pel_x = 300
		pel_y = 0


	if barra_y == pel_y:
		if barra_x == pel_x:
			pel_x_vel *=-1
			pel_y_vel *=-1


	# dibujo
	ventana.fill(negro)
	#pelota
	pelota = pygame.draw.rect(ventana, rojo, (pel_x, pel_y, 20, 20))
	# dibujo barra
	barraDes = pygame.draw.rect(ventana, blanco, (barra_x, barra_y, 100, 10))



	if pelota.colliderect(barraDes):
			pel_y_vel *= -1





	pygame.display.flip()
	reloj.tick(60)





