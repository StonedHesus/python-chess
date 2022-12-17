from abc import ABCMeta, abstractmethod
from dataclasses import dataclass
from typing import Self, Optional 

class OutOfBoundsException(Exception):
    """
    Exception raised when an index is out of bounds.

    Author: Andrei-Paul Ionescu.
    """
    pass

class UnsuportedBehaviourException(Exception):
    """
    Exception raised when an unsuported behaviour is encountered.

    Author: Andrei-Paul Ionescu.
    """
    pass

@dataclass(frozen=True, kw_only=True, slots=True)
class Piece(metaclass=ABCMeta):
    """
    An abstract represenation of a piece object.

    Attributes:
        x: The x-axis coordinate of the piece.
        y: The y-axis coordinate of the piece.
        sprite: An optional type object, which, if non-nil, it indicates the sprite assosciated with the piece object.

    Author: Andrei-Paul Ionescu.
    """

    x : int 
    y : int 
    sprite : Optional[int]
    
    @abstractmethod
    def draw(self, panel) -> None: 
        """
        Draws the piece to a provided panel, which is passed as a formal argument to the routine.

        Args:
            panel: The panel to draw upon.

        Author: Andrei-Paul Ionescu.
        """
        ...
    
    @abstractmethod
    def move(self, x, y) -> Self:
        """
        Moves the piece. The operation will yield a new piece object, since the piece type is immutable.

        Args:
            x: The x-axis coordinate of the piece.
            y: The y-axis coordinate of the piece.

        Returnss: The new piece object whose coordinates are translated to the newly provided ones.

        Implementation specification:
            Do note, that based on the given design, upon overriding, this here method will yield a exception
            if the given coordinates are out of bounds, or do not obey with the rules which the given piece
            adheres to.
        
        Author: Andrei-Paul Ionescu.
        """
        ...

@dataclass(frozen=True, kw_only = True, slots = True)
class Pawn(Piece):
    x_step : int = 1
    y_step : int = 0

    def move(self, x, y) -> Self:
        self.x += self.x_step
        self.y += self.y_step
        return self

@dataclass(frozen=True, kw_only = True, slots = True)
class Rook(Piece):
    x_step : int = 1
    y_step : int = 0

    def move(self, x, y) -> Self:
        self.x += self.x_step
        self.y += self.y_step
        return self

@dataclass(frozen=True, kw_only = True, slots = True)
class Knight(Piece):
    x_step : int = 1
    y_step : int = 0

    def move(self, x, y) -> Self:
        self.x += self.x_step
        self.y += self.y_step
        return self

@dataclass(frozen=True, kw_only = True, slots = True)
class Bishop(Piece):
    x_step : int = 1
    y_step : int = 0

    def move(self, x, y) -> Self:
        self.x += self.x_step
        self.y += self.y_step
        return self

@dataclass(frozen=True, kw_only = True, slots = True)
class King(Piece):
    x_step : int = 1
    y_step : int = 0

    def move(self, x, y) -> Self:
        self.x += self.x_step
        self.y += self.y_step
        return self

@dataclass(frozen=True, kw_only = True, slots = True)
class Queen(Piece):
    x_step : int = 1
    y_step : int = 0

    def move(self, x, y) -> Self:
        self.x += self.x_step
        self.y += self.y_step
        return self
