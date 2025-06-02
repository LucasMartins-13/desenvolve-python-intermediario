def intervalo_invertido(a, b):
    if a > b:
        print("invalido")
    else:
        if a < b:
            intervalo_invertido(a + 1, b)
        print(a, end=' ')