from dataclasses import dataclass
from abc import ABC, abstractmethod
from typing import Self


@dataclass(frozen=True, kw_only=True, slots=True)
class Board(ABC):
    """
        It is crucial to note, that based on the design choices of the developers, aka yours truly; there is a
        need for a base, abstract type for the board, due to one sole reason:

                The software will allow the instantiation of different modes of chess, or games that utilise 
                the chessboard and its pieces. 

        Hence, in order to be able to minimise cohesion, and to allow further scaling to be as natural as
        possible, I had decided to introduce the abstract 'proto' type, or core type if you will; for the board
        hierarchy, ensuring us that a board abides to certain characteristics and behavioural patterns.
    """
    width: int
    height: int
    board: list[list]

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def get_dimensions(self) -> tuple[int, int]:
        return self.width, self.height

    def get_piece(self, x: int, y: int):
        if x < 0 or x >= self.width:
            raise IndexError(
                "It appears that the provided x-coordinate is out of bounds.")
        if y < 0 or y >= self.height:
            raise IndexError(
                "It appears that the provided y-coordinate is out of bounds.")

        return self.board[x][y]

    @staticmethod
    @abstractmethod
    def new_board() -> Self:
        ...


def _fill_board_with_none(width: int, height: int) -> list[list]:
    return [[None for _ in range(width)] for _ in range(height)]


class StandardBoard(Board):
    """
        The StandardBoard class represents a specialisation of the abstract board type.
        Its role is to represent the standard chessboard, which is comprised of eight rows and eight columns.

        The sole method that needs to be altered is the static abstractly defined within the base type, method 
        new_board(), which acts as a static factory method.
    """

    @staticmethod
    def new_board() -> Self:
        return StandardBoard(width=8, height=8, board=_fill_board_with_none(8, 8))
