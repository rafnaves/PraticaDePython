# POO - classes e objetos


# Classe exemplo
class Pessoa:
    def __init__(self, nome, idade): # Metodo
        self.nome = nome # Atributos
        self.idade = idade
    
    def saudacao(self):
        return f"Olá, Meu nome é {self.nome} e eu tenho {self.idade} anos."

# Objetos
# Os objetos chamam tanto a Classe para si, quanto funções 
# que serão executadas usando as informações do objeto
pessoa1 = Pessoa("Alice", 30)
mensagem = pessoa1.saudacao()
print (mensagem)

pessoa2 = Pessoa("Rafael", 21)
mensagem = pessoa2.saudacao()
print (mensagem)

# Herança
# Exemplo de herança

'''class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        print(f"O animal {self.nome} andou")
        return
    def emitir_som(self):
        pass

# Classe que herdou
class Cachorro(Animal):
     def emitir_som(self):
        return "au, au" # polimorfismo
     
class Gato(Animal):
    def emitir_som(self):
        return "Miau!" # polimorfismo
    
# Objetos
dog = Cachorro(nome="Renatinho")
cat = Gato(nome="Feliciana")

# Polimorfismo
animais = [dog, cat]

for animal in animais:
    print(f"{animal.nome} faz: {animal.emitir_som()}")'''


# Encapsulamento
class ContaBancaria:
    def  __init__(self, saldo):
        self.__saldo = saldo

    def  depositar(self, valor):
        if valor > 0:
            self.__saldo += valor 
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
    
    def consultar_saldo(Self):
        return Self.__saldo
    
conta = ContaBancaria(saldo=1000)
print(f"Saldo da conta: {conta.consultar_saldo()}")
conta.depositar(valor=1200)
conta.sacar(valor=150)
print(f"Saldo da conta: {conta.consultar_saldo()}")

# Exemplo de Abstração
from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

class Carro(Veiculo):
    def __init__(self):
        super().__init__()

# Herança multipla

class Animal:
    def __init__(self, nome):
        self.nome = nome

    def emitir_som(self):
        pass

class Mamifero(Animal):
    def amamentar(self):
        return f"{self.nome} está amamentando"
    
class Ave(Animal):
    def voar(self):
        return f"{self.nome} está voando"

class Morcego(Mamifero, Ave):
    def emitir_som(self):
        return "Morcegos emitem sons ultrassônicos"
    
morcego = Morcego(nome="Batman")

# Acessando métodos da classe base "animal"
print("Nome do morcego:", morcego.nome)
print("Som do Morcego:", morcego.emitir_som())

# Acessando os metodos das classes "Mamimefero" e "Ave"
print("Morcego amamentando:", morcego.amamentar())
print("Morcego voando:", morcego.voar())

# Decoradores

def meu_decorador(func):
    def wrapper():
        print("Antes da função ser chamada")
        func()
        print("depois da função ser chamada")
    return wrapper

@meu_decorador
def minha_funcao():
    print("Minha função foi chamada")

minha_funcao()

class MeuDecorador:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwds):
        pass


# Decoradores Comuns

class MinhaClasse:
    valor = 10
    def __init__(self, nome):
        self.nome = nome # Atributo da instancia

    def metodo_instancia(self):
        return f"Metodo de instancia chamado para {self.nome}"
    
    @classmethod
    def  metodo_classe(cls):
        return f"Metodo de classe chamado para valor={cls.valor}"
    
    @staticmethod
    def metodo_estatico():
        return "Metodo estatico chamado"
    

obj = MinhaClasse(nome="Exemplo")
print(obj.metodo_instancia())
print(MinhaClasse.metodo_classe())
print(MinhaClasse.metodo_estatico())

class Carros:
    def  __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    @classmethod
    def criar_carro(cls, configuracao):
        marca, modelo, ano = configuracao.split(",")
        return cls(marca, modelo, int(2022))
    

configuracao1 = "Toyota,Corolla,2022"
carro1 = Carros.criar_carro(configuracao1)
print(f"marca:{carro1.marca}\nModelo:{carro1.modelo}\nAno: {carro1.ano}")

class Matematica:

    @staticmethod
    def somar(a, b):
        return a + b
    
print(Matematica.somar(a=10, b=15))