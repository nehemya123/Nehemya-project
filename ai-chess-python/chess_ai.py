import math
import copy

piece_values = {
    "P": 1,
    "N": 3,
    "B": 3,
    "R": 5,
    "Q": 9,
    "K": 100
}


class ChessAI:
    def evaluate_board(self, board):
        score = 0
        for row in board:
            for piece in row:
                if piece != "--":
                    value = piece_values[piece[1]]
                    if piece[0] == "b":
                        score += value
                    else:
                        score -= value
        return score

    def simulate_move(self, board, start, end):
        new_board = copy.deepcopy(board)
        sr, sc = start
        er, ec = end
        new_board[er][ec] = new_board[sr][sc]
        new_board[sr][sc] = "--"

        moved_piece = new_board[er][ec]
        if moved_piece == "wP" and er == 0:
            new_board[er][ec] = "wQ"
        elif moved_piece == "bP" and er == 7:
            new_board[er][ec] = "bQ"

        return new_board

    def get_all_moves_from_board(self, board, game, color):
        original_board = game.board
        game.board = board
        moves = game.get_all_moves(color)
        game.board = original_board
        return moves

    def minimax(self, board, game, depth, maximizing, alpha, beta):
        if depth == 0:
            return self.evaluate_board(board)

        color = "b" if maximizing else "w"
        moves = self.get_all_moves_from_board(board, game, color)

        if not moves:
            return self.evaluate_board(board)

        if maximizing:
            max_eval = -math.inf
            for start, end in moves:
                new_board = self.simulate_move(board, start, end)
                eval_score = self.minimax(new_board, game, depth - 1, False, alpha, beta)
                max_eval = max(max_eval, eval_score)
                alpha = max(alpha, eval_score)
                if beta <= alpha:
                    break
            return max_eval
        else:
            min_eval = math.inf
            for start, end in moves:
                new_board = self.simulate_move(board, start, end)
                eval_score = self.minimax(new_board, game, depth - 1, True, alpha, beta)
                min_eval = min(min_eval, eval_score)
                beta = min(beta, eval_score)
                if beta <= alpha:
                    break
            return min_eval

    def find_best_move(self, board, game):
        best_score = -math.inf
        best_move = None
        moves = self.get_all_moves_from_board(board, game, "b")

        for start, end in moves:
            new_board = self.simulate_move(board, start, end)
            score = self.minimax(new_board, game, 2, False, -math.inf, math.inf)
            if score > best_score:
                best_score = score
                best_move = (start, end)

        return best_move