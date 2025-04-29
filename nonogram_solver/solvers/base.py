import logging
from abc import ABC, abstractmethod

from ..board import Board


class BaseSolver(ABC):
    logger = logging.getLogger("nonogram.solver")

    def __init__(self, board: Board):
        self.board = board

    @abstractmethod
    def solve(self, visualize: bool = False, visualize_time: float = 0.1) -> bool:
        raise NotImplementedError("This Needs to be Implemented")
