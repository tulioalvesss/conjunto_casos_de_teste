# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colab.


"""

# RF01 - Validador de CPF
def validar_cpf(cpf):
    if len(cpf) != 11 or not cpf.isdigit():
        return False
    soma = 0
    peso = 10
    for i in range(9):
        soma += int(cpf[i]) * peso
        peso -= 1
    resto = soma % 11
    if resto < 2:
        digito1 = 0
    else:
        digito1 = 11 - resto
    if int(cpf[9]) != digito1:
        return False
    soma = 0
    peso = 11
    for i in range(10):
        soma += int(cpf[i]) * peso
        peso -= 1
    resto = soma % 11
    if resto < 2:
        digito2 = 0
    else:
        digito2 = 11 - resto
    if int(cpf[10]) != digito2:
        return False
    return True

# Teste RF01
print("RF01 - Validador de CPF:")
testes_cpf = [("12345678900", True), ("11111111111", False), ("99999999999", False)]
for entrada, saida_esperada in testes_cpf:
    resultado = validar_cpf(entrada)
    print(f"Entrada: {entrada}, Saída esperada: {saida_esperada}, Saída: {resultado}")
print()

# RF02 - Validador de Cartão de Crédito e Autorização de Compra
def validar_cartao(numero, nome, validade, cvv):
    if len(numero) != 16 or not numero.isdigit():
        return ("Inválido", "Compra negada")
    return ("Válido", "Compra autorizada")

# Teste RF02
print("RF02 - Validador de Cartão de Crédito e Autorização de Compra:")
testes_cartao = [("1234567890123456", "João da Silva", "12/25", "123"),
                 ("9876543210987654", "Maria Oliveira", "09/23", "789"),
                 ("4444333322221111", "Pedro Souza", "03/28", "321")]
for numero, nome, validade, cvv in testes_cartao:
    resultado = validar_cartao(numero, nome, validade, cvv)
    print(f"Número do Cartão: {numero}, Nome do Titular: {nome}, Validade: {validade}, CVV: {cvv}, Saída esperada: {resultado}")
print()

# RF03 - Conversor de Moedas
def converter_moeda(valor_em_reais):
    valor_em_dolares = valor_em_reais / 5.5  # Considerando uma taxa de câmbio fictícia
    return round(valor_em_dolares, 2)

# Teste RF03
print("RF03 - Conversor de Moedas:")
testes_moeda = [(100.00, 18.18), (500.00, 90.91), (1000.00, 181.82)]
for valor_em_reais, saida_esperada in testes_moeda:
    resultado = converter_moeda(valor_em_reais)
    print(f"Valor em R$: {valor_em_reais}, Saída esperada em $: {saida_esperada}, Saída: {resultado}")
print()

# RF04 - Operação lógica AND
def operacao_and(a, b):
    return a and b

# Teste RF04
print("RF04 - Operação lógica AND:")
testes_and = [(1, 1, 1), (1, 0, 0), (0, 0, 0)]
for entrada_a, entrada_b, saida_esperada in testes_and:
    resultado = operacao_and(entrada_a, entrada_b)
    print(f"Entrada: {entrada_a}, {entrada_b}, Saída esperada: {saida_esperada}, Saída: {resultado}")
print()

# RF05 - Validador de Placas de Veículos
def validar_placa(placa):
    if len(placa) == 7 and placa.isalnum():
        return "Válido"
    else:
        return "Inválido"

# Teste RF05
print("RF05 - Validador de Placas de Veículos:")
testes_placa = [("ABC1234", "Válido"), ("XYZ9876", "Válido"), ("1234567", "Inválido")]
for entrada, saida_esperada in testes_placa:
    resultado = validar_placa(entrada)
    print(f"Entrada: {entrada}, Saída esperada: {saida_esperada}, Saída: {resultado}")
print()
