from typing import List, Tuple, NewType, Self
from enum import Enum

class CellType(Enum):
    UNCLEAN = 0
    WALL = 1
    CLEAN = 2

    def __str__(self) -> str:
        if self == Self.UNCLEAN:
            return "."
        elif self == Self.WALL:
            return "X"
        elif self == Self.CLEAN:
            return " "

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    def anticlockwise(self) -> Self:
        """
        Example:
            >>> dir = Direction.NORTH
            >>> assert dir.anticlockwise() == Direction.WEST
        """
        if self == Direction.NORTH:
            return Direction.WEST
        elif self == Direction.WEST:
            return Direction.SOUTH
        elif self == Direction.SOUTH:
            return Direction.EAST
        elif self == Direction.EAST:
            return Direction.NORTH

class Position(Tuple[int, int]):
    """
    좌표를 나타냅니다. (x, y) 순입니다.
    """
    # alias 타입 만들려면 NewType 쓰면 되는데, `forward`, `backward` 함수 숨기고
    # 싶었어요

    # forward, backward에 쓰기 위한 맵
    delta_map = {
        Direction.NORTH: (0, -1),
        Direction.EAST: (+1, 0),
        Direction.SOUTH: (0, +1),
        Direction.WEST: (-1, 0),
    }

    @classmethod
    def forward(cls, pos: Self, dir: Direction) -> Self:
        """
        Example:
            >>> pos = (1, 2)
            >>> assert (2, 3) == Position.forward(pos, Direction.WEST)
        """
        x, y = pos
        dx, dy = cls.delta_map[dir]
        return (x + dx, y + dy)

    @classmethod
    def backward(cls, pos: Self, dir: Direction) -> Self:
        x, y = pos
        dx, dy = cls.delta_map[dir]
        return (x - dx, y - dy)

class Room():
    room: List[List[CellType]]
    def __init__(self, str: str):
        """
        주어진 문자열을 파싱하여 2차원 배열의 방을 만듭니다.
        """
        lines = str.split("\n")
        self.room = [
            [CellType(int(cell)) for cell in line.split()] for line in lines
        ]

    def is_unclean(self, position: Position) -> bool:
        x, y = position
        return self.room[y][x] == CellType.UNCLEAN

    def is_wall(self, position: Position) -> bool:
        x, y = position
        return self.room[y][x] == CellType.WALL

    def set_clean(self, position: Position):
        x, y = position
        self.room[y][x] = CellType.CLEAN

    def __str__(self) -> str:
        return '\n'.join([' '.join(map(str, line)) for line in self.room])

class Roomba:
    current: Position
    heading: Direction
    room: Room
    clean_count: int

    def __init__(self, position: Position, room: Room, heading: Direction):
        """
        :param position: 초기 시작 위치 (x, y)
        """
        self.current = position
        self.room = room
        self.heading = heading
        self.clean_count = 0

    def run(self):
        while self.next_step():
            pass

    def next_step(self) -> bool:
        """
        한 차례 움직입니다. 더 움직일 수 없다면 False를 반환합니다.
        """

        # 하라면 대로 하면 되긴 하는데...
        if self.room.is_unclean(self.current):
            self.room.set_clean(self.current)
            self.clean_count += 1
        adjacents = self.adjacent_positions()
        if not any(map(lambda x: self.room.is_unclean(x), adjacents)):
            backward = Position.backward(self.current, self.heading)
            if not self.room.is_wall(backward):
                self.current = backward
            else:
                return False
        else:
            self.heading = self.heading.anticlockwise()
            forward = Position.forward(self.current, self.heading)
            if self.room.is_unclean(forward):
                self.current = forward
        return True

    def adjacent_positions(self) -> List[Position]:
        """
        동. 서, 남, 북으로 인접한 칸을 배열로 반환합니다.
        """
        x, y = self.current
        deltas = [(0, -1), (0, +1), (-1, 0), (+1, 0)]
        return [(x + xd, y + yd) for (xd, yd) in deltas]

if __name__ == '__main__':
    import sys
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())

    # `sys.stdin.read` 함수 쓰면 EOF까지 싹 가져올 수 있어요
    room = Room(sys.stdin.read())

    # 문제에서는 (세로좌표, 가로좌표) 순인데, 반대로 생각하고 코딩해서
    # 여기서 바꿔줬습니다.
    roomba = Roomba((c, r), room, Direction(d))
    roomba.run()
    print(roomba.clean_count)
