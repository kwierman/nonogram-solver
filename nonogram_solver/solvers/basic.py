from ..board import BoardState
from .base import BaseSolver


class BasicSolver(BaseSolver):

    def solve(self, visualize=False, visualize_time=0.1, solver_passes=100):
        for pass_n in range(solver_passes):
            for x in range(self.board.size):
                arr = self.board.board[:, x]
                edge = self.board.get_edges()[0][x]

                self.reduce_most_basic(arr, edge)
                self.reduce_arithmetic(arr, edge)
                self.reduce_solve_from_edge(arr, edge)
                self.reduce_solve_fill(arr, edge)

            for y in range(self.board.size):
                arr = self.board.board[y, :]
                edge = self.board.get_edges()[1][y]

                self.reduce_most_basic(arr, edge)
                self.reduce_arithmetic(arr, edge)
                self.reduce_solve_from_edge(arr, edge)
                self.reduce_solve_fill(arr, edge)
            if not (self.board.board == BoardState.OPEN.value).any():
                self.logger.info(f"Board Solved after {pass_n} passes")
                break

        if visualize:
            self.board.visualize(visualize_time, title=f"Solver Pass {pass_n}")

        if (self.board.board == BoardState.OPEN.value).any():
            self.logger.warning("BOARD IS UNSOLVED")
            return False
        return True

    def most_basic_solution(self, arr, edges):
        if len(edges) == 1 and edges[0] == len(arr):
            arr[:] = BoardState.CLOSED.value
        elif len(edges) == 0:
            arr[:] = BoardState.MARKED.value

    def reduce_most_basic(self, arr, edges):
        # Trim down the selection
        while arr[0] == BoardState.MARKED.value:
            arr = arr[1:]
        while arr[-1] == BoardState.MARKED.value:
            arr = arr[:-1]
        self.most_basic_solution(arr, edges)

    def arithmetic_solve(self, arr, edges):
        """In this given array, try and"""
        if len(edges) - 1 + sum(edges) == self.board.size:
            curr_index = 0
            for edge in edges:
                arr[curr_index : curr_index + edge] = BoardState.CLOSED.value
                curr_index += edge + 1
                if curr_index - 1 < len(arr):
                    arr[curr_index - 1] = BoardState.MARKED.value

    def reduce_arithmetic(self, arr, edges):
        # Trim down the selection
        while arr[0] == BoardState.MARKED.value:
            arr = arr[1:]
        while arr[-1] == BoardState.MARKED.value:
            arr = arr[:-1]
        self.arithmetic_solve(arr, edges)

    def solve_from_edge(self, arr, edges):
        if arr[0] == BoardState.CLOSED.value:
            arr[: edges[0]] == BoardState.CLOSED.value
        if arr[-1] == BoardState.CLOSED.value:
            arr[-edges[-1] :] == BoardState.CLOSED.value

    def reduce_solve_from_edge(self, arr, edges):
        # Trim down the selection
        while arr[0] == BoardState.MARKED.value:
            arr = arr[1:]
        while arr[-1] == BoardState.MARKED.value:
            arr = arr[:-1]
        self.solve_from_edge(arr, edges)

    def solve_fill(self, arr, edges):
        sub_array = arr[: edges[0]]
        if (sub_array == BoardState.CLOSED.value).any():
            while sub_array[0] != BoardState.CLOSED.value:
                sub_array = sub_array[1:]
            sub_array = BoardState.CLOSED.value
        sub_array = arr[-edges[-1] :]
        if (sub_array == BoardState.CLOSED.value).any():
            while sub_array[-1] != BoardState.CLOSED.value:
                sub_array = sub_array[:-1]
            sub_array = BoardState.CLOSED.value

    def reduce_solve_fill(self, arr, edges):
        # Trim down the selection
        while arr[0] == BoardState.MARKED.value:
            arr = arr[1:]
        while arr[-1] == BoardState.MARKED.value:
            arr = arr[:-1]
        self.solve_fill(arr, edges)
