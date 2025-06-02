RAIZ_IDX, ESQ_IDX, DIR_IDX = 0, 1, 2

def pre_ordem(arvore):
    if arvore is None:
        return
    print(arvore[RAIZ_IDX], end=' ')
    pre_ordem(arvore[ESQ_IDX])
    pre_ordem(arvore[DIR_IDX])

arvore = [
    4,              # raíz, nível 0
    [               # ramo da esquerda, nível 1
        2,          # valor filho esquerda
        [1, None, None],   # ramo da esquerda, nível 2
        [3, None, None]    # ramo da direita, nível 2
    ],
    [               # ramo da direita, nível 1
        5,          # valor filho da direita
        None,              # ramo da esquerda, nível 2
        None               # ramo da direita, nível 2
    ]
]

print(pre_ordem(arvore))