from __future__ import annotations

_NEED = int(1e6)


class _NoSolutionException(Exception):
    pass


def _3d_printing(cmyks: list[list[int]]) -> list[int]:
    """"""
    mins = [min(inks) for inks in zip(*cmyks)]
    if sum(mins) < _NEED:
        raise _NoSolutionException()
    left = _NEED
    solution: list[int] = []
    for min_ in mins:
        take = min(min_, left)
        left -= take
        solution.append(take)
    return solution


def _main() -> None:
    t = int(input())
    for i in range(1, t + 1):
        cmyks: list[list[int]] = [list(map(int, input().split())) for _ in range(3)]
        try:
            inks = _3d_printing(cmyks)
        except _NoSolutionException:
            print(f"Case #{i}: IMPOSSIBLE")
            continue
        print(f'Case #{i}: {" ".join(map(str,inks))}')


if __name__ == "__main__":
    _main()
