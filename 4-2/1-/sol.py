from __future__ import annotations


def _spiraling_into_control(n: int, k: int) -> list[tuple[int, int]]:
    """"""
    if k >= n * n - 1:
        return []
    diff = k - n + 1
    if k < n - 1:
        return []
    if diff % 2:
        return []
    div = n - 1
    inner_remain = k - 4 * div
    if inner_remain > 0:
        inner_rows = _spiraling_into_control(n - 2, inner_remain)
        return [(start + 4 * n, end + 4 * n) for start, end in inner_rows]
    q, r = divmod(diff, div)
    r //= 2
    break_off_point = div // 2 + 1 + div * q + r
    # Go inwards
    if n == 3:
        return [(break_off_point, 9)]
    print(f"k={k}, inner_remain={inner_remain}, break_off_point={break_off_point}")
    inner_div = n - 3
    inner_start = inner_div // 2 + 1 + inner_div * q + r
    inner_dividend = inner_start - 1 - inner_div // 2
    inner_q, inner_r = divmod(inner_dividend, inner_div)
    if inner_r >= inner_div // 2:
        inner_q += 1
        inner_r = 0
    pass
    rows: list[tuple[int, int]] = [(break_off_point, inner_start + 4 * div)]
    return rows


def _main() -> None:
    t = int(input())
    for i in range(1, t + 1):
        n, k = map(int, input().split())
        rows = _spiraling_into_control(n, k)
        if rows:
            print(f"Case #{i}: {len(rows)}")
            for start, end in rows:
                print(f"{start} {end}")
        else:
            print(f"Case #{i}: IMPOSSIBLE")


if __name__ == "__main__":
    _main()
