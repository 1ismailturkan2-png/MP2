import pygame


class Guns_Class:
    def __init__(self, image, name, type, push_back, bullet_speed, ammo, location = None):
        self.name = name
        self.rect = image.get_rect()
        self.image = image
        self.type = type 
        self.push_back = push_back
        self.bullet_speed = bullet_speed
        self.ammo = ammo  


pygame.init() 
screen = pygame.display.set_mode((800, 600))


Kar98_surface = pygame.image.load("Kar98.png").convert_alpha()
Kar98_surface = pygame.transform.scale(Kar98_surface, (80, 30))

AWP_surface = pygame.image.load("AWP.png").convert_alpha()
AWP_surface = pygame.transform.scale(AWP_surface, (80, 30))

Operator_surface = pygame.image.load("Operator.png").convert_alpha()
Operator_surface = pygame.transform.scale(Operator_surface, (80, 30))

Bazooka_surface = pygame.image.load("Bazooka.jpg").convert_alpha()
Bazooka_surface = pygame.transform.scale(Bazooka_surface, (80, 30))

RPG_surface = pygame.image.load("RPG.png").convert_alpha()
RPG_surface = pygame.transform.scale(RPG_surface, (80, 30))




Kar98 = Guns_Class(Kar98_surface, "Kar98" ,"Sniper", 150, 10, 5)
AWP = Guns_Class(AWP_surface, "AWP", "Sniper", 110, 20, 5)
Operator = Guns_Class(Operator_surface, "Operator", "Sniper", 130, 15, 5)
Bazooka = Guns_Class(Bazooka_surface, "Bazooka", "Explosion", 1000, 10, 1)
RPG = Guns_Class(RPG_surface, "RPG", "Explosion", 1000, 7, 2)



Guns_Dictionary = {}
Guns_Dictionary["Kar98"] = Kar98
Guns_Dictionary["AWP"] = AWP
Guns_Dictionary["Operator"] = Operator
Guns_Dictionary["Bazooka"] = Bazooka
Guns_Dictionary["RPG"] = RPG

