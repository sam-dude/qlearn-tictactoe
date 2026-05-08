# game.py

from typing import List, Tuple, Optional

class TicTacToe:
    def __init__(self):
        self.reset()

    def reset(self) -> str:
        """Reset the board and return initial state"""
        self.board = ["-"] * 9
        self.current_player = "X"
        self.done = False
        self.winner = None
        return self.get_state()

    def get_state(self) -> str:
        """Return state as a string"""
        return "".join(self.board)

    def available_actions(self) -> List[int]:
        """Return indices of empty cells"""
        return [i for i, cell in enumerate(self.board) if cell == "-"]

    def step(self, action: int) -> Tuple[str, int, bool]:
        """
        Apply action and return:
        (next_state, reward, done)
        """
        if self.done:
            raise Exception("Game already finished")

        if self.board[action] != "-":
            raise ValueError(f"Invalid action {action}")

        # Place mark
        self.board[action] = self.current_player

        # Check result
        self.winner = self.check_winner()

        if self.winner:
            self.done = True
            reward = 1 if self.winner == "X" else -1
            return self.get_state(), reward, True

        if "-" not in self.board:
            self.done = True
            return self.get_state(), 0, True  # draw

        # Switch player
        self.current_player = "O" if self.current_player == "X" else "X"

        return self.get_state(), 0, False

    def check_winner(self) -> Optional[str]:
        """Return 'X', 'O', or None"""
        lines = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # cols
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]

        for a, b, c in lines:
            if self.board[a] == self.board[b] == self.board[c] != "-":
                return self.board[a]

        return None

    def render(self):
        """Print the board (for debugging)"""
        for i in range(0, 9, 3):
            print(self.board[i:i+3])
        print()