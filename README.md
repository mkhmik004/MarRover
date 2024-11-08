# Rover Simulator 🚀

A Python-based rover simulator that processes movement and turning instructions from a text file and calculates the rover's position and orientation. The rover can display its actions in text format or provide a graphical visualization with customizable colors using Python's `turtle` library.

## Features

- Parses commands from a `.txt` file to control the rover's movements and rotations.
- Supports graphical visualization of the rover's path with optional color selection.
- Uses trigonometry to accurately update the rover's position and orientation.

## Requirements

- **Python 3**
- **turtle** (comes pre-installed with Python)

## Usage

### 1. Command-Line Arguments

- **`file`**: Path to the text file containing movement instructions.
- **`--graphical`**: (Optional) Enables graphical visualization of the rover. Choose a color for the rover’s path. Defaults to **black**.

### 2. Input File Format

Each line in the file should contain one instruction in the following format:

- **Turn Instructions**: `turn <angle> degrees [clockwise|counterclockwise]`
- **Move Instructions**: `Move <distance> meters [backward|forward]`

Degrees should be between 0 and 360, and meters should be positive.

**Example**:
```txt
Move 10 meters forward
Turn 45 degrees clockwise
Move 5 meters forward
Turn 30 degrees counterclockwise
Move 10 meters forward

