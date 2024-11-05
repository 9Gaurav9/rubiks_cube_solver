# rubiks_cube_solver/ui.py
import pygame
import sys
from solver import CubeSolver

class CubeDisplay:
    def __init__(self, cube):
        pygame.init()
        self.screen = pygame.display.set_mode((500, 500))
        pygame.display.set_caption("Rubik's Cube Color Selector")

        self.cube = cube
        self.colors = {
            'white': (255, 255, 255),
            'yellow': (255, 255, 0),
            'green': (0, 255, 0),
            'blue': (0, 0, 255),
            'orange': (255, 165, 0),
            'red': (255, 0, 0)
        }
        self.selected_color = 'white'
        self.cell_size = 30
        self.start_button_rect = pygame.Rect(200, 400, 100, 40)

    def draw_palette(self):
        x, y = 50, 450
        for color_name, color_value in self.colors.items():
            pygame.draw.rect(self.screen, color_value, (x, y, self.cell_size, self.cell_size))
            x += self.cell_size + 10

    def select_color_from_palette(self, pos):
        x, y = 50, 450
        for color_name, color_value in self.colors.items():
            if pygame.Rect(x, y, self.cell_size, self.cell_size).collidepoint(pos):
                self.selected_color = color_name
            x += self.cell_size + 10

    def draw_cube_face(self, face, start_x, start_y):
        for i, row in enumerate(self.cube.faces[face]):
            for j, color in enumerate(row):
                rect = pygame.Rect(start_x + j * self.cell_size, start_y + i * self.cell_size, self.cell_size, self.cell_size)
                pygame.draw.rect(self.screen, self.colors[color], rect)
                pygame.draw.rect(self.screen, (0, 0, 0), rect, 1)

    def set_color_on_cube(self, face, pos, start_x, start_y):
        for i in range(3):
            for j in range(3):
                rect = pygame.Rect(start_x + j * self.cell_size, start_y + i * self.cell_size, self.cell_size, self.cell_size)
                if rect.collidepoint(pos):
                    self.cube.faces[face][i][j] = self.selected_color

    def draw_all_faces(self):
        face_positions = {
            'U': (200, 50),
            'F': (200, 140),
            'R': (290, 140),
            'L': (110, 140),
            'B': (380, 140),
            'D': (200, 230)
        }
        for face, (x, y) in face_positions.items():
            self.draw_cube_face(face, x, y)

    def draw_start_button(self):
        pygame.draw.rect(self.screen, (0, 255, 0), self.start_button_rect)
        font = pygame.font.Font(None, 36)
        text = font.render("Start", True, (255, 255, 255))
        self.screen.blit(text, (self.start_button_rect.x + 10, self.start_button_rect.y + 5))

    def run(self):
        running = True
        while running:
            self.screen.fill((192, 192, 192))
            self.draw_palette()
            self.draw_all_faces()
            self.draw_start_button()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if self.start_button_rect.collidepoint(event.pos):
                        self.show_3d_solution()
                    elif 450 <= event.pos[1] <= 450 + self.cell_size:
                        self.select_color_from_palette(event.pos)
                    else:
                        face_positions = {
                            'U': (200, 50),
                            'F': (200, 140),
                            'R': (290, 140),
                            'L': (110, 140),
                            'B': (380, 140),
                            'D': (200, 230)
                        }
                        for face, (x, y) in face_positions.items():
                            self.set_color_on_cube(face, event.pos, x, y)

            pygame.display.flip()

    def show_3d_solution(self):
        solver = CubeSolver(self.cube)
        solution = solver.solve()
        for move in solution:
            self.animate_move(move)

    def animate_move(self, move):
        self.apply_move(move)
        self.display_move(move)

    def apply_move(self, move):
        # Updates the internal cube state based on the move (e.g., R, U, F, etc.)
        face_map = {'R': self.cube.rotate_right, 'U': self.cube.rotate_up, 'F': self.cube.rotate_front}  # Define moves
        if move in face_map:
            face_map[move]()

    def display_move(self, move):
        # Pseudo 3D-like effect for move visualization
        frames = 10
        for frame in range(frames):
            self.screen.fill((192, 192, 192))
            self.draw_palette()
            self.draw_all_faces()

            # Display smooth transition of a move
            # E.g., if 'R', show the right column moving
            face = move[0]  # Example only; you’d add animation per face here
            # For 'R' move, visually slide rows to simulate right turn
            # Additional calculations would be done per face requirement

            pygame.display.flip()
            pygame.time.delay(50)  # Delay to create smooth animation

    def close(self):
        pygame.quit()
