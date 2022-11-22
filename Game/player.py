import pygame
import animation

pygame.init()
screen = pygame.display.set_mode((1280,720))
pygame.display.set_caption('TANUJ YO')
game_icon = pygame.image.load('HeroKnight/game_icon.png').convert_alpha()
pygame.display.set_icon(game_icon)
clock = pygame.time.Clock()
run = True

#ground
ground = pygame.image.load('HeroKnight/ground.png').convert_alpha()
ground = pygame.transform.scale(ground,(1280,720))
ground_rect = ground.get_rect(topleft = (0,500))

#player
player = pygame.image.load('HeroKnight/Idle/HeroKnight_Idle_0.png').convert_alpha()
player = pygame.transform.scale2x(player)
player_rect = player.get_rect(bottomleft = (500,400))
player_mask = pygame.mask.from_surface(player)

ANIME = animation.Animation()

jump = False
dir = 'xr'
vel_y = 10
current_frame = 0


while run:
    attack = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    screen.fill('sky blue')
    screen.blit(ground,ground_rect)

    player_rect.y += 5
    if player_rect.y >= 400:
        player_rect.y = 400

    keys=pygame.key.get_pressed()

    if keys[pygame.K_LSHIFT] and jump is False:
        jump = True
    if jump is True:
        player_rect.y -= vel_y * 4
        vel_y -= 0.5
        if vel_y < -10:
            jump = False
            vel_y = 10
        if dir == 'xr':
            screen.blit(ANIME.update(0.1,3),player_rect)
        else:
            screen.blit(pygame.transform.flip(ANIME.update(0.1,3),True,False),player_rect)

    if keys[pygame.K_d]:
        attack = False
        dir = 'xr'
        player_rect.x +=3 
        screen.blit(ANIME.update(0.15,2) ,player_rect)

    if keys[pygame.K_a]:
        attack = False
        dir = 'xl'
        player_rect.x -= 3
        screen.blit(pygame.transform.flip(ANIME.update(0.1,2),True,False),player_rect)

    if keys[pygame.K_f] and attack == True:
        attack = True
        if dir == 'xr':
            screen.blit(ANIME.update(0.1,4),player_rect)
        else:
            screen.blit(pygame.transform.flip(ANIME.update(0.1,4),True,False),player_rect)


    if keys[pygame.K_d] or keys[pygame.K_a] or keys[pygame.K_f] or keys[pygame.K_LSHIFT]:
        pass
    else:
        if dir == 'xr':
            screen.blit(ANIME.update(0.1,1),player_rect)
        else:
            screen.blit(pygame.transform.flip(ANIME.update(0.1,1),True,False),player_rect)

    pygame.display.update()
    clock.tick(60)