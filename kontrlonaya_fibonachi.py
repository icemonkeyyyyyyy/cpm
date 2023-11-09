def fib_rec(n: int):
    if n <= 1:
        return n
    else:
        return fib_rec(n - 1) + fib_rec(n - 2)


def fib_dyn(n: int):
    numbers = [0, 1]
    for i in range(2, n + 1):
        numbers.append(numbers[i - 1] + numbers[i - 2])
    return numbers[n]


n_dyn = 10
n_rec = 5

print(
    f"Recursive: {fib_rec(n_rec)}\n"
    f"Dynamic: {fib_dyn(n_dyn)}"
)
