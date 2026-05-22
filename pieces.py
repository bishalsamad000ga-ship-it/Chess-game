"""
Chess Game - Piece definitions and movement logic
"""

from enum import Enum
from typing import List, Tuple

class PieceType(Enum):
    PAWN = 1
    KNIGHT = 2
    BISHOP = 3
    ROOK = 4
    QUEEN = 5
    KING = 6

class Color(Enum):
    WHITE = 1
    BLACK = 2

class Piece:
    """Base class for all chess pieces"""
    
    def __init__(self, piece_type: PieceType, color: Color):
        self.type = piece_type
        self.color = color
        self.moved = False  # Track if piece has moved (for castling/pawn promotion)
    
    def __repr__(self):
        """Return Unicode representation of the piece"""
        pieces_white = {
            PieceType.PAWN: '♙',
            PieceType.KNIGHT: '♘',
            PieceType.BISHOP: '♗',
            PieceType.ROOK: '♖',
            PieceType.QUEEN: '♕',
            PieceType.KING: '♔',
        }
        pieces_black = {
            PieceType.PAWN: '♟',
            PieceType.KNIGHT: '♞',
            PieceType.BISHOP: '♝',
            PieceType.ROOK: '♜',
            PieceType.QUEEN: '♛',
            PieceType.KING: '♚',
        }
        
        if self.color == Color.WHITE:
            return pieces_white[self.type]
        else:
            return pieces_black[self.type]
    
    def get_possible_moves(self, row: int, col: int, board: 'Board') -> List[Tuple[int, int]]:
        """
        Get all possible moves for this piece from the given position.
        Subclasses override this method.
        """
        raise NotImplementedError
    
    @staticmethod
    def is_valid_position(row: int, col: int) -> bool:
        """Check if position is within board bounds"""
        return 0 <= row < 8 and 0 <= col < 8


class Pawn(Piece):
    def __init__(self, color: Color):
        super().__init__(PieceType.PAWN, color)
    
    def get_possible_moves(self, row: int, col: int, board: 'Board') -> List[Tuple[int, int]]:
        moves = []
        direction = -1 if self.color == Color.WHITE else 1
        start_row = 6 if self.color == Color.WHITE else 1
        
        # Forward move
        new_row = row + direction
        if self.is_valid_position(new_row, col) and board.get_piece(new_row, col) is None:
            moves.append((new_row, col))
            
            # Double move from starting position
            if row == start_row:
                new_row = row + 2 * direction
                if board.get_piece(new_row, col) is None:
                    moves.append((new_row, col))
        
        # Capture diagonally
        for new_col in [col - 1, col + 1]:
            new_row = row + direction
            if self.is_valid_position(new_row, new_col):
                target = board.get_piece(new_row, new_col)
                if target and target.color != self.color:
                    moves.append((new_row, new_col))
        
        # En passant (simplified - not fully implemented)
        
        return moves


class Knight(Piece):
    def __init__(self, color: Color):
        super().__init__(PieceType.KNIGHT, color)
    
    def get_possible_moves(self, row: int, col: int, board: 'Board') -> List[Tuple[int, int]]:
        moves = []
        knight_moves = [
            (-2, -1), (-2, 1), (-1, -2), (-1, 2),
            (1, -2), (1, 2), (2, -1), (2, 1)
        ]
        
        for dr, dc in knight_moves:
            new_row, new_col = row + dr, col + dc
            if self.is_valid_position(new_row, new_col):
                target = board.get_piece(new_row, new_col)
                if target is None or target.color != self.color:
                    moves.append((new_row, new_col))
        
        return moves


class Bishop(Piece):
    def __init__(self, color: Color):
        super().__init__(PieceType.BISHOP, color)
    
    def get_possible_moves(self, row: int, col: int, board: 'Board') -> List[Tuple[int, int]]:
        moves = []
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            while self.is_valid_position(new_row, new_col):
                target = board.get_piece(new_row, new_col)
                if target is None:
                    moves.append((new_row, new_col))
                elif target.color != self.color:
                    moves.append((new_row, new_col))
                    break
                else:
                    break
                new_row += dr
                new_col += dc
        
        return moves


class Rook(Piece):
    def __init__(self, color: Color):
        super().__init__(PieceType.ROOK, color)
    
    def get_possible_moves(self, row: int, col: int, board: 'Board') -> List[Tuple[int, int]]:
        moves = []
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            while self.is_valid_position(new_row, new_col):
                target = board.get_piece(new_row, new_col)
                if target is None:
                    moves.append((new_row, new_col))
                elif target.color != self.color:
                    moves.append((new_row, new_col))
                    break
                else:
                    break
                new_row += dr
                new_col += dc
        
        return moves


class Queen(Piece):
    def __init__(self, color: Color):
        super().__init__(PieceType.QUEEN, color)
    
    def get_possible_moves(self, row: int, col: int, board: 'Board') -> List[Tuple[int, int]]:
        moves = []
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (1, -1), (1, 0), (1, 1)
        ]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            while self.is_valid_position(new_row, new_col):
                target = board.get_piece(new_row, new_col)
                if target is None:
                    moves.append((new_row, new_col))
                elif target.color != self.color:
                    moves.append((new_row, new_col))
                    break
                else:
                    break
                new_row += dr
                new_col += dc
        
        return moves


class King(Piece):
    def __init__(self, color: Color):
        super().__init__(PieceType.KING, color)
    
    def get_possible_moves(self, row: int, col: int, board: 'Board') -> List[Tuple[int, int]]:
        moves = []
        directions = [
            (-1, -1), (-1, 0), (-1, 1), (0, -1),
            (0, 1), (1, -1), (1, 0), (1, 1)
        ]
        
        for dr, dc in directions:
            new_row, new_col = row + dr, col + dc
            if self.is_valid_position(new_row, new_col):
                target = board.get_piece(new_row, new_col)
                if target is None or target.color != self.color:
                    moves.append((new_row, new_col))
        
        # Castling (simplified - not fully implemented)
        
        return moves
