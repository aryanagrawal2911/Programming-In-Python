# Evaluate the expression :


def evaluate(x, y, z):
    a = eval("(x < y) or (not (z == y) and (z < x))")
    return a


print(evaluate(x = 0, y = 6, z = 10), "\n", evaluate(x = 1, y = 1, z = 1))
