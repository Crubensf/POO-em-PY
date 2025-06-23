import random
from Personagem import Personagem


class Inimigo(Personagem):
    def __init__(self, nome, hp, ataque, defesa, critico=0.05, esquiva=0.05, mana=0):
        super().__init__(nome, hp, ataque, defesa, critico, esquiva, mana)

    def escolher_acao(self, alvo):
        acoes = ["atacar"]
        if self.mana >= 10:
            acoes.append("ataque_magico")
        if self.mana >= 8 and self.hp < 50:
            acoes.append("curar")

        acao_escolhida = random.choice(acoes)
        if acao_escolhida == "atacar":
            self.atacar(alvo)
        elif acao_escolhida == "ataque_magico":
            self.ataque_magico(alvo)
        elif acao_escolhida == "curar":
            self.curar()

    def atacar(self, alvo):
        dano = self.ataque
        if random.random() < self.critico:
            print("**CRITICO DO INIMIGO**")
            dano *= 2
        print(f"{self.nome} ataca {alvo.nome}, causando {dano:.0f} de dano.")
        alvo.receber_dano(dano)

    def ataque_magico(self, alvo):
        if self.mana >= 10:
            dano = self.ataque + 5
            self.mana -= 10
            print(f"{self.nome} usa um ataque mágico em {alvo.nome}")
            alvo.receber_dano(dano)
        else:
            print(f"{self.nome} tentou usar um ataque mágico mas não tinha mana suficiente.")

    def curar(self):
        if self.mana >= 8:
            cura = 15
            self.hp += cura
            self.mana -= 8
            print(f"{self.nome} se cura recuperando {cura} de HP.")
        else:
            print(f"{self.nome} tentou se curar mas não tinha mana suficiente")


class Goblin(Inimigo):
    def __init__(self):
        super().__init__(nome="Goblin", hp=30, ataque=6, defesa=2, critico=0.05, esquiva=0.1, mana=10)

class Orc(Inimigo):
    def __init__(self):
        super().__init__(nome="Orc", hp=50, ataque=10, defesa=4, critico=0.1, esquiva=0.08, mana=15)

class ChefeFinal(Inimigo):
    def __init__(self):
        super().__init__(nome="Dragão Ancião", hp=120, ataque=18, defesa=8, critico=0.2, esquiva=0.1, mana=30)