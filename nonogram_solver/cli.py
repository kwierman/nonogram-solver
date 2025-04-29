import logging

import click

from .board import Board
from .generator import BoardGenerator
from .solvers import solver_factory


@click.command()
@click.option(
    "--board-size", "-b", default=10, help="The Size of the board to generate"
)
@click.option("--visualize", "-v", default=False, help="Visualize the Board?")
@click.option(
    "--visualize-time", "-t", default=1.0, help="Visualization Time Per Solve"
)
@click.option("--solver", "-s", default="basic", help="Which solver to use")
@click.option("--n-boards", "-b", default=10, help="Number of Board to Generate")
def main(
    board_size=10, visualize=False, visualize_time=1.0, solver="basic", n_boards=10
):
    logging.basicConfig(level=logging.INFO)
    solver_name = solver

    n_solved = 0
    for i in range(n_boards):
        logging.info(f"Starting run {i}")
        generator = BoardGenerator(board_size)

        logging.info("Filling Board")
        truth = generator.fill_board()

        if visualize:
            logging.info("Visualizing Truth")
            generator.truth.visualize(
                visualize_time=visualize_time, title=f"Truth run {i}"
            )

        logging.info("Creating Unsolved Board")
        unsolved = Board(board_size)
        unsolved.set_edges(truth.get_edges())

        # Create the Solver
        logging.info("Creating Solver")
        solver = solver_factory(name=solver_name, truth=unsolved)

        n_solved += solver.solve(visualize=visualize, visualize_time=visualize_time)
    logging.info(
        f"For a total of {n_boards}, The number of successful solutions is {n_solved}"
    )


if __name__ == "__main__":
    main()
