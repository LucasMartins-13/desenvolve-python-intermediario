from rich.console import Console
from rich.panel import Panel

console = Console()

"""
Módulo painel - 

Este módulo contém funções para exibir textos dentro de painéis
do Rich, com ou sem título.

Funções:
- painel_simples(texto, isArquivo=False): exibe texto dentro de um painel simples.
- painel_com_titulo(texto, isArquivo=False): exibe texto dentro de um painel com título.

Exemplos de uso no terminal:

# Painel simples com texto direto
python main.py "Olá!" -m painel -f painel_simples

# Painel simples com arquivo
python main.py "mensagem.txt" -a -m painel -f painel_simples

# Painel com título
python main.py "mensagem.txt" -a -m painel -f painel_com_titulo
"""

def painel(texto: str, isArquivo: bool = False) -> None:
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    console.print(Panel(texto))

def painel_com_titulo(texto: str, isArquivo: bool = False) -> None:
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    console.print(Panel(texto, title="Título"))