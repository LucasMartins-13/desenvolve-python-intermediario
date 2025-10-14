from rich.console import Console
from rich.panel import Panel

console = Console()

"""
Módulo layout - 

Este módulo contém funções para exibir textos usando layouts básicos do Rich,
como painéis e cabeçalhos/rodapés.

Funções:
- mostrar_panel(texto, isArquivo=False): exibe o texto dentro de um painel.
- cabeçalho_rodape(texto, isArquivo=False): exibe um cabeçalho, o texto e um rodapé.

Exemplos de uso no terminal:

# Exibir um texto direto em painel
python main.py "Olá mundo!" -m layout -f mostrar_panel

# Exibir um arquivo dentro de painel
python main.py "mensagem.txt" -a -m layout -f mostrar_panel

# Exibir cabeçalho e rodapé
python main.py "Teste" -m layout -f cabeçalho_rodape
"""

def mostrar_panel(texto: str, isArquivo: bool = False) -> None:
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    console.print(Panel(texto, title="Layout: Panel"))

def cabeçalho_rodape(texto: str, isArquivo: bool = False) -> None:
    if isArquivo:
        with open(texto, "r", encoding="utf-8") as f:
            texto = f.read()
    console.print("=== CABEÇALHO ===")
    console.print(texto)
    console.print("=== RODAPÉ ===")