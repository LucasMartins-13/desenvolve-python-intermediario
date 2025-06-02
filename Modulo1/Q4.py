def nn_primo(n, divisor=2):
    if n < 2:
        return False
    if divisor * divisor > n:
        return True
    if n % divisor == 0:
        return False
    return nn_primo(n, divisor + 1)