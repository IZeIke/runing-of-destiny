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
        self.state_win =-1;
        self.change_mode = 0
        self.key_state = 0

    def horizontal_key(self,key):
        if key == arcade.key.RIGHT and self.status_snail == 0:
            self.stickman.x += 5
            self.status_snail=1;
        elif key == arcade.key.LEFT and self.status_snail == 1:
            self.stickman.x += 5
            self.status_snail=0;
        elif key == arcade.key.D and self.status_turtle == 0:
            self.turtle.x += 5
            self.status_turtle=1;
        elif key == arcade.key.A and self.status_turtle == 1:
            self.turtle.x += 5
            self.status_turtle=0;

    def vertical_key(self,key):
        if key == arcade.key.UP and self.status_snail == 0:
            self.stickman.x += 5
            self.status_snail=1;
        elif key == arcade.key.DOWN and self.status_snail == 1:
            self.stickman.x += 5
            self.status_snail=0;
        elif key == arcade.key.W and self.status_turtle == 0:
            self.turtle.x += 5
            self.status_turtle=1;
        elif key == arcade.key.S and self.status_turtle == 1:
            self.turtle.x += 5
            self.status_turtle=0;

    def on_key_press(self, key, key_modifiers):
        self.change_mode+=1

        if self.change_mode == 100:
            self.key_state = 1
        if self.change_mode == 200:
            self.key_state = 0
            self.change_mode =0

        if self.key_state == 0:
            self.horizontal_key(key)
        if self.key_state == 1:
            self.vertical_key(key)


    def win_state(self):
        if self.stickman.x>1200 and self.turtle.x<1200:
            self.state_win=0;
        elif self.turtle.x>1200 and self.stickman.x<1200:
            self.state_win=1;


    def animate(self, delta):
        self.stickman.animate(delta)
        self.turtle.animate(delta)





