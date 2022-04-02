from __future__ import annotations


def _d1000000(dices: list[int]) -> int:
    """"""
    rev_sorted_dices = sorted(dices, reverse=True)
    while True:
        for i, d in zip(range(len(rev_sorted_dices), 0, -1), rev_sorted_dices):
            if i > d:
                break
        else:
            break
        rev_sorted_dices.pop()
    return len(rev_sorted_dices)


def _main() -> None:
    t = int(input())
    for i in range(1, t + 1):
        # `N` not needed
        int(input())
        dices = list(map(int, input().split()))
        length = _d1000000(dices)
        print(f"Case #{i}: {length}")


if __name__ == "__main__":
    _main()
