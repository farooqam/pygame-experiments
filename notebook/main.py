import pygame

pygame.init()

surface_height = 600
surface_width = 600
horizontal_line_color = pygame.Color(0, 0, 200)

surface = pygame.display.set_mode((surface_width, surface_height))
surface.fill((255, 255, 255))

current_y = 60
line_height = 20
num_lines = int((surface_height - current_y) / line_height)

# Draw horizontal lines.
for n in range(0, num_lines):
    for x in range(0, surface_width):
        surface.set_at((x, current_y), horizontal_line_color)
    current_y = current_y + line_height

vertical_line_color = (200, 0, 0)
vertical_line_offset = 25

# Draw vertical line.
for y in range(0, surface_height):
    surface.set_at((vertical_line_offset, y), vertical_line_color)

pygame.display.update()
input()
