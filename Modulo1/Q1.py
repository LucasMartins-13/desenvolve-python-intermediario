def intervalo(a, b):
    if a > b:
        print("invalido")
    else:
        print(a, end=' ')
        if a < b:
            intervalo(a + 1, b)