"""
Chess Game - Main game controller and UI
"""

from board import Board
from pieces import Color

class ChessGame:
    """Main chess game controller"""
    
    def __init__(self):
        self.board = Board()
        self.current_player = Color.WHITE
        self.move_history = []
        self.game_over = False
        self.winner = None
    
    def switch_player(self):
        """Switch to the other player"""
        self.current_player = Color.BLACK if self.current_player == Color.WHITE else Color.WHITE
    
    def make_move(self, from_notation: str, to_notation: str) -> bool:
        """
        Make a move in chess notation (e.g., 'e2' 'e4')
        Returns True if move was successful
        """
        from_row, from_col = self.board.notation_to_position(from_notation)
        to_row, to_col = self.board.notation_to_position(to_notation)
        
        if from_row is None or to_row is None:
            print("❌ Invalid notation. Use format: a1 b2")
            return False
        
        piece = self.board.get_piece(from_row, from_col)
        
        if piece is None:
            print("❌ No piece at that position")
            return False
        
        if piece.color != self.current_player:
            print(f"❌ That's not your piece! It's {self.current_player.name}'s turn.")
            return False
        
        if self.board.move_piece(from_row, from_col, to_row, to_col):
            move_notation = f"{from_notation} → {to_notation}"
            self.move_history.append(move_notation)
            print(f"✓ {self.current_player.name} moves {move_notation}")
            
            # Check game status
            self.switch_player()
            
            if self.board.is_checkmate(self.current_player):
                self.game_over = True
                self.winner = "White" if self.current_player == Color.BLACK else "Black"
                print(f"\n🎉 CHECKMATE! {self.winner} wins!")
                return True
            
            if self.board.is_stalemate(self.current_player):
                self.game_over = True
                print("\n🤝 STALEMATE! The game is a draw.")
                return True
            
            if self.board.is_in_check(self.current_player):
                print(f"⚠️  CHECK! {self.current_player.name} king is under attack!")
            
            return True
        else:
            print("❌ Illegal move")
            return False
    
    def display_status(self):
        """Display current game status"""
        print(f"\n{'='*40}")
        print(f"Current Player: {self.current_player.name}")
        print(f"{'='*40}\n")
        self.board.display()
    
    def display_history(self):
        """Display move history"""
        if not self.move_history:
            print("No moves yet!")
            return
        
        print("\n📜 Move History:")
        for i, move in enumerate(self.move_history, 1):
            print(f"{i}. {move}")
        print()
    
    def reset_game(self):
        """Reset the game"""
        self.board = Board()
        self.current_player = Color.WHITE
        self.move_history = []
        self.game_over = False
        self.winner = None
        print("✓ Game reset!")
    
    def run(self):
        """Main game loop"""
        print("\n" + "="*50)
        print("  ♟️  WELCOME TO CHESS GAME ♟️")
        print("="*50)
        print("\nCommands:")
        print("  - Move: enter two positions (e.g., 'e2 e4')")
        print("  - History: view move history")
        print("  - Reset: start a new game")
        print("  - Quit: exit the game")
        print("\n" + "="*50 + "\n")
        
        self.display_status()
        
        while not self.game_over:
            try:
                user_input = input(f"{self.current_player.name}'s move: ").strip().lower()
                
                if user_input == "quit":
                    print("Thanks for playing! 👋")
                    break
                elif user_input == "history":
                    self.display_history()
                elif user_input == "reset":
                    self.reset_game()
                    self.display_status()
                elif " " in user_input:
                    parts = user_input.split()
                    if len(parts) == 2:
                        from_pos, to_pos = parts
                        if self.make_move(from_pos, to_pos):
                            self.display_status()
                    else:
                        print("❌ Invalid format. Use: position1 position2")
                else:
                    print("❌ Unknown command. Try 'e2 e4' to move or 'help' for commands.")
            
            except KeyboardInterrupt:
                print("\n\nGame interrupted. Thanks for playing! 👋")
                break
            except Exception as e:
                print(f"❌ Error: {e}")


def main():
    """Entry point for the chess game"""
    game = ChessGame()
    game.run()


if __name__ == "__main__":
    main()
