import pygame
import pygame.locals
from models.player import Player
from models.tiles import Item
from models.tiles import Finish
from models.tiles import Wall
from models.maze import Maze
import time

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
    walls = pygame.sprite.Group()
    fin = pygame.sprite.Group()
    for y, line in enumerate(maze._layout):
            for x, char in enumerate(line):
                if char == "x":
                    walls.add(Wall(x*50, y*50))
#                    new_wall = Wall(x*50, y*50)
#                    wall_list.append(new_wall)
                if char == "e":
                    fin.add(Finish(x*50, y*50))
                if char == "p":
                    player.rect.x = x*50
                    player.rect.y = y*50
    item_locs = []
    item_list = []
    item_count = 0
    items = pygame.sprite.Group()
    while item_count < 4:
        loc = maze.find_random_spot()
        if loc not in item_locs:
            
            item_locs.append(loc)
            x, y = loc
            new_item = Item(x*50, y*50)
            items.add(new_item)
            item_list.append(new_item)
            item_count += 1
    cd = False

    arial = pygame.font.SysFont('arial', 45)
    item_get = 0
    running = True
    while running:
        window.fill((255, 255, 255))

        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.KEYUP:
                cd = False

        keys = pygame.key.get_pressed()
        if keys[pygame.locals.K_RIGHT] and cd == False and maze.can_move_to(player.rect.y/50, (player.rect.x+50)/50):
            player.rect.x = min(player.rect.x + 50, 1000)
            cd = True
        elif keys[pygame.locals.K_LEFT]  and cd == False and maze.can_move_to(player.rect.y/50, (player.rect.x-50)/50):
            player.rect.x = max(player.rect.x - 50, 0)
            cd = True
        elif keys[pygame.locals.K_UP] and cd == False and maze.can_move_to((player.rect.y-50)/50, player.rect.x/50):
            player.rect.y = max(player.rect.y - 50, 0)
            cd = True
        elif keys[pygame.locals.K_DOWN] and cd == False and maze.can_move_to((player.rect.y+50)/50, player.rect.x/50):
            player.rect.y = max(player.rect.y + 50, 0)
            cd = True


        
        if pygame.sprite.spritecollide(player, items, dokill=True):
            item_get +=1
        if pygame.sprite.spritecollide(player, fin, dokill=True) and item_get == 4:
            win = True
            running = False
        elif pygame.sprite.spritecollide(player, fin, dokill=True):
            win = False
            running = False

        text = f"Debug: {cd}, also Items obtained: {item_get}"
        text_surface = arial.render(text, True, (0, 0, 0))
        window.blit(text_surface, (0, 950))
        #draw everything. This stuff should probably be in a view

        
        window.blit(player.image, player.rect)
#        window.blit(finish.image, finish.rect)
#        for item in item_list:
#            window.blit(item.image, item.rect)
        items.draw(window)
        walls.draw(window)
        fin.draw(window)
#        for wall in wall_list:
#            window.blit(wall.image, wall.rect)
        pygame.display.update()
    if win == True:
        print("Win")
    elif win == False:
        print("Lose")

if __name__ == "__main__":
    main()
