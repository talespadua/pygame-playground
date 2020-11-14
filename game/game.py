import pygame

from game.levels.level_factory import LevelFactory
from game.levels.level_renderer import LevelRenderer
from game.settings import Settings


class Game:
    def __init__(self, settings: Settings) -> None:
        self.settings = settings
        pygame.init()
        self.display = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.settings.window_caption)
        self.running = False
        self.current_level = LevelFactory.create(1)
        # self.cell_size = pygame.Vector2(256 / 4, 256 / 8)
        self.cell_size = pygame.Vector2(768 / 8, 768 / 16)
        self.level_renderer = LevelRenderer(self.cell_size, self.display)

    def run(self) -> None:
        self.running = True

        while self.running:
            self.handle_input()
            self.update()
            self.render()
            self.clock.tick(self.settings.frames_per_second)

        pygame.quit()
        quit()

    def update(self) -> None:
        pass

    def render(self) -> None:
        self.level_renderer.render(self.current_level)
        pygame.display.update()

    def handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    return
            return
