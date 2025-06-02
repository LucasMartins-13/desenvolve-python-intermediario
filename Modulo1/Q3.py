def soma(n):
    if n <= 1:
        return 1
    return n + soma(n - 1)