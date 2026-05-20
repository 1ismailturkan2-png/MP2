import pygame
pygame.init()
Screen1 =  pygame.display.set_mode((800,400))
color = (0, 0, 255) 
Screen1.fill(color) 
pygame.display.update()
Game_Active = True
sky_surface = pygame.image.load("sky.png").convert()
sky_surface = pygame.transform.scale(sky_surface,(800,300))
ground_surface = pygame.image.load("ground.png").convert()
ground_surface = pygame.transform.scale(ground_surface,(800,100))
player = pygame.image.load("player.png").convert_alpha()
player_rect = player.get_rect(center=(400,210))
v_x = 0
v_y = 0
while Game_Active :
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_Active = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                v_y -= 5
            elif event.key == pygame.K_a:  
                v_x -= 5 
            elif event.key == pygame.K_s:
                v_y += 5
            elif event.key == pygame.K_d: 
                v_x += 5
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                v_y += 5
            elif event.key == pygame.K_a:  
                v_x += 5 
            elif event.key == pygame.K_s:
                v_y -= 5
            elif event.key == pygame.K_d: 
                v_x -= 5    
    player_rect.move_ip(v_x, v_y)
    Screen1.blit(sky_surface,(0,0))
    Screen1.blit(ground_surface,(0,300))
    Screen1.blit(player, player_rect)
    pygame.display.update()
    pygame.time.Clock().tick(60)   
