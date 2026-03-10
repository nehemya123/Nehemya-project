import pygame
import sys
from chess_ai import ChessAI

pygame.init()

WIDTH, HEIGHT = 640, 640
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH // COLS

WHITE = (240, 217, 181)
BROWN = (181, 136, 99)
HIGHLIGHT = (100, 200, 100)
TEXT_COLOR = (20, 20, 20)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Chess Game")
font = pygame.font.SysFont(None, 44)

initial_board = [
    ["bR", "bN", "bB", "bQ", "bK", "bB", "bN", "bR"],
    ["bP", "bP", "bP", "bP", "bP", "bP", "bP", "bP"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["--", "--", "--", "--", "--", "--", "--", "--"],
    ["wP", "wP", "wP", "wP", "wP", "wP", "wP", "wP"],
    ["wR", "wN", "wB", "wQ", "wK", "wB", "wN", "wR"],
]

piece_symbols = {
    "wK": "K", "wQ": "Q", "wR": "R", "wB": "B", "wN": "N", "wP": "P",
    "bK": "K", "bQ": "Q", "bR": "R", "bB": "B", "bN": "N", "bP": "P"
}


class ChessGame:
    def __init__(self):
        self.board = [row[:] for row in initial_board]
        self.selected = None
        self.valid_moves = []
        self.white_turn = True
        self.ai = ChessAI()

    def draw_board(self):
        for row in range(ROWS):
            for col in range(COLS):
                color = WHITE if (row + col) % 2 == 0 else BROWN
                pygame.draw.rect(
                    screen, color,
                    (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE)
                )

                if self.selected == (row, col):
                    pygame.draw.rect(
                        screen, HIGHLIGHT,
                        (col * SQUARE_SIZE, row * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 4
                    )

                if (row, col) in self.valid_moves:
                    pygame.draw.circle(
                        screen, HIGHLIGHT,
                        (col * SQUARE_SIZE + SQUARE_SIZE // 2, row * SQUARE_SIZE + SQUARE_SIZE // 2),
                        10
                    )

                piece = self.board[row][col]
                if piece != "--":
                    text = font.render(piece_symbols[piece], True, TEXT_COLOR)
                    text_rect = text.get_rect(center=(
                        col * SQUARE_SIZE + SQUARE_SIZE // 2,
                        row * SQUARE_SIZE + SQUARE_SIZE // 2
                    ))
                    screen.blit(text, text_rect)

    def get_piece_moves(self, row, col):
        piece = self.board[row][col]
        if piece == "--":
            return []

        color = piece[0]
        kind = piece[1]
        moves = []

        directions = []
        if kind == "P":
            step = -1 if color == "w" else 1
            start_row = 6 if color == "w" else 1

            if 0 <= row + step < 8 and self.board[row + step][col] == "--":
                moves.append((row + step, col))
                if row == start_row and self.board[row + 2 * step][col] == "--":
                    moves.append((row + 2 * step, col))

            for dc in [-1, 1]:
                nr, nc = row + step, col + dc
                if 0 <= nr < 8 and 0 <= nc < 8:
                    if self.board[nr][nc] != "--" and self.board[nr][nc][0] != color:
                        moves.append((nr, nc))

        elif kind == "N":
            jumps = [
                (-2, -1), (-2, 1), (-1, -2), (-1, 2),
                (1, -2), (1, 2), (2, -1), (2, 1)
            ]
            for dr, dc in jumps:
                nr, nc = row + dr, col + dc
                if 0 <= nr < 8 and 0 <= nc < 8:
                    if self.board[nr][nc] == "--" or self.board[nr][nc][0] != color:
                        moves.append((nr, nc))

        elif kind == "B":
            directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        elif kind == "R":
            directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        elif kind == "Q":
            directions = [
                (-1, -1), (-1, 1), (1, -1), (1, 1),
                (-1, 0), (1, 0), (0, -1), (0, 1)
            ]

        elif kind == "K":
            steps = [
                (-1, -1), (-1, 0), (-1, 1),
                (0, -1),          (0, 1),
                (1, -1),  (1, 0), (1, 1)
            ]
            for dr, dc in steps:
                nr, nc = row + dr, col + dc
                if 0 <= nr < 8 and 0 <= nc < 8:
                    if self.board[nr][nc] == "--" or self.board[nr][nc][0] != color:
                        moves.append((nr, nc))

        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                if self.board[nr][nc] == "--":
                    moves.append((nr, nc))
                else:
                    if self.board[nr][nc][0] != color:
                        moves.append((nr, nc))
                    break
                nr += dr
                nc += dc

        return moves

    def move_piece(self, start, end):
        sr, sc = start
        er, ec = end
        self.board[er][ec] = self.board[sr][sc]
        self.board[sr][sc] = "--"

        moved_piece = self.board[er][ec]
        if moved_piece == "wP" and er == 0:
            self.board[er][ec] = "wQ"
        elif moved_piece == "bP" and er == 7:
            self.board[er][ec] = "bQ"

    def get_all_moves(self, color):
        all_moves = []
        for r in range(8):
            for c in range(8):
                if self.board[r][c] != "--" and self.board[r][c][0] == color:
                    for move in self.get_piece_moves(r, c):
                        all_moves.append(((r, c), move))
        return all_moves

    def ai_turn(self):
        move = self.ai.find_best_move(self.board, self)
        if move:
            self.move_piece(move[0], move[1])
            self.white_turn = True

    def handle_click(self, pos):
        if not self.white_turn:
            return

        col = pos[0] // SQUARE_SIZE
        row = pos[1] // SQUARE_SIZE

        if self.selected:
            if (row, col) in self.valid_moves:
                self.move_piece(self.selected, (row, col))
                self.selected = None
                self.valid_moves = []
                self.white_turn = False
            else:
                self.selected = None
                self.valid_moves = []
        else:
            piece = self.board[row][col]
            if piece != "--" and piece[0] == "w":
                self.selected = (row, col)
                self.valid_moves = self.get_piece_moves(row, col)


def main():
    clock = pygame.time.Clock()
    game = ChessGame()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                game.handle_click(pygame.mouse.get_pos())

        if not game.white_turn:
            game.ai_turn()

        game.draw_board()
        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()