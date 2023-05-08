import pygame
from fighter import Fighter
pygame.init()

# pravim game window

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("RAČ ROOM")

#frame rate
clock = pygame.time.Clock()
FPS = 60

#boje
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

#neke tu varijable

intro_count = 3
last_count_update = pygame.time.get_ticks()
score = [0, 0]
round_over = False
ROUND_OVER_COOLDOWN = 2000

#define font
count_font = pygame.font.Font("freesansbold.ttf", 80)
score_font = pygame.font.Font("freesansbold.ttf", 30)

#tekst
def tekst(text, font, text_col, x, y):
  img = font.render(text, True, text_col)
  screen.blit(img, (x, y))

# ucitati background
pozadina = pygame.image.load("C:/Users/LENOVO/PycharmProjects/pythonProject/pozadina.png").convert_alpha()
nikola = pygame.image.load("C:/Users/LENOVO/PycharmProjects/pythonProject/nikola.png").convert_alpha()
#funkcija za pozivanje pozadine
def pozovi_pozadinu():
    scaled_pozadina = pygame.transform.scale(pozadina, (SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.blit(scaled_pozadina, (0, 0))

#prikaz napadackog zivota

def draw_health_bar(health, x, y):
    ratio = health / 100
    pygame.draw.rect(screen, WHITE, (x - 5, y - 5, 410, 40))
    pygame.draw.rect(screen, RED, (x,y, 400, 30))
    pygame.draw.rect(screen, YELLOW, (x,y, 400 * ratio, 30))

#dva napadaca
napadac_1 = Fighter(1, 193, 400, False)
napadac_2 = Fighter(2, 695, 400, True)

# game loop
run = True
while run:

    clock.tick(FPS)

    #pozovi pozadinu
    pozovi_pozadinu()

    #health bar
    draw_health_bar(napadac_1.health, 20, 20)
    draw_health_bar(napadac_2.health, 580, 20)

    if (napadac_1.alive == False):
        score[1] += 1
        napadac_1.health = 100
        napadac_2.health = 100
        napadac_1.alive = True
    elif (napadac_2.alive == False):
        score[0] += 1
        napadac_2.health = 100
        napadac_1.health = 100
        napadac_2.alive = True

    #tekst
    tekst("P1: " + str(score[0]), score_font, RED, 20, 60)
    tekst("P2: " + str(score[1]), score_font, BLUE, 580, 60)

    napadac_1.update()
    napadac_2.update()

    #pomeri napadace
    napadac_1.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, napadac_2)
    napadac_2.move(SCREEN_WIDTH, SCREEN_HEIGHT, screen, napadac_1)


    # pozovi_napadaca
    napadac_1.pozovi1(screen)
    napadac_2.pozovi2(screen)

    # event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #update display
    pygame.display.update()

# izaci iz pygame-a
pygame.quit()