from typing import Optional

from ..board import Board
from .base import BaseSolver
from .basic import BasicSolver

__factory_dict__ = {}

__factory_dict__["basic"] = BasicSolver


def solver_factory(truth: Board, name: str = "basic") -> BaseSolver:
    if name not in __factory_dict__:
        raise ValueError(
            f"Solver <{name}> not in available solvers: [{__factory_dict__.keys()}]."
        )
    return __factory_dict__[name](truth)
