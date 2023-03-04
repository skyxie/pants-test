from module_a.dpfs import plus_one


def plus_y(x: int, y: int) -> int:
    if y == 0:
        return x
    return plus_y(plus_one(x), y - 1)
