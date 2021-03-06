import pygame
from Sprite.Sprite import Sprite
from GifAnimation.GifAnimation import GifAnimation
from settings import Settings

# Constant possible direction of movement direction : angle
DIRECTIONS = {
    "UP": 0,
    "LEFT": 90,
    "DOWN": 180,
    "RIGHT": 270
}

settings = Settings()


class TankBullet(Sprite):
    def __init__(self, position_x, position_y, screen, tank_angle, shooter):
        super().__init__(screen, settings.bulletWidth, settings.bulletHeight, position_x, position_y, "assets/missile.png", settings.bulletSpeed)
        self.__window_width, self.__window_height = pygame.display.get_surface().get_size()
        self.shooter = shooter
        for direction, angle in DIRECTIONS.items():
            if angle == tank_angle:
                self.direction = direction

        self.move(self.direction)
        self.exploded = False

    def update(self):
        super().update()
        self.check_for_border_hit()

    def check_for_border_hit(self):
        if self.position["x"] <= 5 or self.position["x"] + self.width >= self.__window_width - 5.5:
            self.alive = False
        if self.position["y"] <= 5 or self.position["y"] + self.height >= self.__window_height - 5.5:
            self.alive = False

    def explode(self, frames, animation_objects):
        if not self.alive:
            new_gif = GifAnimation(frames, self.position["x"] - 25, self.position["y"] - 40, self.screen, 10)
            animation_objects.append(new_gif)

    def check_for_hit(self, object_width, object_height, object_position):
        object_x, object_y = object_position["x"], object_position["y"]
        if (object_x + object_width) >= self.position["x"] >= object_x:
            if object_y <= self.position["y"] <= (object_y + object_height):
                return True
        return False
