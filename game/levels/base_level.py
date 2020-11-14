from game.levels.level_config import LevelConfig
from pygame import image, transform


class BaseLevel:
    def __init__(self, level_config: LevelConfig) -> None:
        if level_config.spritesheet_scaling:
            sprite = image.load(level_config.spritesheet)
            self.sprite = transform.smoothscale(
                sprite, level_config.spritesheet_scaling
            )
        else:
            self.sprite = image.load(level_config.spritesheet)

        self.matrix = level_config.level_matrix
