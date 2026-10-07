# Sistema de Controle de Estacionamento

## Trabalho Final A1 - Programação de Computadores

## Integrantes

- Giovanna Gouveia Baroni RGM: 47327901
- Lais Lot da Silva RGM: 47650885
- Thaiane Cristine Antunes RGM: 47070609


## Descrição do projeto

Este projeto consiste em um Sistema de Controle de Estacionamento desenvolvido em Python.

O sistema permite controlar a entrada e saída de veículos, consultar vagas disponíveis, listar veículos estacionados e calcular o valor a pagar de acordo com o tempo de permanência.


## Como executar

Requisitos:
- Python 3 instalado

Para executar o programa:

1. Abra o terminal na pasta do projeto.
2. Execute:

controle_estacionamento.py

O programa será iniciado com um menu interativo.


## Funcionalidades implementadas

O sistema possui as seguintes opções:

1 - Entrada de veículo

Permite cadastrar um novo veículo informando:

- Placa
- Horário de entrada
- Tipo do veículo

2 - Saída de veículo

Permite remover um veículo cadastrado.

O sistema:

- Localiza a placa
- Calcula o tempo de permanência
- Calcula o valor a pagar
- Libera a vaga

3 - Listar veículos estacionados

Exibe todos os veículos atualmente estacionados contendo:

- Número da vaga
- Placa
- Tipo
- Horário de entrada

4 - Consultar vagas

Mostra a quantidade de vagas livres no estacionamento.

0 - Encerrar

Finaliza o programa.


## Funções implementadas

- validar_placa()
  
  Verifica se a placa está no formato AAA-1234.


- validar_horario()

  Verifica se o horário está no formato HH:MM e se é válido.


- calcular_valor()

  Calcula o valor da permanência conforme a tabela de preços.


- cadastrar_veiculo()

  Realiza o cadastro de um novo veículo.


- remover_veiculo()

  Realiza a saída do veículo e cálculo do pagamento.


- listar_veiculos()

  Mostra os veículos cadastrados.


- consultar_vagas()

  Exibe as vagas disponíveis.


- main()

  Controla o menu principal do sistema.


## Decisões de projeto

- A capacidade máxima do estacionamento foi definida como 10 vagas.

- Os dados são armazenados apenas em memória utilizando lista de dicionários.

- Quando o programa é encerrado, os dados são perdidos.

- Caso o usuário informe um tipo de veículo diferente de "carro" ou "moto", o sistema registra como carro.

- O programa não utiliza bibliotecas externas, banco de dados ou arquivos.


## Estrutura dos dados

Cada veículo é armazenado como um dicionário:

{
    "placa": "ABC-1234",
    "entrada": "08:30",
    "vaga": 1,
    "tipo": "carro"
}


## Sistema de cobrança

Primeira hora:

R$ 5,00

Cada 15 minutos adicionais:

R$ 2,00