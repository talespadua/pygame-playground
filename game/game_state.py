from typing import Tuple

from game.levels.base_level import BaseLevel


class GameState:
    def __init__(self, level: BaseLevel):
        self.center = level.initial_position
        self.map = level.map_matrix

    def update_camera(self, camera_position: Tuple[int, int]) -> None:
        self.center = camera_position
