def decimal_para_binario(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_para_binario(n // 2) + str(n % 2)