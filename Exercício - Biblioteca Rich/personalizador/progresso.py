from rich.console import Console
from rich.progress import track
from time import sleep

console = Console()

"""
Módulo progresso - 

Este módulo contém funções que demonstram barras de progresso e spinners
usando Rich.

Funções:
- progresso_simples(texto, isArquivo=False): mostra barra de progresso simulada.
- spinner_simples(texto, isArquivo=False): mostra spinner simples com mensagem.

Exemplos de uso no terminal:

# Barra de progresso
python main.py "Processando..." -m progresso -f progresso_simples

# Spinner simples
python main.py "Carregando..." -m progresso -f spinner_simples
"""

def progresso(texto: str, isArquivo: bool = False) -> None:
    steps = 10

    for _ in track(range(steps), description="Processando..."):
        sleep(0.05)
    console.print("Concluído")

def spinner(texto: str, isArquivo: bool = False) -> None:
    console.print("[bold]Carregando...[/]")
    sleep(0.3)
    console.print("Pronto")