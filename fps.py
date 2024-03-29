import numpy as np

base = float(input("Digite a base: "))
t = int(input("Digite a quantidade de dígitos da mantissa: "))
menor, maior = input("Digite o menor e o maior expoente separados por espaço: ").split()
menor = int(menor)
maior = int(maior)

print("Valores inseridos:")
print("Base:", base)
print("Quantidade de dígitos da mantissa:", t)
print("Menor expoente:", menor)
print("Maior expoente:", maior)

num_menor = 0.0

# ZERO
zero_mantissa = "0." + "0" * (t - 1) 
zero = float(zero_mantissa) * np.power(base, menor)

# Menor Positivo Não Nulo
mantissa_menor = "0.1" + "0" * t
menor_positivo = float(mantissa_menor) * np.power(base, menor)

# Maior Positivo Não Nulo
mantissa_maior = "0." + "9" * t
maior_positivo = float("0." + "9" * t) * np.power(base, maior)

num_max_mantissas = (base - 1) * np.power(base, t - 1)
num_max_exp = maior - menor + 1
num_elem_posit = num_max_mantissas * num_max_exp
num_total_elementos = 2*(num_elem_posit) + 1

print("ZERO:", zero)
print("Menor Positivo Não Nulo:", menor_positivo)
print("Maior Positivo Não Nulo:", maior_positivo)
print("Número máximo de mantissas:", num_max_mantissas)
print("Número máximo de expoentes:", num_max_exp)
print("Número de elementos positivos:", num_elem_posit)
print("Número total de elementos:", num_total_elementos)
