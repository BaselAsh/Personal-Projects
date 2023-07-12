import pygame
import os



WIDTH, HEIGHT = 900, 500 
BG_COLOR = (0, 0, 0)
WHITE = (255, 255, 255)
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FPS = 60
VEL = 5
BORDER = pygame.Rect(WIDTH / 2 - 5, 0, 10, HEIGHT)

SHIP_WIDTH, SHIP_HEIGHT = 55, 40

YELLOW_SHIP_IMAGE = pygame.image.load(
    os.path.join("Assets", "spaceship_yellow.png")
)
YELLOW_SHIP = pygame.transform.rotate(
    pygame.transform.scale(YELLOW_SHIP_IMAGE, (SHIP_WIDTH, SHIP_HEIGHT)),
    270,
)
RED_SHIP_IMAGE = pygame.image.load(os.path.join("Assets", "spaceship_red.png"))
RED_SHIP = pygame.transform.rotate(
    pygame.transform.scale(RED_SHIP_IMAGE, (SHIP_WIDTH, SHIP_HEIGHT)), 90
)


def draw_window(color, yellow, red):
    WIN.fill(color)
    pygame.draw.rect(WIN, WHITE, BORDER)
    WIN.blit(YELLOW_SHIP, (yellow.x, yellow.y))
    WIN.blit(RED_SHIP, (red.x, red.y))
    pygame.display.update()


def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > -10:  # LEFT
        yellow.x -= VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > -5:  # UP
        yellow.y -= VEL
    if (
        keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 10
    ):  # DOWN
        yellow.y += VEL
    if (
        keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x + 15
    ):  # RIGHT
        yellow.x += VEL


def red_handle_movment(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > -5:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 10:  # DOWN
        red.y += VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH + 25:  # RIGHT
        red.x += VEL


def main():
    yellow = pygame.Rect(100, 210, SHIP_WIDTH, SHIP_HEIGHT)
    red = pygame.Rect(800, 210, SHIP_WIDTH, SHIP_HEIGHT)

    clock = pygame.time.Clock()
    run = True
    while run:
        pygame.display.set_caption("Basel's Game")
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        draw_window(BG_COLOR, yellow, red)

        keys_pressed = pygame.key.get_pressed()

        yellow_handle_movement(keys_pressed, yellow)
        red_handle_movment(keys_pressed, red)

    pygame.quit()


if __name__ == "__main__":
    main()
