import arcade
from random import randint
import arcade.key

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
        arcade.set_background_color(arcade.color.SAND)
        self.world = World(width,height)
        self.stickman_sprite = ModelSprite('images/snail.png',model=self.world.stickman)
        self.turtle_sprite = ModelSprite('images/turtle.png',model=self.world.turtle)
        self.sand = arcade.Sprite('images/sand.jpg');
        self.starfish_list = arcade.SpriteList()
        filename = "images/starfish.png"
        for i in range(10):
            starfish = arcade.Sprite(filename)
            starfish.center_x = randint(0, SCREEN_WIDTH - 1)
            starfish.center_y = randint(0, SCREEN_HEIGHT - 1)
            self.starfish_list.append(starfish)



    def on_draw(self):
        arcade.start_render()
        self.sand.draw()
        self.starfish_list.draw(fast=True)
        self.stickman_sprite.draw()
        self.turtle_sprite.draw()
        if self.world.state_win == 0:
            arcade.draw_text("Snail Win!!!",600, 300,arcade.color.RED_DEVIL, 40)

        if self.world.state_win == 1:
            arcade.draw_text("Turtle Win!!!",600, 300,arcade.color.RED_DEVIL, 40)


    def animate(self, delta):
        self.world.animate(delta)
        self.world.win_state()

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)


if __name__ == '__main__':
    window = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()