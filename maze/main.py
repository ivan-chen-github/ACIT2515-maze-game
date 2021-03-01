import pygame
import pygame.locals
from models.player import Player
from models.tiles import Item
from models.tiles import Finish
from models.tiles import Wall
from models.maze import Maze

def main():
    """
    Main function to run the game
    """
    pygame.init()

    window = pygame.display.set_mode((1000, 1000))
    window.set_colorkey((255, 255, 255))
    clock = pygame.time.Clock()

    maze = Maze("maze.txt")
    player = Player()
    wall_list = []
    for y, line in enumerate(maze._layout):
            for x, char in enumerate(line):
                if char == "x":
                    new_wall = Wall(x*50, y*50)
                    wall_list.append(new_wall)
                if char == "e":
                    finish = Finish(x*50, y*50)
                if char == "p":
                    player.rect.x = x*50
                    player.rect.y = y*50
    item_locs = []
    item_list = []
    items = 0
    while items < 4:
        loc = maze.find_random_spot()
        if loc not in item_locs:
            
            item_locs.append(loc)
            x, y = loc
            new_item = Item(x*50, y*50)
            item_list.append(new_item)
            items += 1
    

    arial = pygame.font.SysFont('arial', 18)

    running = True
    while running:
        window.fill((255, 255, 255))

        clock.tick(60)

        text = f"wall_list length: ${item_locs}"
        text_surface = arial.render(text, True, (0, 0, 0))
        window.blit(text_surface, (0, 950))

        for event in pygame.event.get():
            if event.type == pygame.locals.QUIT:
                running = False
            elif event.type == pygame.locals.KEYDOWN:
                if event.key in (pygame.locals.K_ESCAPE, pygame.locals.K_q):
                    running = False

        keys = pygame.key.get_pressed()
        if keys[pygame.locals.K_RIGHT]:
            #-- move the player right by 20 pixels
            player.rect.x = min(player.rect.x + 10, 400)
        elif keys[pygame.locals.K_LEFT]:
            #-- move the player left by 20 pixels
            player.rect.x = max(player.rect.x - 10, 0)

        #draw everything. This stuff should probably be in a view
        window.blit(player.image, player.rect)
        window.blit(finish.image, finish.rect)
        for item in item_list:
            window.blit(item.image, item.rect)
        for wall in wall_list:
            window.blit(wall.image, wall.rect)
        pygame.display.update()

if __name__ == "__main__":
    main()
