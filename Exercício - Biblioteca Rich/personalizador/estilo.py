from rich.console import Console

console = Console()

"""
Módulo estilo - 

Este módulo contém funções para aplicar estilos simples no texto,
como negrito e destaque colorido.

Funções:
- negrito(texto, isArquivo=False): imprime texto em negrito.
- destaque(texto, isArquivo=False): imprime texto com destaque em cor.

Exemplos de uso no terminal:

# Texto em negrito
python main.py "Python é incrível!" -m estilo -f negrito

# Texto com destaque
python main.py "Texto destacado" -m estilo -f destaque
"""

def negrito(texto: str, isArquivo: bool = False) -> None:
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    console.print(f"[bold]{texto}[/bold]")

def destaque(texto: str, isArquivo: bool = False) -> None:
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    console.print(f"[green]{texto}[/green]")
