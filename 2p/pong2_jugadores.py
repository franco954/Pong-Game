


import pygame, random
pygame.init()



# Colores

black = (0, 0 ,0)
white = (255, 255, 255)
red = (255, 0, 0)
blue = (0, 0, 255)
screen_size = (800, 600)
player_width = 15
player_height = 90



screen = pygame.display.set_mode(screen_size)
clock = pygame.time.Clock()


# cordenadas y vel jugador 1
player1_x_coor = 50
player1_y_coor = 300 - 45
player1_y_speed = 0

# cordenadas y vel jugador 2
player2_x_coor = 750 - player_width
player2_y_coor = 300 - 45
player2_y_speed = 0


# cordenadas de la pelota

pelota_x = 400
pelota_y = 300
pelota_speed_x = 2.8
pelota_speed_y = 2.8


# puntos hechos

puntoG = False

punto_player1 = 0
punto_player2 = 0


# texto puntos
game_over = False


while not game_over:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game_over = True
		if event.type == pygame.KEYDOWN:
			# jugador 1
			if event.key == pygame.K_w:
				player1_y_speed = -6
			if event.key == pygame.K_s:
				player1_y_speed = 6
			# jugador 2
			if event.key == pygame.K_UP:
				player2_y_speed = -6
			if event.key == pygame.K_DOWN:
				player2_y_speed = 6

		if event.type == pygame.KEYUP:
			# jugador 1
			if event.key == pygame.K_w:
				player1_y_speed = 0
			if event.key == pygame.K_s:
				player1_y_speed = 0
			# jugador 2
			if event.key == pygame.K_UP:
				player2_y_speed = 0
			if event.key == pygame.K_DOWN:
				player2_y_speed = 0
	
	# zona de logica
	if pelota_y > 590 or pelota_y < 10:
		pelota_speed_y *= -1

	# revisa si la pelota sale del lado derecho
	if pelota_x > 800:
		pelota_x = 400
		pelota_y = 300
		# si sale de la pantalla invierte direccion
		pelota_speed_x = 2.8
		pelota_speed_y = 2.8
		pelota_speed_x *= -1
		pelota_speed_y *= -1
		punto_player1 += 1
	


		# revisa si la pelota sale del lado izquierdo
	if pelota_x < 0:
		pelota_x = 400
		pelota_y = 300
		# si sale de la pantalla invierte direccion
		pelota_speed_x = 2.8
		pelota_speed_y = 2.8
		pelota_speed_x *= -1
		pelota_speed_y *= -1
		punto_player2 += 1

	

	# MOD COR PARA DAR MOV A LOS JUGADORES
	player1_y_coor += player1_y_speed
	player2_y_coor += player2_y_speed

	# mov pelota

	pelota_x += pelota_speed_x
	pelota_y += pelota_speed_y



	screen.fill(black)
	# zona de dibujo

	jugador1 = pygame.draw.rect(screen, red, (player1_x_coor, player1_y_coor, player_width, player_height))
	jugador2 = pygame.draw.rect(screen, blue, (player2_x_coor, player2_y_coor, player_width, player_height))
	pelota = pygame.draw.circle(screen, white, (pelota_x, pelota_y), 10)
	

	# colisiones
	if pelota.colliderect(jugador1) or pelota.colliderect(jugador2):
		pelota_speed_x *= -1.2

	
	# marcador de puntos
	miFuente = pygame.font.Font(None, 25)
	miTexto = miFuente.render(str(punto_player1) + " - " + str(punto_player2), 0, (white))


	# if punto_player1 == 3 and punto_player2 < 3:
	# 	textoGanador = pygame.font.Font(None, 25)
	# 	miTexto = miFuente.render(str(punto_player1) + " - " + str(punto_player2), 0, (white))





	screen.blit(miTexto, (380, 20))
	pygame.display.flip() # Actualizar
	clock.tick(60) # FPS
pygame.quit()




