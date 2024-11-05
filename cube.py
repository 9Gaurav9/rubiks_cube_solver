# rubiks_cube_solver/rubiks_cube.py
class RubiksCube:
    def __init__(self):
        # Initialize the cube with six faces
        self.faces = {
            'U': [['white'] * 3 for _ in range(3)],
            'D': [['yellow'] * 3 for _ in range(3)],
            'F': [['green'] * 3 for _ in range(3)],
            'B': [['blue'] * 3 for _ in range(3)],
            'L': [['orange'] * 3 for _ in range(3)],
            'R': [['red'] * 3 for _ in range(3)],
        }

    def rotate_right(self):
        # Rotate the right face clockwise and adjust adjacent faces
        self.faces['R'] = self._rotate_face_clockwise(self.faces['R'])
        self._rotate_adjacent_faces_right()

    def rotate_up(self):
        # Rotate the upper face clockwise and adjust adjacent faces
        self.faces['U'] = self._rotate_face_clockwise(self.faces['U'])
        self._rotate_adjacent_faces_up()

    def rotate_front(self):
        # Rotate the front face clockwise and adjust adjacent faces
        self.faces['F'] = self._rotate_face_clockwise(self.faces['F'])
        self._rotate_adjacent_faces_front()

    def _rotate_face_clockwise(self, face):
        return [list(row) for row in zip(*face[::-1])]

    def _rotate_adjacent_faces_right(self):
        # Adjust the adjacent faces for a right face rotation
        temp = self.faces['U'][0][2], self.faces['F'][0][2], self.faces['D'][0][2], self.faces['B'][2][0]
        self.faces['U'][0][2], self.faces['F'][0][2], self.faces['D'][0][2], self.faces['B'][2][0] = \
            self.faces['F'][0][2], self.faces['D'][0][2], self.faces['B'][2][0], self.faces['U'][0][2]

    def _rotate_adjacent_faces_up(self):
        # Adjust the adjacent faces for an upper face rotation
        temp = self.faces['F'][0], self.faces['R'][0], self.faces['B'][0], self.faces['L'][0]
        self.faces['F'][0], self.faces['R'][0], self.faces['B'][0], self.faces['L'][0] = \
            self.faces['L'][0], self.faces['F'][0], self.faces['R'][0], self.faces['B'][0]

    def _rotate_adjacent_faces_front(self):
        # Adjust the adjacent faces for a front face rotation
        temp = self.faces['U'][2], self.faces['R'][:, 0], self.faces['D'][0], self.faces['L'][:, 2]
        self.faces['U'][2], self.faces['R'][:, 0], self.faces['D'][0], self.faces['L'][:, 2] = \
            self.faces['L'][:, 2], self.faces['U'][2], self.faces['R'][:, 0], self.faces['D'][0]
