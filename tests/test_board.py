from nonogram_solver.board import Board


def test_board():
    board = Board()
    assert board.size == 10
    assert board.board.shape == (10, 10)
