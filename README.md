# Chess Game in Python
By Knightly Coders

## Developer
- **Name:** Shokhjakhon Akhmedov
- **Matriculation Number:** 99491698
- **Contribution:** 100% of code implementation

## Features

- Complete chess piece movement rules
- Turn-based gameplay (White vs Black)
- Piece capture mechanics
- Game state tracking
- Visual move suggestions
- Check detection
- Resignation option
- Game over screen with restart capability
- Captured pieces display

## Game Components

### Pieces
- All standard chess pieces implemented (Pawn, Rook, Knight, Bishop, Queen, King)
- Each piece has its own movement logic and validation
- Visual representation using PNG images

### Board
- 8x8 chess board with alternating colors
- Piece position tracking
- Move validation
- Game state management

### UI Features
- Move highlighting
- Valid move indicators
- Turn status display
- Game over screen
- Restart functionality
- Resignation button

## How to Play

1. White moves first
2. Click on a piece to select it
3. Valid moves will be shown as dots
4. Click on a valid position to move
5. Captured pieces are displayed on the side
6. Use the RESIGN button to forfeit
7. After game over, use RESTART for a new game

## Requirements

- Python 3.13.1
- Pygame library
- Chess piece images in 'images' folder
- bahnschrift.ttf font file

## Installation

1. Install Python 3.13.1
2. Install Pygame:
```bash
pip install pygame
3. Place chess piece images in 'images' folder
4. Run the game:
python chess.py

## File structure
- chess.py - Main game file
- bahnschrift.ttf - Font file for text rendering
- images/ - Directory containing chess piece images
