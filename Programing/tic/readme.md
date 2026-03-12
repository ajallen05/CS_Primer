# Curses Tic-Tac-Toe

A classic Tic-Tac-Toe game implemented in the terminal using the `curses` library. It features an AI opponent that uses the Minimax algorithm, ensuring it always plays optimally.

## Features

- **AI Opponent**: Powered by the Minimax algorithm, making it impossible to beat.
- **Terminal UI**: Clean and interactive interface using the Python `curses` module.
- **Game Persistence**: Automatically saves game progress to `progress.json` and resumes upon restart.
- **Controls**:
    - Use Arrow Keys or WASD to move the cursor.
    - Press the key corresponding to your character (X or O) to place your move.
    - Press 'R' to restart after a game ends.

## Installation

Ensure you have the required dependencies installed:

```bash
pip install -r requirements.txt
```

*Note: On Windows, `windows-curses` is required as the standard `curses` module is not included by default.*

## Usage

Start the game by running:

```bash
python main.py
```

## File Structure

- `main.py`: The entry point of the game containing the core logic and UI loop.
- `minimax.py`: Implementation of the Minimax algorithm for the AI.
- `crazy.py`: An alternative or extended version of the game logic.
- `simple_curses.py`: A simpler implementation or demonstration of curses usage.
- `progress.json`: Stores the current game state for persistence.
- `requirements.txt`: List of Python dependencies.
