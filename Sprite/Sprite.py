import pygame


# Constant possible direction of movement direction : angle
DIRECTIONS = {
    "UP": 0,
    "LEFT": 90,
    "DOWN": 180,
    "RIGHT": 270
}


class Sprite:
    def __init__(self, screen, width, height, position_x, position_y, image_link, speed=0.7):
        # Sprite's dimensions
        self.constWidth = width
        self.constHeight = height
        self.width = width
        self.height = height
        # Holds Sprite's position in dict
        self.position = {
            "x": position_x,
            "y": position_y
        }
        # Main game screen object
        self.screen = screen
        # Loads Sprite's image
        self.image = pygame.image.load(image_link)
        # Sprite speed values
        self.speed_x = 0
        self.speed_y = 0
        # Holds current angle of image to rotate when moving
        self.current_image_angle = 0
        # Status of sprite's life
        self.alive = True

        self.speed_and_direction = {
            "UP": -speed,
            "DOWN": speed,
            "RIGHT": speed,
            "LEFT": -speed
        }

    def draw(self):
        # Draws sprite on proper position everytime when pygame loop executes
        self.screen.blit(self.image, (self.position["x"], self.position["y"]))

    def update(self):
        # Updates Sprite's values on game screen everytime when pygame loop executes
        # Moves sprite on x axis
        self.position["x"] += self.speed_x
        # Moves sprint on Y axis
        self.position["y"] += self.speed_y

    def move(self, direction):
        # Changes speed according to the direction
        if direction == "UP" or direction == "DOWN":
            self.speed_y = self.speed_and_direction[direction]

            # Fix Y position caused rectangle sprite
            if direction == "DOWN" and self.current_image_angle == 90:
                self.position["x"] += 26
            elif direction == "UP" and self.current_image_angle == 90:
                self.position["x"] += 26
                self.position["y"] -= 26
            elif direction == "UP" and self.current_image_angle == 270:
                self.position["y"] -= 26

            # Swaps sprite dimensions
            if self.current_image_angle == 90 or self.current_image_angle == 270:
                self.width = self.constWidth
                self.height = self.constHeight

        elif direction == "RIGHT" or direction == "LEFT":
            # Swap dimensions (sprite is a rectangle)
            self.speed_x = self.speed_and_direction[direction]

            # Fix Y position caused rectangle sprite
            if direction == "LEFT" and self.current_image_angle == 180:
                self.position["x"] -= 26
            elif direction == "LEFT" and self.current_image_angle == 0:
                self.position["x"] -= 26
                self.position["y"] += 26

            if direction == "RIGHT" and self.current_image_angle == 0:
                self.position["y"] += 26

            # Swaps sprite dimensions
            if self.current_image_angle == 0 or self.current_image_angle == 180:
                self.width = self.constHeight
                self.height = self.constWidth

        # Rotates sprite
        self.rotate_sprite(direction)

    def rotate_sprite(self, destination_direction):
        # rotates image in appropriate direction
        if destination_direction == self.current_image_angle:
            self.current_image_angle = DIRECTIONS[destination_direction]
            return
        # Calculates angle difference
        rotate_angle = DIRECTIONS[destination_direction] - self.current_image_angle
        self.image = pygame.transform.rotate(self.image, rotate_angle)
        self.current_image_angle = DIRECTIONS[destination_direction]

    def stop(self):
        self.speed_x = self.speed_y = 0