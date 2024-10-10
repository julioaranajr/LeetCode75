def fibonacci(n: int) -> int:
    """A function to find the nth Fibonacci number.

    Args:
        n (int): An integer.

    Returns:
        int: The nth Fibonacci number.
    """
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b
