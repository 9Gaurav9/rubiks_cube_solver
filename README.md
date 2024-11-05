
# Rubik's Cube Solver

## Overview

This project is a visual Rubik's Cube solver that allows users to manually input colors for each face of a 3x3 Rubik's Cube using a graphical user interface (GUI). The application utilizes an algorithm to solve the cube and visually demonstrates the solution through a series of animated moves.

## Features

- **Color Selection**: Choose colors for each face of the cube using a simple UI.
- **Animated Solution**: Watch the cube solve itself with smooth animations that represent each move in 3D.
- **Customizable Colors**: Modify the color palette to suit personal preferences.
- **User-Friendly Interface**: Intuitive layout for setting colors and starting the solution.

## Technologies Used

- Python
- Pygame
- Basic algorithms for Rubik's Cube solving

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/9Gaurav9/rubiks_cube_solver.git
   cd rubiks_cube_solver
   ```

2. **Install Dependencies**:
   Make sure you have Python installed. You can install the required packages using pip:
   ```bash
   pip install pygame
   ```

## Usage

1. Run the application:
   ```bash
   python main.py
   ```

2. **Select Colors**:
   - Click on the colored squares at the bottom of the screen to select a color.
   - Click on the corresponding squares of the cube to set the selected color for each face.

3. **Start Solving**:
   - Once all colors are set, click the "Start" button to see the solution in action.
   - The cube will animate its moves until it reaches the solved state.

## Implementation Details

### File Structure

```
rubiks_cube_solver/
│
├── main.py              # Entry point of the application
├── rubiks_cube.py       # Contains the Rubik's Cube class and rotation logic
├── solver.py            # Implements the CubeSolver class for solving logic
└── ui.py                # Handles the graphical user interface and interactions
```

### Cube Logic

The `RubiksCube` class manages the state of the cube and provides methods for rotating the faces. The `CubeSolver` class implements an algorithm to determine the sequence of moves needed to solve the cube.

### UI

The UI is built using Pygame and allows for color selection and cube manipulation. It visually represents the cube and animates the solving process.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Thanks to the open-source community for the libraries and resources used in this project.
- Special thanks to the authors of various Rubik's Cube algorithms for their contributions to the field.

