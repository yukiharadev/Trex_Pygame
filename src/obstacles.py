import pygame

class SpriteAnimation:
    def __init__(self, filename, frame_size=(33, 33), num_frames=5):
        self.sprite_sheet = pygame.image.load(filename)
        self.frame_width, self.frame_height = frame_size
        max_frames = self.sprite_sheet.get_width() // self.frame_width
        self.frames = [self.sprite_sheet.subsurface((i * self.frame_width, 0, self.frame_width, self.frame_height)) for i in range(min(num_frames, max_frames))]
        self.frame_index = 0
        self.frame_rate = 10
        self.x, self.y = 1080, 380

    def update(self):
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.x -= 5 
        if self.x < -34:
            self.x = 1080

    def draw(self, screen):
        scaled_frame = pygame.transform.scale(self.frames[self.frame_index], (self.frame_width * 2, self.frame_height * 2))
        screen.blit(scaled_frame, (self.x, self.y))
    def reset_position(self):
        self.x = 1080