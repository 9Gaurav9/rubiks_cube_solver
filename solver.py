# rubiks_cube_solver/solver.py
from cube import RubiksCube


class CubeSolver:
    def __init__(self, cube: RubiksCube):
        self.cube = cube

    def solve(self):
        # Here, you would implement or call a solving algorithm like Kociemba's
        # Let's simulate by returning a mock solution sequence.
        return ["R", "U", "R'", "U'", "F", "U", "F'", "R", "U", "R'"]  # Placeholder steps

    def display_solution(self, moves):
        print("Solution steps:")
        print(" -> ".join(moves))
