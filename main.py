# rubiks_cube_solver/main.py
import pygame
from cube import RubiksCube
from ui import CubeDisplay
from solver import CubeSolver


def main():
    # Initialize the cube with default colors
    cube = RubiksCube()

    # Launch the color selection UI
    print("Use the UI to select and set colors for each face of the cube.")
    display = CubeDisplay(cube)
    display.run()  # Run the UI until the user closes it

    # Display the final state of the cube (for debugging or verification)
    cube.display_cube()

    # Solve the cube
    solver = CubeSolver(cube)
    solution = solver.solve()
    solver.display_solution(solution)

    # Display solution visually
    for move in solution:
        display.draw_cube()
        pygame.time.wait(500)  # Adjust wait time to see each move visually

    display.close()


if __name__ == "__main__":
    main()
