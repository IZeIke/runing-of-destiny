import arcade.key


class Stickman:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def animate(self, delta):
        self.x += 0

class Turtle:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def animate(self, delta):
        self.x += 0

class World:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.stickman = Stickman(150, 150)
        self.turtle = Turtle(150,450)
        self.status_snail = 0
        self.status_turtle = 0

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.RIGHT and self.status_snail == 0:
            self.stickman.x += 5
            self.status=1;
        elif key == arcade.key.LEFT and self.status_snail == 1:
            self.stickman.x += 5
            self.status=0;
        elif key == arcade.key.D and self.status_turtle == 0:
            self.turtle.x += 5
            self.status=1;
        elif key == arcade.key.A and self.status_turtle == 1:
            self.turtle.x += 5
            self.status=0;


    def animate(self, delta):
        self.stickman.animate(delta)
        self.turtle.animate(delta)





