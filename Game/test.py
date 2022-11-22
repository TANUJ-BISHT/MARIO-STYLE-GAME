import pygame, sys



class Player(pygame.sprite.Sprite):
	def __init__(self, pos_x, pos_y):
		super().__init__()
		self.attack_animation = False
		self.sprites = []
		self.sprites.append(pygame.image.load('HeroKnight/Run/HeroKnight_run_0.png'))
		self.sprites.append(pygame.image.load('HeroKnight/Run/HeroKnight_run_1.png'))
		self.sprites.append(pygame.image.load('HeroKnight/Run/HeroKnight_run_2.png'))
		self.sprites.append(pygame.image.load('HeroKnight/Run/HeroKnight_run_3.png'))
		self.sprites.append(pygame.image.load('HeroKnight/Run/HeroKnight_run_4.png'))
		self.sprites.append(pygame.image.load('HeroKnight/Run/HeroKnight_run_5.png'))
		self.sprites.append(pygame.image.load('HeroKnight/Run/HeroKnight_run_6.png'))
		self.sprites.append(pygame.image.load('HeroKnight/Run/HeroKnight_run_7.png'))
		self.sprites.append(pygame.image.load('HeroKnight/Run/HeroKnight_run_8.png'))
		self.sprites.append(pygame.image.load('HeroKnight/Run/HeroKnight_run_9.png'))
		self.current_sprite = 0
		self.image = self.sprites[self.current_sprite]

		self.rect = self.image.get_rect()
		self.rect.topleft = [pos_x,pos_y]

	def attack(self):
		self.attack_animation = True

	def update(self,speed):
		if self.attack_animation == True:
			self.current_sprite += speed
			if int(self.current_sprite) >= len(self.sprites):
				self.current_sprite = 0


		self.image = self.sprites[int(self.current_sprite)]

# General setup
pygame.init()
clock = pygame.time.Clock()
run_1 = True

# Game Screen
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("Sprite Animation")

# Creating the sprites and groups
moving_sprites = pygame.sprite.Group()
player = Player(100,100)
moving_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run_1 = False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LSHIFT]:
        player.attack()
    screen.fill((0,0,0))
    moving_sprites.draw(screen)
    moving_sprites.update(0.25)
    pygame.display.flip()
    clock.tick(60)