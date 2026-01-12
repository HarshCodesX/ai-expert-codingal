def print_board(board):
    """Prints the current state of the board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

def check_winner(board):
    """Checks if there's a winner or a tie."""
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
            
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
        
    # Check for tie
    if all(cell != " " for row in board for cell in row):
        return "Tie"
        
    return None

def main():
    """Main game loop."""
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    print("Welcome to Tic Tac Toe!")
    
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn.")
        
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            
            if board[row][col] == " ":
                board[row][col] = current_player
                
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    if winner == "Tie":
                        print("It's a tie!")
                    else:
                        print(f"Player {winner} wins!")
                    break
                
                # Switch players
                current_player = "O" if current_player == "X" else "X"
            else:
                print("That spot is already taken! Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter 0, 1, or 2 for both row and column.")

if __name__ == "__main__":
    main()
