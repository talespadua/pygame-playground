from game.game import Game
from game.settings import Settings


if __name__ == "__main__":
    settings = Settings(
        screen_width=800,
        screen_height=600,
        frames_per_second=15,
        window_caption="PlaceHolder Caption",
    )
    game = Game(settings)
    game.run()
