from typing import List, Self, Tuple
from enum import Enum, auto

class Direction(Enum):
    UP = auto()
    DOWN = auto()
    LEFT = auto()
    RIGHT = auto()

    def __str__(self):
        return self.name

    def clockwise(self) -> Self:
        """
        Example:
            >>> dir = Direction.UP
            >>> assert Direction.RIGHT == dir.clockwise()
        """
        if self == self.UP:
            return self.RIGHT
        elif self == self.RIGHT:
            return self.DOWN
        elif self == self.DOWN:
            return self.LEFT
        elif self == self.LEFT:
            return self.UP

def next(x: int, y: int, direction: Direction) -> Tuple[int, int]:
    """
    x, y가 주어졌을 때 direction 방향으로 이동할 경우의 좌표를 반환합니다.
    """
    if direction == Direction.UP:
        return (x, y - 1)
    elif direction == Direction.DOWN:
        return (x, y + 1)
    elif direction == Direction.LEFT:
        return (x - 1, y)
    elif direction == Direction.RIGHT:
        return (x + 1, y)

class Snail():
    ns: List[List[int]]
    target_number_position: Tuple[int, int]

    def __init__(self, n: int, target_number: int):
        self.ns = [[0 for _ in range(0, n)] for _ in range(0, n)]

        # 시작점 잡기
        x = y = n // 2

        # current_level은 1, 3, 5, 7, ...와 같은 홀수입니다.
        current_level = 1
        # stack에 방향을 저장합니다.
        stack = []
        for i in range(1, n * n + 1):
            self.ns[y][x] = i
            if i == target_number:
                self.target_number_position = (x, y)

            # 홀수의 제곱을 만나면 현재 단계가 끝난 것입니다.
            # 다음 목표를 설정하고 방향을 무식하게 스택에 때려 박습니다
            # 예:
            #     n = 3일 경우 9면 끝남
            if i == current_level ** 2:
                current_level += 2
                stack += [Direction.UP] * (current_level - 1)
                stack += [Direction.LEFT] * (current_level - 1)
                stack += [Direction.DOWN] * (current_level - 1)
                stack += [Direction.RIGHT] * (current_level - 2)
                stack.append(Direction.UP)
            x, y = next(x, y, stack.pop())
 
    def __str__(self):
        return '\n'.join([' '.join(map(str, line)) for line in self.ns])
    
if __name__ == '__main__':
    n = int(input())
    target_number = int(input())

    if n % 2 == 0:
        raise ValueError('input can not be even number.')

    s = Snail(n, target_number)
    print(s)
    x, y = s.target_number_position
    print(y + 1, x + 1)
