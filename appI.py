from colorama import init, Fore, Style

# Inicializa o Colorama
init(autoreset=True)

# Lista com os níveis e situações do reservatório
niveis_reservatorio = [
    "Nível 1 - Muito baixo (crítico)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (alerta)"
]

def definir_cor(nivel):
    """Retorna a cor correspondente ao nível do reservatório."""
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

def exibir_status(nivel):
    """Exibe a situação do reservatório com a cor apropriada."""
    if 1 <= nivel <= 5:
        cor = definir_cor(nivel)
        mensagem = niveis_reservatorio[nivel - 1]
        print(cor + mensagem + Style.RESET_ALL)
    else:
        print(Fore.WHITE + "Nível inválido! Digite um valor entre 1 e 5." + Style.RESET_ALL)

# Solicita ao usuário o nível atual do reservatório
try:
    nivel_atual = int(input("Digite o nível atual do reservatório (1 a 5): "))
    exibir_status(nivel_atual)
except ValueError:
    print(Fore.WHITE + "Por favor, digite um número inteiro válido." + Style.RESET_ALL)
