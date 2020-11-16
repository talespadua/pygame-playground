from typing import List, Optional, Tuple

from pydantic import BaseModel


class LevelConfig(BaseModel):
    spritesheet: str
    map_matrix: List[List[int]]
    spritesheet_scaling: Optional[List[int]] = None
    initial_position: Tuple[int, int]
    # sprite_mapping: Dict[int, Enum]
