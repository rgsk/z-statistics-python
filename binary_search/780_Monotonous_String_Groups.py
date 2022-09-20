# nodemon --watch 780_Monotonous_String_Groups.py -e py --exec "mypy 780_Monotonous_String_Groups.py && python 780_Monotonous_String_Groups.py"

from enum import Enum


class OpType(Enum):
    increasing = 1
    descreasing = 2


def get_max(s: str, i: int, type: OpType):
    j = i + 1
    n = len(s)
    while j < n:
        if (type == OpType.increasing and s[j] >= s[j-1]) or (type == OpType.descreasing and s[j] <= s[j-1]):
            j += 1
        else:
            return j
    return j


def solve1(s: str):
    i = 0
    n = len(s)
    c = 0
    while i < n:
        i = max(get_max(s, i, OpType.increasing),
                get_max(s, i, OpType.descreasing))
        c += 1
    return c


def solve2(s: str):
    if not s:
        return 0

    n = len(s)
    c = 1
    increasing = None

    for i in range(1, n):
        if s[i-1] != s[i]:
            v = s[i] > s[i-1]
            if v != increasing:
                if increasing is not None:
                    c += 1
                    increasing = None
                else:
                    increasing = v
    return c


def test1():
    s = "abcdcba"
    print(solve2(s))


def test2():
    s = "dcda"
    print(solve2(s))


test1()
test2()
