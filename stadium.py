import arcade

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

from model import Stickman,World

class ModelSprite(arcade.Sprite):
    def __init__(self, *args, **kwargs):
        self.model = kwargs.pop('model', None)

        super().__init__(*args, **kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x, self.model.y)


    def draw(self):
        self.sync_with_model()
        super().draw()

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.WHITE)

        self.world = World(width,height);
        self.stickman_sprite = ModelSprite('images/snail.png',model=self.world.stickman)
        self.turtle_sprite = ModelSprite('images/turtle.png',model=self.world.turtle)


    def on_draw(self):
        arcade.start_render()
        self.stickman_sprite.draw()
        self.turtle_sprite.draw()

    def animate(self, delta):
        self.world.animate(delta)
       # self.stickman_sprite.set_position(self.world.stickman.x, self.world.stickman.y)

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)


if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()