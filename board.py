"""
Chess Game - Board management and move validation
"""

from pieces import (
    Piece, Pawn, Knight, Bishop, Rook, Queen, King, PieceType, Color
)
from typing import Optional, List, Tuple

class Board:
    """Chess board management"""
    
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.initialize_board()
    
    def initialize_board(self):
        """Set up the chess board with standard starting position"""
        # Black pieces (top)
        self.board[0][0] = Rook(Color.BLACK)
        self.board[0][1] = Knight(Color.BLACK)
        self.board[0][2] = Bishop(Color.BLACK)
        self.board[0][3] = Queen(Color.BLACK)
        self.board[0][4] = King(Color.BLACK)
        self.board[0][5] = Bishop(Color.BLACK)
        self.board[0][6] = Knight(Color.BLACK)
        self.board[0][7] = Rook(Color.BLACK)
        
        for col in range(8):
            self.board[1][col] = Pawn(Color.BLACK)
        
        # White pieces (bottom)
        for col in range(8):
            self.board[6][col] = Pawn(Color.WHITE)
        
        self.board[7][0] = Rook(Color.WHITE)
        self.board[7][1] = Knight(Color.WHITE)
        self.board[7][2] = Bishop(Color.WHITE)
        self.board[7][3] = Queen(Color.WHITE)
        self.board[7][4] = King(Color.WHITE)
        self.board[7][5] = Bishop(Color.WHITE)
        self.board[7][6] = Knight(Color.WHITE)
        self.board[7][7] = Rook(Color.WHITE)
    
    def get_piece(self, row: int, col: int) -> Optional[Piece]:
        """Get piece at position"""
        if 0 <= row < 8 and 0 <= col < 8:
            return self.board[row][col]
        return None
    
    def set_piece(self, row: int, col: int, piece: Optional[Piece]):
        """Set piece at position"""
        if 0 <= row < 8 and 0 <= col < 8:
            self.board[row][col] = piece
    
    @staticmethod
    def notation_to_position(notation: str) -> Tuple[Optional[int], Optional[int]]:
        """Convert chess notation (e.g., 'e2') to board position (row, col)"""
        if len(notation) != 2:
            return None, None
        
        col_char = notation[0].lower()
        row_char = notation[1]
        
        if col_char < 'a' or col_char > 'h' or row_char < '1' or row_char > '8':
            return None, None
        
        col = ord(col_char) - ord('a')
        row = 8 - int(row_char)
        
        return row, col
    
    @staticmethod
    def position_to_notation(row: int, col: int) -> str:
        """Convert board position (row, col) to chess notation (e.g., 'e2')"""
        col_char = chr(ord('a') + col)
        row_char = str(8 - row)
        return col_char + row_char
    
    def move_piece(self, from_row: int, from_col: int, to_row: int, to_col: int) -> bool:
        """
        Move a piece from one position to another
        Returns True if move was successful
        """
        piece = self.get_piece(from_row, from_col)
        
        if piece is None:
            return False
        
        # Get possible moves for the piece
        possible_moves = piece.get_possible_moves(from_row, from_col, self)
        
        if (to_row, to_col) not in possible_moves:
            return False
        
        # Make the move
        self.set_piece(to_row, to_col, piece)
        self.set_piece(from_row, from_col, None)
        piece.moved = True
        
        # Check if this move leaves own king in check
        if self.is_in_check(piece.color):
            # Undo the move
            self.set_piece(from_row, from_col, piece)
            self.set_piece(to_row, to_col, None)
            piece.moved = False
            return False
        
        # Pawn promotion
        if piece.type == PieceType.PAWN:
            if (piece.color == Color.WHITE and to_row == 0) or \
               (piece.color == Color.BLACK and to_row == 7):
                self.set_piece(to_row, to_col, Queen(piece.color))
        
        return True
    
    def find_king(self, color: Color) -> Tuple[Optional[int], Optional[int]]:
        """Find the king position for a given color"""
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece and piece.type == PieceType.KING and piece.color == color:
                    return row, col
        return None, None
    
    def is_in_check(self, color: Color) -> bool:
        """Check if a player's king is in check"""
        king_row, king_col = self.find_king(color)
        
        if king_row is None:
            return False
        
        # Check if any opponent piece can attack the king
        opponent_color = Color.BLACK if color == Color.WHITE else Color.WHITE
        
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece and piece.color == opponent_color:
                    moves = piece.get_possible_moves(row, col, self)
                    if (king_row, king_col) in moves:
                        return True
        
        return False
    
    def has_legal_moves(self, color: Color) -> bool:
        """Check if a player has any legal moves"""
        for row in range(8):
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece and piece.color == color:
                    moves = piece.get_possible_moves(row, col, self)
                    for to_row, to_col in moves:
                        # Try the move
                        target = self.get_piece(to_row, to_col)
                        self.set_piece(to_row, to_col, piece)
                        self.set_piece(row, col, None)
                        
                        # Check if king is in check after move
                        legal = not self.is_in_check(color)
                        
                        # Undo the move
                        self.set_piece(row, col, piece)
                        self.set_piece(to_row, to_col, target)
                        
                        if legal:
                            return True
        
        return False
    
    def is_checkmate(self, color: Color) -> bool:
        """Check if a player is in checkmate"""
        return self.is_in_check(color) and not self.has_legal_moves(color)
    
    def is_stalemate(self, color: Color) -> bool:
        """Check if a player is in stalemate"""
        return not self.is_in_check(color) and not self.has_legal_moves(color)
    
    def display(self):
        """Display the chess board"""
        print("  a b c d e f g h")
        print("  ───────────────")
        
        for row in range(8):
            print(f"{8 - row}│", end=" ")
            for col in range(8):
                piece = self.get_piece(row, col)
                if piece is None:
                    print("·", end=" ")
                else:
                    print(str(piece), end=" ")
            print(f"│{8 - row}")
        
        print("  ───────────────")
        print("  a b c d e f g h")
        print()
