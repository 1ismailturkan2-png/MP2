import pygame
pygame.init()
Screen1 = pygame.display.set_mode((800,400))
color = (0, 0, 255) 
Screen1.fill(color) 
pygame.display.update()
Game_Active = True
sky_surface = pygame.image.load("sky.png").convert()
sky_surface = pygame.transform.scale(sky_surface,(800,300))
ground_surface = pygame.image.load("ground.png").convert()
ground_surface = pygame.transform.scale(ground_surface,(800,100))
player1 = pygame.image.load("player.png").convert_alpha()


class Characters(pygame.sprite.Sprite):
    def __init__(self, name, image, location, x_velocity):
        super().__init__()
        self.name = name
        self.image = image
        self.rect = image.get_rect(center = location)
        self.location = location
        self.x_velocity = x_velocity
    def update (self):
        self.rect.move_ip(self.x_velocity, 0)
        if self.rect.right > 800 or self.rect.left < 0 :
            self.x_velocity *= -1




P1 = Characters("PLAYER 1 ", player1, (400,200), 1)
Character_Group = pygame.sprite.Group() 
Character_Group.add(P1)
while Game_Active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
           Game_Active = False 
    Screen1.blit(sky_surface,(0,0))
    Screen1.blit(ground_surface,(0,300))
    Character_Group.draw(Screen1)
    Character_Group.update()



    pygame.display.update()
    
