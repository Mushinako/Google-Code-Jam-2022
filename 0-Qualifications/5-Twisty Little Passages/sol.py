# pyright: reportMissingTypeStubs = false

from __future__ import annotations

from random import randint
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Generator

_MAX_QUERY_COUNT = 1000


class _JudgeQuitException(Exception):
    pass


def _read() -> str:
    data = input()
    if data == "-1":
        raise _JudgeQuitException()
    return data


def _send(output: str) -> None:
    print(output, flush=True)


def _get_rooms(n: int, k: int, starting_room: int) -> Generator[int, None, None]:
    """"""
    visited_rooms: set[int] = {starting_room}
    for _ in range(min(n, k - 1, _MAX_QUERY_COUNT)):
        while True:
            room = randint(1, n)
            if room not in visited_rooms:
                visited_rooms.add(room)
                break
        yield room


def _get_passage_counts(n: int, k: int) -> tuple[int, int]:
    """"""
    room, passage_count = map(int, _read().split())
    sum_: int = passage_count
    len_: int = 1
    for r in _get_rooms(n, k, room):
        _send(f"T {r}")
        sum_ += int(_read().split()[1])
        len_ += 1
    return sum_, len_


def _twisty_little_passages(n: int, k: int) -> None:
    """"""
    sum_, len_ = _get_passage_counts(n, k)
    total_count = round(sum_ * n / 2 / len_)
    _send(f"E {total_count}")


def _main() -> None:
    t = int(input())
    try:
        for _ in range(t):
            n, k = map(int, _read().split())
            _twisty_little_passages(n, k)
    except _JudgeQuitException:
        return


if __name__ == "__main__":
    _main()
