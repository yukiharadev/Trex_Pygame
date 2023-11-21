import pygame

class Animation:
    def __init__(self, filename, frame_size=(128, 128), num_frames=11, initial_position=(100, 310)):
        self.sprite_sheet = pygame.image.load(filename)
        self.frame_width, self.frame_height = frame_size
        max_frames = self.sprite_sheet.get_width() // self.frame_width
        self.frames = [self.sprite_sheet.subsurface((i * self.frame_width, 0, self.frame_width, self.frame_height)) for i in range(min(num_frames, max_frames))]
        self.frame_index = 0
        self.frame_rate = 10
        self.x, self.y = initial_position
        self.clock_tick_value = 30
        self.jump_strength = -17
        self.dy = 0

    def jump(self):
        if self.y == 310:
            self.dy = self.jump_strength

    def update(self):
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.dy += 1  # Add gravity
        self.y += self.dy

        if self.y > 310:
            self.y = 310
            self.dy = 0

    def draw(self, screen):
        scaled_frame = pygame.transform.scale(self.frames[self.frame_index], (self.frame_width, self.frame_height))
        screen.blit(scaled_frame, (self.x, self.y))

    def clock_tick(self):
        pygame.time.Clock().tick(self.clock_tick_value)  # Rename to avoid naming conflict
    def is_collision(self, other_sprite):

        self_rect = pygame.Rect(self.x, self.y, self.frame_width, self.frame_height)
        other_rect = pygame.Rect(other_sprite.x, other_sprite.y, other_sprite.frame_width * 2, other_sprite.frame_height * 2)
        return self_rect.colliderect(other_rect)
    def reset_position(self):
        self.x, self.y = (100, 310)
        self.dy = 0 

