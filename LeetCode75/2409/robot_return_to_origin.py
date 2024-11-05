"""Method to determine if a robot returns to the origin after a series of moves."""

def judge_circle(moves: str) -> bool:
    """Return True if the robot returns to the origin after a series of moves."""
    x, y = 0, 0
    for move in moves:
        if move == "U":
            y += 1
        elif move == "D":
            y -= 1
        elif move == "L":
            x -= 1
        elif move == "R":
            x += 1
    return x == 0 and y == 0
