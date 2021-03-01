import pygame

class GameView():
    def __init__(self, walls, fin, items, player):
        self._arial = pygame.font.SysFont('arial', 45)
        self._walls = walls
        self._fin = fin
        self._items = items
        self._player = player
        self._window = pygame.display.set_mode((1000, 1050))
        self._window.set_colorkey((255, 255, 255))

    def draw_map(self):
        self._window.fill((50, 25, 0))

        text = f"Items obtained: {self._player._backpack}"
        text_surface = self._arial.render(text, True, (255, 255, 255))
        self._window.blit(text_surface, (0, 1000))

        self._window.blit(self._player.image, self._player.rect)
        self._items.draw(self._window)
        self._walls.draw(self._window)
        self._fin.draw(self._window)
        pygame.display.update()
