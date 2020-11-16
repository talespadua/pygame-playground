import pygame

from game.game_state import GameState
from game.levels.level_factory import LevelFactory
from game.renderers.map_renderer import MapRenderer
from game.settings import Settings


class Game:
    def __init__(self, settings: Settings) -> None:
        pygame.init()

        self.settings = settings
        self.font = pygame.font.SysFont("Arial", 18)

        self.display = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        self.clock = pygame.time.Clock()
        pygame.display.set_caption(self.settings.window_caption)
        self.running = False
        self.current_level = LevelFactory.create(1)
        self.camera_position = self.current_level.initial_position
        self.game_state = GameState(self.current_level)
        self.level_renderer = MapRenderer(
            self.game_state,
            self.display,
            self.current_level.sprite,
        )

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
        self.game_state.update_camera(self.camera_position)

    def update_fps(self) -> pygame.surface.Surface:
        fps = str(int(self.clock.get_fps()))
        fps_text = self.font.render(fps, True, pygame.Color("coral"))
        return fps_text

    def render(self) -> None:
        self.display.fill((0, 0, 0))
        self.display.blit(self.update_fps(), (10, 0))
        self.level_renderer.render(self.game_state)
        pygame.display.update()

    def handle_input(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    return
                elif event.key == pygame.K_RIGHT:
                    self.camera_position = (
                        self.camera_position[0] + 1,
                        self.camera_position[1],
                    )
                elif event.key == pygame.K_LEFT:
                    self.camera_position = (
                        self.camera_position[0] - 1,
                        self.camera_position[1],
                    )
                elif event.key == pygame.K_DOWN:
                    self.camera_position = (
                        self.camera_position[0],
                        self.camera_position[1] + 1,
                    )
                elif event.key == pygame.K_UP:
                    self.camera_position = (
                        self.camera_position[0],
                        self.camera_position[1] - 1,
                    )
            return
