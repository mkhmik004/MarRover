Rover Simulator 🚀
A Python-based rover simulator that processes movement and turning instructions from a text file and calculates the rover's position and orientation. The rover can display its actions in text format or provide a graphical visualization with customizable colors using Python's turtle library.

Features
Parses commands from a .txt file to control the rover's movements and rotations.
Supports graphical visualization of the rover's path with optional color selection.
Uses trigonometry to accurately update the rover's position and orientation.
Requirements
Python 3
turtle (comes pre-installed with Python)
Usage
1. Command-Line Arguments
file: Path to the text file containing movement instructions.
--graphical: (Optional) Enables graphical visualization of the rover. Choose a color for the rover’s path. Defaults to black.
2. Input File Format
Each line in the file should contain one instruction in the following format:

Turn Instructions: turn [degrees] [clockwise|counterclockwise]
Move Instructions: move [meters] [forward|backward]
Degrees should be between 0 and 360, and meters should be positive.

Example:

txt
Copy code
move 5 forward
turn 90 clockwise
move 10 backward
turn 45 counterclockwise
3. Running the Script
Run the script from the command line with the necessary arguments:

bash
Copy code
python rover_simulator.py path/to/instructions.txt --graphical red
Example Commands
Text Output Only:

bash
Copy code
python rover_simulator.py instructions.txt
Graphical Visualization:

bash
Copy code
python rover_simulator.py instructions.txt --graphical blue
Explanation of Functionality
Parsing Instructions: The script reads instructions from a .txt file and parses them into movement and turn actions.

Executing Movements:

For each instruction, it calculates the new position based on trigonometric functions (sine and cosine) for forward and backward movements relative to the current orientation.
Graphical Mode:

If --graphical is enabled, turtle graphics will draw the rover’s path on a canvas, changing orientation and position based on the parsed instructions.
Error Handling
If an invalid instruction is found, the script exits and displays the line number of the problematic instruction.
