from module_a import plus_one


def plus_two(x: int) -> int:
    return plus_one(plus_one(x))
