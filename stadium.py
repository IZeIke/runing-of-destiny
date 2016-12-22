import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

from model import Stickman



class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        self.stickman = Stickman(100,250)
        self.stickman_sprite = arcade.Sprite('images/run1.png')


    def on_draw(self):
        arcade.start_render()
        self.stickman_sprite.draw()

    def animate(self, delta):
        stickman = self.stickman
        stickman.animate(delta)
        self.stickman_sprite.set_position(stickman.x,stickman.y)


if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()