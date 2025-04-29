from typing import List, Tuple

import logging
from enum import Enum

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import numpy as np


class BoardState(Enum):
    OPEN = 0  # Don't know if it's Closed or not
    MARKED = 1  # Mark as not Closed
    CLOSED = 2  # Means part of a closed sequence


class Board:
    logger = logging.getLogger("nonogram.board")

    def __init__(self, size: int = 10):
        """Implements a board of shape (size, size), where the axes are (x,y)"""
        self.size = size
        self.board = np.zeros(shape=(size, size))
        self.xlabels = [
            [
                0,
            ]
            for _ in range(size)
        ]
        self.ylabels = [
            [
                0,
            ]
            for _ in range(size)
        ]

    def visualize(self, visualize_time: float, title: str = "Truth") -> None:

        fig, ax = plt.subplots()
        im = ax.imshow(self.board)

        # Show all ticks and label them with the respective list entries
        ax.set_xticks(
            range(self.size),
            labels=[str(i) for i in self.xlabels],
            rotation=45,
            ha="right",
            rotation_mode="anchor",
        )
        ax.set_yticks(range(self.size), labels=[str(i) for i in self.ylabels])

        ax.set_title(title)

        colors = [
            im.cmap(im.norm(value))
            for value in [
                BoardState.OPEN.value,
                BoardState.MARKED.value,
                BoardState.CLOSED.value,
            ]
        ]
        # create a patch (proxy artist) for every color
        patches = [
            mpatches.Patch(color=colors[0], label="OPEN"),
            mpatches.Patch(color=colors[1], label="MARKED"),
            mpatches.Patch(color=colors[2], label="CLOSED"),
        ]
        # put those patched as legend-handles into the legend
        plt.legend(handles=patches, bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.0)

        fig.tight_layout()

        plt.show(block=False)
        plt.pause(visualize_time)

        # Close the plot window after the pause
        plt.close()

    def set_edges(self, edges: tuple[list[list[int]], list[list[int]]]) -> None:
        self.xlabels = edges[0]
        self.ylabels = edges[1]

    def get_edges(self) -> tuple[list[list[int]], list[list[int]]]:
        return self.xlabels, self.ylabels

    def mark(self, x: int, y: int, value: BoardState) -> None:
        if x >= self.board.shape[0] or y >= self.board.shape[1]:
            raise ValueError(
                f"Board Indices out of bounds <{{x,y}}> for board shape {self.board.shape}"
            )
        self.board[x, y] = value  # type: ignore
