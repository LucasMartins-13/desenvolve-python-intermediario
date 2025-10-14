import argparse
import sys
from personalizador import layout, painel, progresso, estilo

"""
Main - 

Este script permite imprimir textos ou arquivos no terminal usando 
a biblioteca Rich, com módulos de layout, painel, progresso e estilo.

--------------------------------------------------------------------------------
USO BÁSICO:

python main.py "entrada" [-a] [-m MODULO] [-f FUNCAO]

- entrada (obrigatório): texto direto ou caminho para arquivo
- -a, --arquivo: indica que a entrada é um arquivo
- -m, --modulo: módulo a ser usado (id ou nome)
- -f, --funcao: função do módulo a ser usada (nome ou id)

--------------------------------------------------------------------------------
MÓDULOS DISPONÍVEIS:

1 ou layout     -> personalizador.layout
   - mostrar_panel(texto, isArquivo=False)
   - cabeçalho_rodape(texto, isArquivo=False)

2 ou painel     -> personalizador.painel
   - painel_simples(texto, isArquivo=False)
   - painel_com_titulo(texto, isArquivo=False)

3 ou progresso  -> personalizador.progresso
   - progresso_simples(texto, isArquivo=False)
   - spinner_simples(texto, isArquivo=False)

4 ou estilo     -> personalizador.estilo
   - negrito(texto, isArquivo=False)
   - destaque(texto, isArquivo=False)

--------------------------------------------------------------------------------
EXEMPLOS DE USO NO TERMINAL:

# 1) Texto direto no layout
python main.py "Olá mundo!" -m layout -f mostrar_panel

# 2) Arquivo no layout
python main.py "mensagem.txt" -a -m layout -f mostrar_panel

# 3) Painel simples com texto direto
python main.py "Teste painel" -m painel -f painel_simples

# 4) Painel com título usando arquivo
python main.py "mensagem.txt" -a -m painel -f painel_com_titulo

# 5) Barra de progresso
python main.py "Processando..." -m progresso -f progresso_simples

# 6) Spinner simples
python main.py "Carregando..." -m progresso -f spinner_simples

# 7) Texto em negrito
python main.py "Python é incrível!" -m estilo -f negrito

# 8) Texto com destaque
python main.py "Texto destacado" -m estilo -f destaque

"""

MODULES = {
    "1": ("layout", layout),
    "2": ("painel", painel),
    "3": ("progresso", progresso),
    "4": ("estilo", estilo),
}

def list_options():
    for k, (name, mod) in MODULES.items():
        funcs = [f for f in dir(mod) if not f.startswith("_")]
        print(f"{k} = {name}: funções -> {', '.join(funcs)}")

def main():
    parser = argparse.ArgumentParser(description="Imprime texto formatado com rich (versão simples).")
    parser.add_argument("entrada", help="texto ou caminho para arquivo")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Indica que entrada é arquivo")
    parser.add_argument("-m", "--modulo", help="Módulo (id ou nome). Use -h para ver opções")
    parser.add_argument("-f", "--funcao", help="Função (nome ou id). Use -h para ver opções")
    args = parser.parse_args()
    
    if args.modulo is None:
        print("Módulo não informado. Opções:")
        list_options()
        sys.exit(1)

    mod = None
    for k, (name, module) in MODULES.items():
        if args.modulo == k or args.modulo == name:
            mod = module
            break

    if mod is None:
        print("Módulo inválido")
        list_options()
        sys.exit(1)

    funcs = [f for f in dir(mod) if not f.startswith("_")]
    if not funcs:
        print("Nenhuma função pública disponível neste módulo.")
        sys.exit(1)

    func_name = None
    if args.funcao is None:
        func_name = funcs[0]
    else:
        if args.funcao.isdigit():
            idx = int(args.funcao) - 1
            if 0 <= idx < len(funcs):
                func_name = funcs[idx]
        else:
            if args.funcao in funcs:
                func_name = args.funcao

    if func_name is None:
        print("Função inválida. Opções:")
        for i, f in enumerate(funcs, start=1):
            print(i, f)
        sys.exit(2)

    func = getattr(mod, func_name)
    func(args.entrada, args.arquivo)

if __name__ == "__main__":
    main()
