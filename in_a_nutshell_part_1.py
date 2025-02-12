# Números
x = 10          # Inteiro
y = 3.14        # Float
z = 1 + 2j      # Complexo
print(x + y)    # Soma: 13.14

# Variáveis
nome = "Alice"   # String
idade = 25       # Inteiro
altura = 1.70    # Float

# Texto
texto = "Olá, mundo!"
print(texto.upper())  # OLÁ, MUNDO!

# Booleanos
a = True
b = False
print(a and b)  # False

# Listas
lista = [1, 2, 3, "quatro", True]
print(lista[3])  # "quatro"
lista.append(5)  # Adiciona 5 à lista

# Tuplas
tupla = (1, 2, 3)
print(tupla[1])  # 2

# Dicionários
dicionario = {"nome": "Alice", "idade": 25}
print(dicionario["nome"])  # Alice
dicionario["altura"] = 1.70

# Loop for
for num in [1, 2, 3]:
    print(num)  # 1, depois 2, depois 3

# Loop while
x = 0
while x < 5:
    print(x)  # 0 a 4
    x += 1

# Python do Zero ao Junior
print("oi")
print(10/5)

# Variáveis armazenam dados
ingressos = 50
compradores = 250
tem_ingresso_suficiente = (ingressos >= compradores)

# Entrada de dados
nome = input("Fala seu nome: ")
nome = int(input("Digite um número: "))

# Condições
salario = float(input("Informe o salário: "))
if salario <= 3000:
    print("Junior")
elif salario <= 6000:  # Exemplo de outra condição
    print("Pleno")
else:
    print("Sênior")

# Listas
listas = [1, 2, 3, 4]
listas.append(5)  # Adiciona 5 à lista

# Laço com range
notas = []
for x in range(5):
    notas.append(float(input(f"Digite a nota {x+1}: ")))

# Loop while
contador = 1
while contador <= 5:
    print(contador)
    contador += 1

# Dicionário
pessoa = {
    "nome": "programador Python"
}
print(pessoa["nome"])
