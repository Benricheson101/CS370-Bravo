def wrapping_add(a: int, b: int, limit: int) -> int:
    return (a + b) % limit if (a + b) > 0 else limit - (abs(a + b) % limit) - 1


def clamped_add(a: int, b: int, limit: int) -> int:
    return max(0, min(limit, a + b))
