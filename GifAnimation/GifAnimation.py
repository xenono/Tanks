import pygame


class GifAnimation:
    def __init__(self, folder_with_frames, first_frame_number, last_frame_number, position_x, position_y, screen):
        self.screen = screen
        self.folder_with_frames = folder_with_frames
        self.first_frame_number = first_frame_number
        self.last_frame_number = last_frame_number
        self.frames = []
        self.frame_counter = 0
        self.is_finished = False
        self.frame_delay = 0
        self.position = (position_x, position_y)

    def load_frames(self):
        # Load all frames
        step = 1 if self.first_frame_number < self.last_frame_number else -1
        for frame in range(self.first_frame_number, self.last_frame_number + step, step):
            path = "assets/{}/0{:02d}.png".format(self.folder_with_frames, frame)
            self.frames.append(pygame.image.load(path))

    def play(self):
        self.screen.blit(self.frames[self.frame_counter], self.position)
        self.frame_delay += 1

    def update(self):
        # Check if all frames were played
        if self.frame_counter == len(self.frames):
            self.is_finished = True

        # Each frame is played 20 times then it switches to another
        if not self.is_finished:
            self.play()
            if self.frame_delay % 20 == 0:
                self.frame_counter += 1


