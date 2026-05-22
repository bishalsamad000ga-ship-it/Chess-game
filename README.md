# ♟️ Chess Game

A complete, playable chess game implementation in Python with all standard chess rules and 2D Unicode character pieces.

## 🎮 Features

- ✅ **Full Chess Rules**: All pieces move according to standard chess rules
  - Pawn: Forward movement with captures, promotion at end rank
  - Knight: L-shaped movements
  - Bishop: Diagonal movements
  - Rook: Horizontal and vertical movements
  - Queen: Combined rook and bishop movements
  - King: One square in any direction

- ✅ **Game Detection**:
  - Check detection
  - Checkmate detection
  - Stalemate detection
  - Move validation (can't move into check)

- ✅ **Beautiful UI**:
  - Unicode chess pieces (♔ ♕ ♖ ♗ ♘ ♙ ♚ ♛ ♜ ♝ ♞ ♟)
  - Clear board display with coordinates
  - Move history tracking

- ✅ **Player-Friendly**:
  - Standard chess notation input (e.g., "e2 e4")
  - Move validation with clear error messages
  - Game history review

## 📋 Project Structure

```
Chess-game/
├── pieces.py          # Piece definitions and movement logic
├── board.py           # Board state and move validation
├── chess_game.py      # Main game logic and UI
└── README.md          # This file
```

## 🚀 How to Play

### Installation
No external dependencies required! Just Python 3.6+

### Running the Game
```bash
python3 chess_game.py
```

### Game Controls
```
e2 e4    - Move piece from e2 to e4 (standard chess notation)
history  - Show move history
reset    - Start a new game
quit     - Exit the game
```

## ♟️ Chess Notation Guide

The board uses standard algebraic notation:
- Columns: **a-h** (left to right)
- Rows: **1-8** (bottom to top)
- Examples:
  - `e2 e4` - Move pawn from e2 to e4 (King's Pawn Opening)
  - `e7 e5` - Move pawn from e7 to e5 (Open Game)
  - `g1 f3` - Move knight from g1 to f3 (Nf3)

## 📊 Initial Board Setup

```
  0 1 2 3 4 5 6 7
  ───────────────
0│ ♜ ♞ ♝ ♛ ♚ ♝ ♞ ♜ │
1│ ♟ ♟ ♟ ♟ ♟ ♟ ♟ ♟ │
2│ · · · · · · · · │
3│ · · · · · · · · │
4│ · · · · · · · · │
5│ · · · · · · · · │
6│ ♙ ♙ ♙ ♙ ♙ ♙ ♙ ♙ │
7│ ♖ ♘ ♗ ♕ ♔ ♗ ♘ ♖ │
  ───────────────
```

## 🎯 Features Explained

### Move Validation
- Each piece can only move according to its rules
- You cannot move through other pieces (except knights)
- You cannot capture your own pieces
- You cannot move into check

### Check & Checkmate
- When your king is under attack, you're in **check**
- If you're in check and have no legal moves, it's **checkmate**
- Checkmate ends the game - the other player wins!

### Stalemate
- If you have no legal moves but are NOT in check
- The game is a draw

### Pawn Promotion
- When a pawn reaches the opposite end of the board
- It automatically promotes to a Queen

## 📝 Example Game

```
♟️ White: e2 e4
♟️ Black: e7 e5
♟️ White: g1 f3
♟️ Black: b8 c6
...
```

## 🔧 Technical Details

### Class Structure

**Piece** (Base Class)
- All pieces inherit from this base class
- Contains Unicode representation
- `get_possible_moves()` method for each piece type

**Board**
- Manages 8x8 board state
- Validates moves
- Detects check/checkmate/stalemate
- Converts between chess notation and positions

**ChessGame**
- Main game controller
- Handles turn switching
- Processes player input
- Maintains move history

## 🎓 Learning Resources

This implementation demonstrates:
- Object-oriented programming in Python
- Game state management
- Algorithm design (move validation, check detection)
- User input handling and validation
- Data structure management (2D arrays, enums)

## 📜 License

This project is open source and available for educational purposes.

## 🤝 Contributing

Feel free to extend this project with:
- GUI using Tkinter or Pygame
- AI opponent using minimax algorithm
- Network multiplayer support
- Move notation with piece names (e.g., Nf3 for knight to f3)
- Castling and en passant special moves
- Time controls
- Rating/ELO system

---

**Enjoy your game! ♟️♔**
