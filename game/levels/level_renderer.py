from pygame import transform, Rect, image, Vector2
from pygame.surface import Surface
from game.levels.base_level import BaseLevel


class LevelRenderer:
    def __init__(self, cell_size: Vector2, display: Surface):
        self.cell_size = cell_size
        self.display = display
        self.x_offset = 32 * 12
        self.y_offset = 32 * 6

    def render(self, level: BaseLevel) -> None:

        for i in range(len(level.matrix)):
            for j in range(len(level.matrix)):
                isometric_x = self.to_isometric_position_x(j, i)
                isometric_y = self.to_isometric_position_y(j, i)

                tile_screen_location = [
                    isometric_x + self.x_offset,
                    isometric_y + self.y_offset,
                ]

                spritesheet_rectangle = Rect(
                    level.matrix[0][0],
                    level.matrix[0][0],
                    self.cell_size.x,
                    self.cell_size.y * 2,
                )
                self.display.blit(
                    level.sprite, tile_screen_location, spritesheet_rectangle
                )

    # based on http://clintbellanger.net/articles/isometric_math/
    def to_isometric_position_x(
        self, orthographic_x: float, orthographic_y: float
    ) -> float:
        return (orthographic_x - orthographic_y) * (self.cell_size.x / 2)

    def to_isometric_position_y(
        self, orthographic_x: float, orthographic_y: float
    ) -> float:
        return (orthographic_x + orthographic_y) * (self.cell_size.y / 2)
