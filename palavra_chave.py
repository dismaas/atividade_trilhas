nome = "Cecilia"
idade = 17
altura = 1.55
estudante = True

print(f"Olá, meu nome é {nome}, tenho {idade} anos de idade.")

a = 5
b = 7

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
divisao_inteira = a // b
resto = a % b
potencia = a ** b

print(f"Divisão formatada: {divisao:.2f}")

idade_usuario = 17

if idade_usuario >= 18:
    print("Maior de idade.")
elif idade_usuario >= 16:
    print("Votante facultativo.")
else:
    print("Menor de idade.")

x = 5
if x > 4 and x < 10:
    print("O número está no intervalo entre 4 e 10.")

contador = 0
while contador < 4:
    print(f"Rodando While: {contador}")
    contador += 1

for i in range(5):
    print(f"Rodando For número: {i}")

numeros = [1, 2, 3, 4, 5, 6]

print(f"Primeiro elemento: {numeros[0]}")
print(f"Último elemento: {numeros[-1]}")

print(f"Do índice 1 ao 3: {numeros[1:4]}")

numeros.append(7)
numeros.insert(2, 99)
numeros.remove(99)
ultimo = numeros.pop()

print(f"Tamanho da lista: {len(numeros)}")
print(f"Soma dos elementos: {sum(numeros)}")
print(f"Valor mínimo: {min(numeros)}")
print(f"Valor máximo: {max(numeros)}")

for indice, valor in enumerate(numeros):
    print(f"Índice {indice} contém o valor {valor}")
