from Personagem import Mago, Berserker, Arqueiro
from Inimigos import Goblin, Orc, ChefeFinal
from combate import batalha


def menu_personagem():
    print("--- Escolha sua classe ---")
    print("1 - Mago")
    print("2 - Berserker")
    print("3 - Arqueiro")
    print("4 - Sair")

    while True:
        escolha = input("Digite a opção: ")
        nome = input("Digite o nome do seu personagem: ")

        if escolha == "1":
            return Mago(nome)
        elif escolha == "2":
            return Berserker(nome)
        elif escolha == "3":
            return Arqueiro(nome)
        elif escolha == "4":
            exit()
        else:
            print("Opção inválida")


def introducao(jogador):
    print("\n" + "="*60)
    print(f"Bem vindo {jogador.nome} o grande {jogador.classe}")
    print("Em um mundo assolado pelas trevas criaturas emergem das sombras\n")
    print("ameaçando vilarejos e consumindo tudo em seu caminho")
    print("Você e a última esperança de um povo esquecido pela luz\n")
    


def transicao(nome_area):
    print("\n" + "-"*50)
    print(f"Você avança para a próxima região: {nome_area}...")
    print("-"*50 + "\n")


def iniciar_jogo():
    jogador = menu_personagem()
    introducao(jogador)

    areas = [
        ("Floresta Sombria", [Goblin(), Goblin(), Orc()]),
        ("Montanhas Gelidas", [Orc(), Orc(), Goblin()]),
        ("Covil do Dragão", [ChefeFinal()])
    ]

    for nome_area, inimigos in areas:
        transicao(nome_area)
        print(f"\n=== Área: {nome_area} ===")
        for inimigo in inimigos:
            venceu = batalha(jogador, inimigo)
            if not venceu:
                print("\nGame Over")
                return

    print("\nParabéns Você venceu todos os inimigos")


if __name__ == "__main__":
    iniciar_jogo()
