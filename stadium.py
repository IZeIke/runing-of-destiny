import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600
STATUS = 0


class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        self.stickman = arcade.Sprite('images/run1.png')
        self.stickman.set_position(100, 250)

    def on_draw(self):
        arcade.start_render()
        self.stickman.draw()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.RIGHT :
            self.stickman.set_position(self.stickman.center_x + 1, self.stickman.center_y)





if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()