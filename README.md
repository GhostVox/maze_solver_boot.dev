# Mazetrix

A Python-based maze generator and solver with a graphical interface built using Tkinter. This project was created as part of the [Boot.dev](https://www.boot.dev) curriculum and demonstrates algorithm implementation, object-oriented programming, and GUI development concepts.

## Features

- **Automatic Maze Generation** - Creates random mazes using recursive backtracking algorithm
- **Visual Maze Solving** - Watches the algorithm solve the maze step-by-step in real-time
- **Interactive GUI** - Built with Tkinter for cross-platform compatibility
- **Animated Visualization** - See walls break during generation and path-finding during solving
- **Configurable Parameters** - Easily adjust maze size, cell dimensions, and margins
- **Depth-First Search** - Uses recursive backtracking for both generation and solving
- **Comprehensive Testing** - Unit tests ensure algorithm correctness

## How It Works

### Maze Generation

1. **Initialize Grid** - Creates a grid of cells, each with four walls
2. **Break Entrance/Exit** - Removes top wall of start cell and bottom wall of end cell
3. **Recursive Backtracking** - Randomly breaks walls between unvisited neighboring cells
4. **Visual Animation** - Shows walls disappearing as the maze is carved out

### Maze Solving

1. **Depth-First Search** - Explores paths recursively from start to finish
2. **Path Visualization** - Red lines show current exploration path
3. **Backtracking Visual** - Gray lines show when algorithm backtracks from dead ends
4. **Solution Highlighting** - Final solution path remains highlighted in red

## Visual Demo

When you run the program, you'll see:

- **Generation Phase**: Walls disappearing as the maze is carved
- **Solving Phase**: Red lines showing the algorithm's exploration
- **Backtracking**: Gray lines when the algorithm hits dead ends
- **Solution**: Final path from entrance (top-left) to exit (bottom-right)

## Prerequisites & Installation

### Required Software

- **Python 3.12+** - Download from [python.org](https://python.org)
- **Poetry** (recommended) or **pip** for dependency management

### Installation Options

#### Option 1: Using Poetry (Recommended)

```bash
# Clone the repository
git clone [your-repo-url]
cd maze_solver_boot.dev

# Install dependencies with Poetry
poetry install

# Activate virtual environment
poetry shell

# Run the maze solver
python main.py
```

#### Option 2: Using pip and virtual environment

```bash
# Clone the repository
git clone [your-repo-url]
cd maze_solver_boot.dev

# Create virtual environment
python -m venv env

# Activate virtual environment
# On Windows:
env\Scripts\activate
# On macOS/Linux:
source env/bin/activate

# Install dependencies
pip install black ruff

# Run the maze solver
python main.py
```

#### Option 3: Direct execution (basic)

```bash
# Clone the repository
git clone [your-repo-url]
cd maze_solver_boot.dev

# Run directly (uses only built-in libraries)
python main.py
```

## Configuration

Modify maze parameters in `main.py`:

```python
def main():
    num_rows = 12        # Number of rows in the maze
    num_cols = 16        # Number of columns in the maze
    margin = 50          # Border margin in pixels
    screen_x = 800       # Window width
    screen_y = 600       # Window height

    # Cell sizes are calculated automatically
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
```

### Customization Options

- **Maze Size**: Adjust `num_rows` and `num_cols` for different maze dimensions
- **Window Size**: Modify `screen_x` and `screen_y` for larger/smaller display
- **Animation Speed**: Change `time.sleep(0.05)` in `maze.py` for faster/slower animation
- **Colors**: Modify colors in `cell.py` (walls: "black", background: "white", path: "red", backtrack: "grey")

## Project Structure

```
maze_solver_boot.dev/
├── main.py              # Application entry point and configuration
├── maze.py              # Maze class with generation and solving algorithms
├── cell.py              # Cell class representing individual maze cells
├── graphics.py          # Graphics utilities (Window, Point, Line classes)
├── test_maze.py         # Unit tests for maze functionality
├── pyproject.toml       # Poetry configuration and dependencies
├── poetry.lock          # Locked dependency versions
├── .gitignore           # Git ignore rules
├── .vscode/             # VS Code configuration
│   └── settings.json    # Editor settings (Black formatter)
└── README.md            # This file
```

## Algorithm Details

### Maze Generation (Recursive Backtracking)

1. Start with a grid where every cell has all four walls
2. Choose a random starting cell and mark it as visited
3. Look for unvisited neighboring cells
4. If unvisited neighbors exist:
   - Choose one randomly
   - Remove the wall between current and chosen cell
   - Recursively call the algorithm on the chosen cell
5. If no unvisited neighbors exist, backtrack to previous cell
6. Continue until all cells have been visited

### Maze Solving (Depth-First Search)

1. Start at the entrance (top-left corner)
2. Mark current cell as visited
3. For each direction (left, right, up, down):
   - If there's no wall blocking the path
   - And the neighboring cell hasn't been visited
   - Move to that cell and continue recursively
4. If the current cell is the exit, return success
5. If no valid moves exist, backtrack and try a different path
6. Visual feedback shows exploration (red) and backtracking (gray)

## Testing

Run the comprehensive test suite:

```bash
# Using Poetry
poetry run python -m pytest test_maze.py -v

# Using standard Python
python -m unittest test_maze.py -v

# Or run directly
python test_maze.py
```

### Test Coverage

- **Maze Creation**: Verifies correct grid dimensions and initialization
- **Entrance/Exit**: Ensures proper entrance and exit wall removal
- **Cell Management**: Tests cell coordinate and center point calculations
- **Reset Functionality**: Confirms visited flags are properly reset

## Development

### Code Formatting

The project uses Black for code formatting:

```bash
# Format all Python files
poetry run black .

# Or with pip
black .
```

### Linting

Uses Ruff for fast Python linting:

```bash
# Run linter
poetry run ruff check .

# Or with pip
ruff check .
```

### VS Code Integration

The project includes VS Code settings for:

- **Automatic formatting** on save using Black
- **Python path configuration** for proper imports
- **Consistent code style** across development environments

## Algorithm Complexity

### Time Complexity

- **Generation**: O(n) where n is the number of cells
- **Solving**: O(n) in worst case (visiting every cell)

### Space Complexity

- **Memory**: O(n) for storing the maze grid
- **Recursion Stack**: O(n) in worst case for deep recursion

## Learning Objectives

This project demonstrates key programming concepts:

- **Recursive Algorithms** - Backtracking for both generation and solving
- **Object-Oriented Design** - Clean separation of concerns with Cell, Maze, and Graphics classes
- **GUI Programming** - Tkinter for cross-platform graphical interfaces
- **Algorithm Visualization** - Real-time animation of algorithm execution
- **Event-Driven Programming** - GUI event handling and window management
- **Unit Testing** - Comprehensive test coverage for algorithm correctness
- **Code Organization** - Modular design with clear responsibilities
- **Package Management** - Poetry for modern Python dependency management

## Troubleshooting

### Common Issues

**"No module named 'tkinter'"**

- Tkinter comes with Python by default
- On some Linux distributions: `sudo apt-get install python3-tk`
- On macOS with Homebrew: `brew install python-tk`

**Window doesn't appear**

- Ensure you're running in a graphical environment
- Try running from terminal rather than IDE
- Check if other GUI applications work on your system

**Animation too fast/slow**

- Modify `time.sleep(0.05)` in `maze.py` `_animate_self()` method
- Increase the value to slow down, decrease to speed up

**Maze generation stuck**

- This is normal for very large mazes
- The algorithm will complete, but may take time for grids larger than 50x50

**Memory issues with large mazes**

- Reduce `num_rows` and `num_cols` in `main.py`
- The algorithm creates recursion depth proportional to maze size

## Future Enhancements

Potential improvements you could add:

- **Multiple solving algorithms** (A\*, Dijkstra's, BFS)
- **Different generation algorithms** (Prim's, Kruskal's)
- **Save/load maze functionality**
- **Custom maze import from files**
- **Performance metrics** (generation time, solution length)
- **Different visualization styles**
- **Interactive maze editing**
- **Multiple entrance/exit points**

Perfect for Python developers interested in algorithm visualization, GUI programming, and understanding classic computer science algorithms in action!
