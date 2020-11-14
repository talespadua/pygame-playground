from pydantic import BaseModel


class Settings(BaseModel):
    screen_width: int
    screen_height: int
    window_caption: str
    frames_per_second: int
