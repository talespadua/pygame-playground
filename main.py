from game.game import Game
from game.settings import Settings


if __name__ == "__main__":
    settings = Settings(
        screen_width=1024,
        screen_height=768,
        frames_per_second=60,
        window_caption="Wanna-be-a-game",
    )
    game = Game(settings)
    game.run()
