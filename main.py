import pygame
import time
import random
import sys

# Colour variables
black = (0, 0, 0)
white = (255, 255, 255)
asphalt = (119, 119, 119)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
yellow = (255, 255, 0)
magenta = (255, 0, 255)
fuchsia = (255, 25, 255)
cyan = (0, 255, 255)
light_cyan = (56, 255, 255)
light_yellow = (255, 255, 102)

# Resolution
resolution = width, height = 800, 600

# Loading images
icon = pygame.image.load("media/wheel.svg")
grass = pygame.image.load("media/grass.jpg")
yellow_strip = pygame.image.load("media/yellow_strip.jpg")
white_strip = pygame.image.load("media/strip.jpg")
intro_background = pygame.image.load("media/the_background.jpg")

# Pygame init
pygame.init()
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("2D Car Racing Game")
pygame.display.set_icon(icon)
screen.fill(asphalt)

# Time module              
clock = pygame.time.Clock()
clock.tick()

# Player
class Player:
    def __init__(self):
        self.x = 370
        self.y = 470
        self.width = 56
        self.height = 125
        self.bound_width_min = 130
        self.bound_width_max = 620
        self.car_img = pygame.transform.scale(
            pygame.image.load("media/car7.jpg").convert_alpha(),
            (self.width, self.height)
        )

    def draw(self):
        screen.blit(self.car_img, (self.x, self.y))

# Function for adding background
def background():

    screen.blit(grass, (0, 0))
    screen.blit(grass, (700, 0))
    screen.blit(yellow_strip, (400, 0))
    screen.blit(yellow_strip, (400, 100))
    screen.blit(yellow_strip, (400, 200))
    screen.blit(yellow_strip, (400, 300))
    screen.blit(yellow_strip, (400, 400))
    screen.blit(yellow_strip, (400, 500))
    screen.blit(yellow_strip, (400, 600))
    screen.blit(white_strip, (120, 0))
    screen.blit(white_strip, (680, 0))


# Function for sending message after car crashes
def crash():
    font = pygame.font.Font("media/BarcadeBrawlRegular-plYD.ttf", 49)
    crashed_message = font.render("GAME OVER", True, (0, 0, 0))
    screen.blit(crashed_message, (200, 200))
    pygame.display.update()
    time.sleep(2)

# Function for score card
def score_card(score, level):
    font = pygame.font.Font("media/BarcadeBrawlRegular-plYD.ttf", 14)
    score = font.render("Score: " + str(score), True, black)
    level = font.render("Level: " + str(level), True, black)
    screen.blit(level, (10, 50))
    screen.blit(score, (10, 100))

# Obstacle
def obstacle(obs_x, obs_y, obs):
    if obs == 0:
        obs_pic = pygame.image.load("media/car2.jpg")
    elif obs == 1:
        obs_pic = pygame.image.load("media/car3.jpg")
    elif obs == 2:
        obs_pic = pygame.image.load("media/car4.jpg")
    elif obs == 3:
        obs_pic = pygame.image.load("media/car5.jpg")
    elif obs == 4:
        obs_pic = pygame.image.load("media/car6.jpg")
    elif obs == 5:
        obs_pic = pygame.image.load("media/car7.jpg")

    screen.blit(obs_pic, (obs_x, obs_y))

# Text object
def text_object(text, font, colour):
    text_surface = font.render(text, True, colour)
    return text_surface, text_surface.get_rect()

# Intro screen
def intro_screen():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        screen.blit(intro_background, (0, 0))

        small_text = pygame.font.Font("media/AtariFontFullVersion-ZJ23.ttf", 20)
        big_text = pygame.font.Font("media/AtariFontFullVersion-ZJ23.ttf", 49)
        title = big_text.render("Dodge Racer", True, (0, 0, 0))
        screen.blit(title, (120, 50))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Start button
        if (80 >= mouse[0] or mouse[0] >= 230) or mouse[1] <= 500 or mouse[1] >= 550:
            pygame.draw.rect(screen, magenta, (80, 500, 150, 50))
        else:
            pygame.draw.rect(screen, fuchsia, (80, 500, 150, 50))
            if click == (1, 0, 0):
                game_loop()

        text_surface, text_rect = text_object("START", small_text, white)
        text_rect.center = ((80 + (150 / 2)), (500 + (50 / 2)))
        screen.blit(text_surface, text_rect)
        # Start button ends here

        # Help button
        if (320 >= mouse[0] or mouse[0] >= 470) or mouse[1] <= 500 or mouse[1] >= 550:
            pygame.draw.rect(screen, cyan, (320, 500, 150, 50))
        else:
            pygame.draw.rect(screen, light_cyan, (320, 500, 150, 50))
            if click == (1, 0, 0):
                help_screen()

        text_surface, text_rect = text_object("HELP", small_text, white)
        text_rect.center = ((320 + (150 / 2)), (500 + (50 / 2)))
        screen.blit(text_surface, text_rect)
        # Help button ends here

        # Quit button
        if (560 >= mouse[0] or mouse[0] >= 710) or mouse[1] <= 500 or mouse[1] >= 550:
            pygame.draw.rect(screen, yellow, (560, 500, 150, 50))
        else:
            pygame.draw.rect(screen, light_yellow, (560, 500, 150, 50))
            if click == (1, 0, 0):
                pygame.quit()
                quit()

        text_surface, text_rect = text_object("QUIT", small_text, white)
        text_rect.center = ((560 + (150 / 2)), (500 + (50 / 2)))
        screen.blit(text_surface, text_rect)
        # Quit button ends here

        pygame.display.update()


# Help screen
def help_screen():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        screen.blit(intro_background, (0, 0))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        small_text = pygame.font.Font("media/AtariFontFullVersion-ZJ23.ttf", 20)

        text_surface, text_rect = text_object("HOW TO PLAY THE GAME", small_text, black)
        text_rect.center = (400, 100)
        screen.blit(text_surface, text_rect)

        text_surface, text_rect = text_object("Dodge as many cars as you can", small_text, white)
        text_rect.center = (400, 200)
        screen.blit(text_surface, text_rect)

        text_surface, text_rect = text_object("Don't go off the road", small_text, white)
        text_rect.center = (400, 250)
        screen.blit(text_surface, text_rect)

        text_surface, text_rect = text_object("<-, -> to move", small_text, white)
        text_rect.center = (400, 300)
        screen.blit(text_surface, text_rect)

        text_surface, text_rect = text_object("s to accelerate", small_text, white)
        text_rect.center = (400, 350)
        screen.blit(text_surface, text_rect)

        text_surface, text_rect = text_object("d to decelerate", small_text, white)
        text_rect.center = (400, 400)
        screen.blit(text_surface, text_rect)

        # Back button
        if (320 >= mouse[0] or mouse[0] >= 470) or mouse[1] <= 500 or mouse[1] >= 550:
            pygame.draw.rect(screen, cyan, (320, 500, 150, 50))
        else:
            pygame.draw.rect(screen, light_cyan, (320, 500, 150, 50))
            if click == (1, 0, 0):
                intro_screen()

        text_surface, text_rect = text_object("BACK", small_text, white)
        text_rect.center = ((320 + (150 / 2)), (500 + (50 / 2)))
        screen.blit(text_surface, text_rect)

        pygame.display.update()
        clock.tick(30)


# Game loop
def game_loop():
    player = Player()
    playerX_dx, playerY_dy = 0, 0
    running = True
    obstacle_speed = 10
    level_speed = obstacle_speed
    obs = 0
    obs_x = random.randrange(130, 620)
    obs_y = -750
    enemy_width = 56
    enemy_height = 125
    car_passed = 0
    score = 0
    level = 1

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    while running:
        screen.fill(asphalt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Keystrokes
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    playerX_dx = -5
                if event.key == pygame.K_RIGHT:
                    playerX_dx = +5
                if event.key == pygame.K_s:
                    obstacle_speed += 2
                if event.key == pygame.K_d:
                    if obstacle_speed < level_speed:
                        obstacle_speed = level_speed
                    else:
                        obstacle_speed -= 2

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    playerX_dx = 0

        player.x += playerX_dx
        background()

        obs_y -= (float(obstacle_speed) / 4)
        obstacle(obs_x, obs_y, obs)
        obs_y += float(obstacle_speed)

        player.draw()
        score_card(int(score), level)

        if player.x <= player.bound_width_min:
            player.x = player.bound_width_min
            crash()
            if click == (1, 0, 0):
                intro_screen()
        elif player.x >= player.bound_width_max:
            player.x = player.bound_width_max
            crash()
            if click == (1, 0, 0):
                intro_screen()

        if obs_y > height:
            obs_y = 0 - enemy_height
            obs_x = random.randrange(130, 620)
            obs = random.randrange(0, 6)
            car_passed += 1
            score = car_passed * 319 / 304

            if score % 100 == 0:
                level += 1
                obstacle_speed += 5
                level_speed += 5

        if player.y < obs_y + enemy_height:
            if player.x > obs_x and player.x < obs_x + enemy_width \
                    or \
                    player.x + player.width > obs_x and player.x + player.width  < obs_x + enemy_width:
                # Right side:
                # if player.x > obs_x or player.x + player.width > obs_x
                # Left side:
                # if player.x < obs_x + obs_width or player.x + player.width < obs_x + enemy_width

                crash()
                if click == (1, 0, 0):
                    intro_screen()


        pygame.display.update()
        clock.tick(60)

intro_screen()
game_loop()
pygame.quit()
quit()
sys.exit()