from typing import List, Optional

from pydantic import BaseModel


class LevelConfig(BaseModel):
    spritesheet: str
    level_matrix: List[List[int]]
    spritesheet_scaling: Optional[List[int]] = None
    # sprite_mapping: Dict[int, Enum]
