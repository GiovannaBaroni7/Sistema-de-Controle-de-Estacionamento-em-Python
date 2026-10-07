# Casos de Teste

## Caso 1 - Cadastro bem sucedido

### Entrada

Opção escolhida:

1 - Entrada de veiculo

Dados informados:

Placa:
ABC-1234

Horário:
08:30

Tipo:
carro


### Saída esperada

Veiculo ABC-1234 cadastrado na vaga 1.


==========================

## Caso 2 - Placa inválida

### Entrada

Opção escolhida:

1 - Entrada de veiculo

Dados informados:

Placa:
ABC1234


### Saída esperada

Placa invalida. Use o formato ABC-1234.


### Resultado esperado

A lista de veículos permanece igual.


==========================

## Caso 3 - Placa duplicada

### Entrada

Primeiro cadastro:

Placa:
ABC-1234


Segundo cadastro:

Placa:
ABC-1234


### Saída esperada

Essa placa ja esta cadastrada no estacionamento.


### Resultado esperado

O veículo não é cadastrado novamente.


==========================

## Caso 4 - Cálculo de valor

### Entrada

Horário de entrada:

08:30


Horário de saída:

09:45


Tempo:

75 minutos


### Saída esperada

Permanencia: 75 min

Total a pagar: R$ 7,00


==========================

## Caso 5 - Saída com placa inexistente

### Entrada

Opção escolhida:

2 - Saida de veiculo


Placa:

XYZ-9999


### Saída esperada

Placa nao encontrada no estacionamento.


==========================

## Caso 6 - Estacionamento lotado

### Entrada

Cadastrar 10 veículos.


Tentativa de cadastrar o 11º veículo.


### Saída esperada

Estacionamento lotado. Nao foi possivel cadastrar.


==========================

## Caso 7 - Horário inválido

### Entrada

Horário:

25:90


### Saída esperada

Horario invalido. Use o formato HH:MM.