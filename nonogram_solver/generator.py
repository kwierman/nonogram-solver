import numpy as np

from .board import Board, BoardState


class BoardGenerator:
    def __init__(self, board_size=10):
        self.truth = Board(board_size)
        self.board_size = board_size

    def fill_board(self) -> Board:
        self.truth.board = np.random.choice(
            a=[BoardState.MARKED.value, BoardState.CLOSED.value],
            size=self.truth.board.shape,
            p=[0.5, 0.5],
        )  # type: ignore

        # Setup the x labels
        row_labels = []
        for x in range(self.board_size):
            current_state = BoardState.MARKED.value
            row = self.truth.board[x, :]
            row_label = []
            for y in row:
                if y == BoardState.MARKED.value:
                    if current_state == BoardState.MARKED.value:
                        ...
                    else:
                        ...

                else:  # y is CLOSED
                    if current_state == BoardState.MARKED.value:
                        row_label.append(1)
                    else:
                        row_label[-1] += 1
                current_state = y
            row_labels.append(row_label)

        # Setup the x labels
        col_labels = []
        for y in range(self.board_size):
            current_state = BoardState.MARKED.value
            col = self.truth.board[:, y]
            col_label = []
            for x in col:
                if x == BoardState.MARKED.value:
                    if current_state == BoardState.MARKED.value:
                        ...
                    else:
                        ...

                else:  # x is CLOSED
                    if current_state == BoardState.MARKED.value:
                        col_label.append(1)
                    else:
                        col_label[-1] += 1
                current_state = x
            col_labels.append(col_label)

        self.truth.set_edges((col_labels, row_labels))

        return self.truth
