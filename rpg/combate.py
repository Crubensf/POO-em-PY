def menu_acoes():
    print("\nEscolha sua ação:")
    print("1 - Ataque Comum")
    print("2 - Ataque Mágico")
    print("3 - Bloquear")
    print("4 - Curar")
    print("5 - Recuperar Mana")


def batalha(jogador, inimigo):
    print(f"\n--- Início da batalha: {jogador.nome} vs {inimigo.nome} ---")

    while jogador.esta_vivo() and inimigo.esta_vivo():
        jogador.status()
        inimigo.status()

        # TURNO DO JOGADOR
        menu_acoes()
        escolha = input("-> ")

        if escolha == "1":
            jogador.atacar(inimigo)
        elif escolha == "2":
            jogador.ataque_magico(inimigo)
        elif escolha == "3":
            jogador.bloquear()
        elif escolha == "4":
            jogador.curar()
        elif escolha == "5":
            jogador.recuperar_mana()
        else:
            print("Ação inválida. Você perdeu o turno.")

        if not inimigo.esta_vivo():
            print(f"\nVocê derrotou {inimigo.nome}!")
            return True

        # TURNO DO INIMIGO
        print(f"\nTurno de {inimigo.nome}:")
        inimigo.escolher_acao(jogador)

        if not jogador.esta_vivo():
            print(f"\n{jogador.nome} foi derrotado!")
            return False
