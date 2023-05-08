import pygame

class Fighter:
    def __init__(self, player, x, y, flip):
        self.flip = flip
        self.player = player
        self.rect = pygame.Rect((x, y, 80, 150))
        self.vel_y = 0
        self.jump = False
        self.cooldown = False
        self.health = 100
        self.alive = True
        self.update_time = pygame.time.get_ticks()
        self.attack_cooldown = 0

    def move(self, screen_width, screen_height, surface, target):
        SPEED = 10
        dx = 0
        GRAVITACIJA = 2

        #keypress
        key = pygame.key.get_pressed()

        #ne moze da se pomera kad napadne (1 action at a time)
        if self.cooldown == False and self.alive == True:

            #koji igrac
            if self.player == 1:

                # pokretanje
                if key[pygame.K_a]:
                    dx = -SPEED
                if key[pygame.K_d]:
                    dx = SPEED

                # skakanje
                if key[pygame.K_w] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True

                # napad
                if key[pygame.K_e]:
                    self.attack(target)

            if self.player == 2:
                # pokretanje
                if key[pygame.K_LEFT]:
                    dx = -SPEED
                if key[pygame.K_RIGHT]:
                    dx = SPEED

                # skakanje
                if key[pygame.K_UP] and self.jump == False:
                    self.vel_y = -30
                    self.jump = True

                # napad
                if key[pygame.K_RSHIFT]:
                    self.attack(target)

        #dodavanje gravitacije
        self.vel_y += GRAVITACIJA
        dy = self.vel_y

        #bounds
        if self.rect.left + dx < 0:
            dx = -self.rect.left
        if self.rect.right + dx > screen_width:
            dx = screen_width - self.rect.right
        if self.rect.bottom + dy > screen_height - 80:
            self.vel_y = 0
            self.jump = False
            dy = screen_height - 80 - self.rect.bottom

        # okretanje igraca jedan prema drugom

        if target.rect.centerx > self.rect.centerx:
            self.flip = False
        else:
            self.flip = True

        # apply attack cooldown
        if self.attack_cooldown > 0:
             self.attack_cooldown -= 1

        #updateovanje pozicije
        self.rect.x += dx
        self.rect.y += dy

    def update(self):
        if self.health <= 0:
            self.health = 0
            self.alive = False
# 2:jump

    def attack(self, target):
        if self.attack_cooldown == 0:
            self.cooldown = False
            attacking_rect = pygame.Rect(self.rect.centerx - (2 * self.rect.width * self.flip), self.rect.y,
                                         2 * self.rect.width, self.rect.height)
            if attacking_rect.colliderect(target.rect):
                target.health -= 10
                self.cooldown = False
                self.attack_cooldown = 10

    def pozovi1(self, surface):
        pygame.draw.rect(surface, (255, 0, 0), self.rect)
        font = pygame.font.Font('freesansbold.ttf', 32)
        tekst = font.render("P1", True, (255, 0, 0))
        surface.blit(surface, (self.rect.x, self.rect.y), self.rect)
        surface.blit(tekst, (self.rect.x + 20, self.rect.y - 30))
    def pozovi2(self, surface):
        pygame.draw.rect(surface, (0, 0, 255), self.rect)
        font = pygame.font.Font('freesansbold.ttf', 32)
        tekst = font.render("P2", True, (0, 0, 255))
        surface.blit(surface, (self.rect.x, self.rect.y), self.rect)
        surface.blit(tekst, (self.rect.x + 20, self.rect.y - 30))