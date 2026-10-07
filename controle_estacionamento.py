# Sistema de Controle de Estacionamento
# Trabalho Final A1 - Programação de Computadores

import math

# Capacidade máxima do estacionamento
CAPACIDADE_MAXIMA = 10

# Lista pra guardar os veículos estacionados
veiculos = []

# ===============================
# FUNÇÕES DE VALIDAÇÃO E CÁLCULO
# ===============================

def validar_placa(placa):
    """Verifica se a placa esta no formato AAA-1234."""
    placa = placa.upper().strip()
    if len(placa) != 8:
        return False
    if placa[3] != "-":
        return False
    letras = placa[:3]
    numeros = placa[4:]
    if not letras.isalpha():
        return False
    if not numeros.isdigit():
        return False
    return True


def validar_horario(horario):
    """Verifica se o horario esta no formato HH:MM e se os valores sao validos.

    Retorna True se o formato for HH:MM, hora entre 00 e 23,
    e minuto entre 00 e 59. Retorna False caso contrario.
    """
    horario = horario.strip()
    if len(horario) != 5:
        return False
    if horario[2] != ":":
        return False
    hora = horario[:2]
    minuto = horario[3:]
    if not hora.isdigit() or not minuto.isdigit():
        return False
    if int(hora) > 23:
        return False
    if int(minuto) > 59:
        return False
    return True


def calcular_valor(minutos):
    """Calcula o valor a pagar com base no tempo de permanencia em minutos.

    Primeira hora (ate 60 min): R$ 5,00.
    Cada 15 minutos adicionais ou fracao: R$ 2,00.
    """
    if minutos <= 60:
        return 5.00
    blocos = math.ceil((minutos - 60) / 15)
    return 5.00 + (blocos * 2.00)

# ======================================================
#  FUNÇÃO DE LOCALIZAÇÃO DE VAGAS
# ======================================================

def localizar_vaga(veiculos):
    """Retorna o numero da primeira vaga livre disponivel.

    Percorre de 1 ate CAPACIDADE_MAXIMA e devolve o primeiro
    numero que nao esteja ocupado por nenhum veiculo na lista.
    """
    vagas_ocupadas = {v["vaga"] for v in veiculos}
    for numero in range(1, CAPACIDADE_MAXIMA + 1):
        if numero not in vagas_ocupadas:
            return numero
    return None


# ==========================
# FUNÇÕES PRINCIPAIS
# ==========================

def cadastrar_veiculo(veiculos):
    """Registra um novo veiculo no estacionamento.

    Solicita placa, horario de entrada e tipo do veiculo.
    Valida cada dado antes de inserir. Nao altera a lista
    se qualquer validacao falhar.
    """
    if len(veiculos) >= CAPACIDADE_MAXIMA:
        print("Estacionamento lotado. Nao foi possivel cadastrar.")
        return

    placa = input("Placa (formato ABC-1234): ").strip().upper()
    if not validar_placa(placa):
        print("Placa invalida. Use o formato ABC-1234.")
        return

    for v in veiculos:
        if v["placa"] == placa:
            print("Essa placa ja esta cadastrada no estacionamento.")
            return

    horario = input("Horario de entrada (HH:MM): ").strip()
    if not validar_horario(horario):
        print("Horario invalido. Use o formato HH:MM (exemplo 08:30).")
        return

    tipo = input("Tipo do veiculo (carro / moto): ").strip().lower()
    if tipo not in ("carro", "moto"):
        tipo = "carro"

    vaga = localizar_vaga(veiculos)
    veiculos.append({"placa": placa, "entrada": horario, "vaga": vaga, "tipo": tipo})
    print(f"Veiculo {placa} cadastrado na vaga {vaga}.")


def remover_veiculo(veiculos):
    """Remove um veiculo do estacionamento e calcula o valor a pagar."""
    
    placa = input("Placa do veiculo que esta saindo: ").strip().upper()
    
    veiculo = next((v for v in veiculos if v["placa"] == placa), None)

    if veiculo is None:
        print("Placa nao encontrada no estacionamento.")
        return

    horario_saida = input("Horario de saida (HH:MM): ").strip()
    if not validar_horario(horario_saida):
        print("Horario invalido. Use o formato HH:MM (exemplo 08:30).")
        return

    h1, m1 = map(int, veiculo["entrada"].split(":"))
    h2, m2 = map(int, horario_saida.split(":"))
    minutos = (h2 * 60 + m2) - (h1 * 60 + m1)

    if minutos < 0:
        print("O horario de saida nao pode ser anterior ao de entrada.")
        return

    valor = calcular_valor(minutos)
    print(f"\nPlaca: {placa} | Entrada: {veiculo['entrada']} | Saida: {horario_saida}")
    print(f"Permanencia: {minutos} min | Total a pagar: R$ {valor:.2f}")
    print(f"Vaga {veiculo['vaga']} liberada.")
    veiculos.remove(veiculo)

def listar_veiculos(veiculos):
    """Lista todos os veiculos estacionados no momento.

    Exibe placa, vaga, tipo e horario de entrada de cada veiculo.
    Caso nao haja veiculos, informa que o estacionamento esta vazio.
    """
    if len(veiculos) == 0:
        print("Nenhum veiculo estacionado no momento.")
        return

    print("\n========================================")
    print(f"{'VAGA':<6} {'PLACA':<10} {'TIPO':<6} {'ENTRADA'}")
    print("========================================")
    for v in veiculos:
        print(f"{v['vaga']:<6} {v['placa']:<10} {v['tipo']:<6} {v['entrada']}")
    print("========================================")
    print(f"Total: {len(veiculos)} veiculo(s) estacionado(s).")


def consultar_vagas(veiculos):
    """Exibe quantas vagas estao livres e quais estao ocupadas."""
    livres = CAPACIDADE_MAXIMA - len(veiculos)
    print(f"\nVagas disponiveis: {livres}/{CAPACIDADE_MAXIMA}")

# ==========================
# TESTES AUTOMÁTICOS
# ==========================


def testes():
    """
    Testa funções principais do programa.
    """

    assert validar_placa("ABC-1234")
    assert not validar_placa("ABC1234")


    assert validar_horario("08:30")
    assert not validar_horario("30:90")


    assert calcular_valor(30) == 5
    assert calcular_valor(75) == 7
    assert calcular_valor(120) == 13


    print("Todos os testes passaram!")

# ==========================
# MENU
# ==========================

def main():
    """Controla o menu principal do sistema de estacionamento."""
    while True:
        print("\n========================================")
        print("         ESTACIONAMENTO - MENU          ")
        print("========================================")
        print("1 - Entrada de veiculo")
        print("2 - Saida de veiculo")
        print("3 - Listar veiculos estacionados")
        print("4 - Consultar vagas")
        print("0 - Encerrar")
        print("========================================")

        opcao = input("Escolha uma opcao: ").strip()

        if opcao == "1":
            cadastrar_veiculo(veiculos)
            
        elif opcao == "2":
            remover_veiculo(veiculos)
            
        elif opcao == "3":
            listar_veiculos(veiculos)
            
        elif opcao == "4":
            consultar_vagas(veiculos)
            
        elif opcao == "0":
            print("Sistema encerrado. Ate logo!")
            break
        
        else:
            print("Opcao invalida. Escolha um numero do menu.")

if __name__ == "__main__":
    
    # Para testar:
    testes() 
    
    main()