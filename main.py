import pygame
from src.obstacles import SpriteAnimation
from src.player import Animation
import random

def load_random_obstacle(melon_filename, pumpkin_filename):
    obstacle_type = random.choice(["melon", "pumpkin"])
    x = 1080

    if obstacle_type == "melon":
        animation = SpriteAnimation(melon_filename)
    else:
        animation = SpriteAnimation(pumpkin_filename)

    return animation, obstacle_type, x

def handle_collision(player, obstacle):
    print("Game Over!")
    player.reset_position()
    obstacle.reset_position()

def main():
    pygame.init()

    width, height = 1080, 608
    screen = pygame.display.set_mode((width, height))
    background = pygame.image.load('background/background.png')
    floor = pygame.image.load('background/floor.png')
    pygame.display.set_caption('SYLVAN ESCAPE')

    melon_filename = 'asset/melon/animation_melon.png' 
    pumpkin_filename = 'asset/pumkin/animation_pumkin.png'

    player = Animation("asset/player/run/Run.png", initial_position=(100, 300))
    animation, obstacle_type, x = load_random_obstacle(melon_filename, pumpkin_filename)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.jump()

        if player.is_collision(animation):
            handle_collision(player, animation)

        screen.blit(background, (0, 0))
        screen.blit(floor, (-5, 75))

        animation.update()
        animation.draw(screen)

        if x <= -34:
            animation, obstacle_type, x = load_random_obstacle(melon_filename, pumpkin_filename)
        x -= 5

        player.update()
        player.draw(screen)
        player.clock_tick()

        pygame.display.flip()
        clock.tick(30)

if __name__ == "__main__":
    main()
