# pyright: reportMissingTypeStubs = false

from __future__ import annotations

_N = 100


def _gen_numbers() -> list[int]:
    """"""
    # The sum of numbers provided by the judge is between 10^2 and 10^11, so we just
    # need a set of numbers that can construct all numbers between 10^2/2 and 10^11/2.
    # Natually, powers of 2 come to mind. We can do 2^0 to 2^29 (2^30 > 10^9 so NG)
    # Unfortunately, these number only add up to at most 2^30-1 (1,073,741,823), so a
    # bunch of large numbers are added to fill the set to make it 100 long
    crude_nums = {2**i for i in range(30)}
    nums: set[int] = {n for n in crude_nums if 1 <= n <= 1_000_000_000}
    n = 1_000_000_000
    while len(nums) < _N:
        nums.add(n)
        n -= 1
    return sorted(nums, reverse=True)


_NUMS = _gen_numbers()
_NUMS_STR = " ".join((str(n) for n in _NUMS))
_NUMS_SUM = sum(_NUMS)


class _JudgeQuitException(Exception):
    """
    Judge has quit. Raise exception so no TLE.
    """


def _read() -> str:
    """
    Read data from judge, and handle incorrect response ending.
    """
    data = input()
    if data == "-1":
        raise _JudgeQuitException()
    return data


def _send(output: str) -> None:
    """
    Send data to judge, which is basically flush printing.
    """
    print(output, flush=True)


def _equal_sum(n: int) -> None:
    """"""
    # This solution assums n = 100
    assert n == _N, f"N should be {_N}"
    # Send the list of prepared numbers
    _send(_NUMS_STR)
    # Judge's numbers
    nums = list(map(int, _read().split()))
    # Calculate the target, which is half of the total sum
    target = (sum(nums) + _NUMS_SUM) // 2
    # Include the numbers returned by the judge. Helpful if the numbers returned are
    # very large
    all_nums = sorted(_NUMS + nums, reverse=True)
    # Try to make the sum
    get_nums: list[str] = []
    for i in all_nums:
        if not target:
            break
        if target < i:
            continue
        target -= i
        get_nums.append(str(i))
    if target:
        raise ValueError(target)
    # Send list of numbers to judge
    _send(" ".join(get_nums))


def _main() -> None:
    t = int(input())
    try:
        for _ in range(t):
            n = int(_read())
            _equal_sum(n)
    except _JudgeQuitException:
        return


if __name__ == "__main__":
    _main()
