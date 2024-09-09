"""
Function to add fractions and subtract fractions
"""
from math import gcd

def add_and_sub_fractions(expression: str) -> str:
    """
    Function to add fractions and subtract fractions
    """
    x, y = 0, 6 * 7 * 8 * 9 * 10
    if expression[0].isdigit():
        expression = '+' + expression
    i, n = 0, len(expression)
    while i < n:
        sign = -1 if expression[i] == '-' else 1
        i += 1
        j = i
        while j < n and expression[j] not in '+-':
            j += 1
        s = expression[i:j]
        a, b = s.split('/')
        x += sign * int(a) * y // int(b)
        i = j
    z = gcd(x, y)
    x //= z
    y //= z
    return f'{x}/{y}'

# Time complexity: O(n)
# Space complexity: O(1)
# n = len(expression)

# Test the function
TEST_EXPRESSION = "-1/2+1/2"
print(f'The expression is: {TEST_EXPRESSION}')
print(f'The result is: {add_and_sub_fractions(TEST_EXPRESSION)}')  # Output: "0/1"
print(f'The subtraction is: {add_and_sub_fractions("-1/2-1/2")}')  # Output: "-1/1"
