# minesweeperPy
minesweeperPy is a Python implementation of the classic Minesweeper game. This project provides a basic Minesweeper game interface with customizable field dimensions and mine density.

## Features
Customizable board dimensions.
Dynamic generation of the game field.
Interactive gameplay.
Reveals empty spaces automatically when an empty cell is clicked.
Ability to solve Minesweeper boards.
## Installation
To run the Minesweeper game, follow these steps:

1. Clone the repository:
```bash
git clone https://github.com/your-username/minesweeperPy.git
```
2. Navigate to the project directory:
```bash
cd minesweeperPy
```
3. Run the game:

```bash
python minesweeper.py
```
## Usage
Upon running the game, you will be prompted to provide the x and y coordinates of the cell you want to uncover.
Enter the coordinates as prompted and press Enter.
The game will display the updated game field, revealing the content of the selected cell and adjacent cells accordingly.
The chata.py file provides functions to print and solve Minesweeper boards.
The fieldCreation.py file contains the board class, which is responsible for creating the game field with customizable dimensions and mine density.

## Code Structure
The code consists of the following components:

minesweeper.py: Main script to run the Minesweeper game. It utilizes the gamingField class to manage the game field and interactions.
fieldCreation.py: Contains functions to create the game field with customizable dimensions and mine density.
chata.py: Provides functions to print and solve Minesweeper boards.
gamingField class: Defines the game field and provides methods to check cells, uncover them, and display the game state.

## Example
Below is an example of how the game is played:

```bash
Give x and y:
 x =  5
 y =  7
```
After entering the coordinates, the game board will be updated to reveal the content of the selected cell and adjacent cells.

## Gameplay Instructions
The game board consists of hidden cells, some of which contain mines.
Your objective is to uncover all cells without detonating any mines.
Cells without mines will display a number indicating the count of adjacent cells containing mines.
If you uncover a mine, the game ends immediately.
## Additional Files
fieldCreation.py: Contains the board class, which is responsible for creating the game field with customizable dimensions and mine density.
chata.py: Provides functions to print and solve Minesweeper boards.

## License
This project is licensed under the MIT License.
