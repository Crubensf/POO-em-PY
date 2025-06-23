from abc import ABC, abstractmethod
import random


class ICombatente(ABC):
    @abstractmethod
    def atacar(self, alvo): pass

    @abstractmethod
    def ataque_magico(self, alvo): pass

    @abstractmethod
    def curar(self): pass


class Personagem(ICombatente, ABC):
    def __init__(self, nome, hp, ataque, defesa, critico, esquiva, mana=0):
        self.nome = nome
        self.hp = hp
        self.ataque = ataque
        self.defesa = defesa
        self.critico = critico
        self.esquiva = esquiva
        self.mana = mana
        self.bloqueando = False
        self.classe = None

    @abstractmethod
    def atacar(self, alvo):
        pass

    @abstractmethod
    def ataque_magico(self, alvo):
        pass

    @abstractmethod
    def curar(self):
        pass

    def recuperar_mana(self):
        self.mana += 15
        print(f"{self.nome} recuperou 15 de mana. Mana atual: {self.mana}")

    def bloquear(self):
        self.bloqueando = True
        print(f"{self.nome} está em posição de bloqueio. Dano será reduzido no próximo ataque.")

    def receber_dano(self, dano):
        if self.bloqueando:
            dano *= 0.5
            self.bloqueando = False
            print(f"{self.nome} bloqueou parte do dano.")

        if random.random() < self.esquiva:
            print(f"{self.nome} esquivou do ataque.")
            return

        dano_final = max(0, dano - self.defesa)
        self.hp -= dano_final
        print(f"{self.nome} recebeu {dano_final:.0f} de dano.")

    def esta_vivo(self):
        return self.hp > 0

    def status(self):
        print(f"{self.nome} | HP: {self.hp} | Mana: {self.mana} | Defesa: {self.defesa}")

# Classes

class Mago(Personagem):
    def __init__(self, nome):
        super().__init__(nome, hp=70, ataque=15, defesa=0.5, critico=0.2, esquiva=0.1, mana=50)
        self.classe = "Mago"

    def atacar(self, alvo):
        dano = self.ataque
        if random.random() < self.critico:
            print("**CRÍTICO**")
            dano *= 2
        print(f"{self.nome} ataca {alvo.nome} com um bastão mágico.")
        alvo.receber_dano(dano)

    def ataque_magico(self, alvo):
        if self.mana >= 10:
            dano = self.ataque + 10
            self.mana -= 10
            print(f"{self.nome} lança uma Bola de Fogo em {alvo.nome}")
            alvo.receber_dano(dano)
        else:
            print(f"{self.nome} está sem mana.")

    def curar(self):
        cura = 20
        self.hp += cura
        print(f"{self.nome} conjura uma magia de cura e recupera {cura} de HP.")

class Berserker(Personagem):
    def __init__(self, nome):
        super().__init__(nome, hp=90, ataque=12, defesa=2, critico=0.1, esquiva=0.07, mana=20)
        self.classe = "Berserker"
        self.buff_turnos = 0

    def atacar(self, alvo):
        dano = self.ataque
        if self.buff_turnos > 0:
            dano *= 1.3
            self.buff_turnos -= 1
        if random.random() < self.critico:
            print("**CRÍTICO**")
            dano *= 2
        print(f"{self.nome} desfere um golpe brutal em {alvo.nome}")
        alvo.receber_dano(dano)

    def ataque_magico(self, alvo):
        if self.mana >= 8:
            self.mana -= 8
            self.buff_turnos = 3
            print(f"{self.nome} ativa 'Fúria Interior'. Seu ataque será aumentado por 3 turnos.")
        else:
            print(f"{self.nome} está sem mana.")

    def curar(self):
        cura = 15
        self.hp += cura
        print(f"{self.nome} regenera {cura} de HP.")

class Arqueiro(Personagem):
    def __init__(self, nome):
        super().__init__(nome, hp=80, ataque=10, defesa=1, critico=0.3, esquiva=0.3, mana=20)
        self.classe = "Arqueiro"
        self.critico_forcado = 0

    def atacar(self, alvo):
        dano = self.ataque
        crit = False
        if self.critico_forcado > 0:
            crit = True
            self.critico_forcado -= 1
        elif random.random() < self.critico:
            crit = True

        if crit:
            print("**CRÍTICO**")
            dano *= 2
        print(f"{self.nome} dispara uma flecha em {alvo.nome}")
        alvo.receber_dano(dano)

    def ataque_magico(self, alvo):
        if self.mana >= 8:
            self.mana -= 8
            self.critico_forcado = 2
            print(f"{self.nome} ativa 'Precisão Mortal'. Os próximos 2 ataques serão críticos.")
        else:
            print(f"{self.nome} está sem mana.")

    def curar(self):
        cura = 10
        self.hp += cura
        print(f"{self.nome} recupera {cura} de HP.")
