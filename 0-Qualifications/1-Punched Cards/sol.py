from __future__ import annotations


def _punched_cards(r: int, c: int) -> list[str]:
    """"""
    rows: list[str] = []
    rows.append("." * 2 + "+-" * (c - 1) + "+")
    rows.append("." * 2 + "|." * (c - 1) + "|")
    for _ in range(r - 1):
        rows.append("+-" * c + "+")
        rows.append("|." * c + "|")
    rows.append("+-" * c + "+")
    return rows


def _main() -> None:
    t = int(input())
    for i in range(1, t + 1):
        r, c = map(int, input().split())
        rows = _punched_cards(r, c)
        print(f"Case #{i}:")
        for row in rows:
            print(row)


if __name__ == "__main__":
    _main()
