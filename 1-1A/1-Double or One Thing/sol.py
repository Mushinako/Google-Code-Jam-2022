from __future__ import annotations


def _double_or_one_thing(s: str) -> str:
    """"""
    # Keep track of indices that should be duplicated
    dup_indices: set[int] = set()
    # Keep track of indices of repeating letters
    reps: set[int] = set()
    for i, c in enumerate(s[:-1]):
        # Compare current and next char
        next_c = s[i + 1]
        # If next char is smaller, don't repeat
        if c > next_c:
            reps = set()
            continue
        # If current char is smaller, repeat
        if c < next_c:
            dup_indices |= reps
            dup_indices.add(i)
            reps = set()
            continue
        # If the chars are the same, keep track of it
        reps.add(i)
    # Construct the string
    cs: list[str] = []
    for i, c in enumerate(s):
        cs.append(c)
        if i in dup_indices:
            cs.append(c)
    return "".join(cs)


def _main() -> None:
    t = int(input())
    for i in range(1, t + 1):
        s = input()
        string = _double_or_one_thing(s)
        print(f"Case #{i}: {string}")


if __name__ == "__main__":
    _main()
