from game.levels.base_level import BaseLevel
from game.levels.level_config import LevelConfig


class LevelFactory:
    @staticmethod
    def create(level_number: int) -> BaseLevel:
        if level_number == 1:
            return BaseLevel(
                LevelConfig(
                    spritesheet="resources/IsoTacticsTileset.png",
                    spritesheet_scaling=[768, 768],
                    level_matrix=[
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                        [0, 0, 0, 0, 0],
                    ],
                )
            )
        raise NotImplementedError
