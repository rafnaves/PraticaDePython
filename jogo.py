# Personagem: Classe mae
# Heroi: Class herdada
# Inimigo: Adversario do Usuario
import random

class Personagem:
    def __init__(self, Nome, Vida, Level):
        self.__Nome = Nome
        self.__Vida = Vida
        self.__Level = Level

    def get_Nome(self):
        return self.__Nome

    def get_Vida(self):
        return self.__Vida

    def get_Level(self):
        return self.__Level
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_Nome()}\nVida: {self.get_Vida()}\nNivel: {self.get_Level()}"
    
    def atacar(self, alvo):
        dano = random.randint(self.get_Level() * 2, self.get_Level() * 4)
        alvo.receber_ataque(dano)
        print(f"{self.get_Nome()} atacou {alvo.get_Nome()} e causou {dano} de dano!")

    def receber_ataque(self, dano):
        self.__Vida -= dano
        if self.__Vida < 0:
            self.__Vida = 0

class Heroi(Personagem):
    def __init__(self, Nome, Vida, Level, habilidade):
        super().__init__(Nome, Vida, Level)
        self.__habilidade = habilidade

    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"
    
    def ataque_especial(self, alvo):
        dano = random.randint(self.get_Level() * 5, self.get_Level() * 8)
        alvo.receber_ataque(dano)
        print(f"{self.get_Nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_Nome()} e causou {dano}")

class Inimigo(Personagem):
    def __init__(self, Nome, Vida, Level, tipo):
        super().__init__(Nome, Vida, Level)
        self.__tipo = tipo

    def  get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"
    
class Jogo:
    """_Classe orquestradora do jogo
    """
    def __init__(self):
        self.heroi = Heroi(Nome="Lindsay", Vida=100, Level=5, habilidade="super-força")
        self.inimigo = Inimigo(Nome="Paris", Vida=50, Level=3, tipo="Voador")  # Nome da variável corrigido

    def iniciar_batalha(self):
        """Fazer a gestão da batalha em turnos"""
        print("Iniciando Batalha")
        while self.heroi.get_Vida() > 0 and self.inimigo.get_Vida() > 0:
            print("\nDetalhes dos Personagens:")
            print(self.heroi.exibir_detalhes())
            print(self.inimigo.exibir_detalhes())

            input("Pressione Enter para atacar...")
            escolha = input("Escolha(1 - Ataque Normal, 2 - Ataque Especial):")

            if escolha == "1":
                self.heroi.atacar(self.inimigo)
            elif escolha == '2':
                self.heroi.ataque_especial(self.inimigo)
            else:
                print("Escolha invalida")

            if self.inimigo.get_Vida() > 0:
                #inimigo ataca heroi
                self.inimigo.atacar(self.heroi)

        if self.heroi.get_Vida() > 0:
            print("\n Parabens voce venceu")
        else:
            print("\n Voce morreu")


# Criar instancia do jogo e iniciar batalha

Jogo = Jogo()
Jogo.iniciar_batalha()