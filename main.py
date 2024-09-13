import pygame
import pygame.freetype
from sys import exit
import config
import components
import population

pygame.init()
clock = pygame.time.Clock()
population = population.Population(500)
font = pygame.freetype.SysFont('Times New Roman', 30)

def generate_pipes():
    config.pipes.append(components.Pipes(config.win_width))

def quit_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

def main():
    pipes_spawn_time = 10

    while True:
        quit_game()

        config.window.fill((0, 0, 0))

        config.ground.draw(config.window)

        if pipes_spawn_time <= 0:
            generate_pipes()
            pipes_spawn_time = 200
        pipes_spawn_time -= 1

        for p in config.pipes:
            p.draw(config.window)
            p.update()
            if p.off_screen:
                config.pipes.remove(p)
        
        if not population.extinct():
            population.update_live_players()
        else:
            config.pipes.clear()
            population.natural_selection()

        # Convert max_lifespan to seconds
        max_lifespan_seconds = population.max_lifespan / 60

        # Display the maximum lifespan in seconds on the screen
        font.render_to(config.window, (10, 10), f"Longest Survivor: {max_lifespan_seconds:.2f} seconds", (255, 255, 255))

        clock.tick(60)
        pygame.display.flip()

main()
