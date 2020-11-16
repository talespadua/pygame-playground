from pygame import Rect, Vector2
from pygame.surface import Surface

from game.game_state import GameState
from game.math.isometric_calculator import to_isometric_position, isometric_offset


class MapRenderer:
    def __init__(
        self,
        game_state: GameState,
        display: Surface,
        map_sprite: Surface,
    ):
        self.map_sprite = map_sprite
        self.display = display
        self.cell_size = Vector2(768 / 8, 768 / 16)

    def isometric_offset(self, map_center: Vector2, screen_size: Vector2) -> Vector2:
        isometric_center = to_isometric_position(map_center, self.cell_size)
        offset = isometric_offset(isometric_center, screen_size, self.cell_size)
        return offset

    def render(self, game_state: GameState) -> None:
        offset = self.isometric_offset(
            Vector2(game_state.center[0], game_state.center[1]), Vector2(1024, 768)
        )
        for i in range(len(game_state.map)):
            for j in range(len(game_state.map)):
                isometric_position = to_isometric_position(
                    Vector2(j, i), self.cell_size
                )

                tile_screen_location = [
                    isometric_position.x + offset.x,
                    isometric_position.y + offset.y,
                ]

                spritesheet_rectangle = Rect(
                    game_state.map[0][0],
                    game_state.map[0][0],
                    self.cell_size.x,
                    self.cell_size.y * 2,
                )
                self.display.blit(
                    self.map_sprite, tile_screen_location, spritesheet_rectangle
                )
