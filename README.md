# HenGuiA
exercício programa da matéria Design de Software 

ficha = 50

nome = input("Bem vindo!! Digite seu nome para começar a jogar Craps:")
apostar_ou_nn = input("{0}, você tem {1} fichas. Deseja apostar nessa rodada?(Sim ou Não)".format(nome, ficha))

if apostar_ou_nn == "Sim":
    aposta = int(input("Quanta fichas deseja apostar?"))
    while aposta >= ficha:
        print("Você tem somente {0} fichas disponíveis para apostar".format(ficha))
        aposta = int(input("Digite novamente quantas fichas deseja apostar?"))
    print("{0} agora vamos entrar na fase chamada Come Out".format(nome))
    print("Na fase Come Out você pode apostar nas modalidades Pass Line Bet, Field, Any Craps e Twelve.")
    modalidade_plb = input("Você deseja jogar na modalidade Pass Line Bet?(Sim OU Não)")
    modalidade_f = input("Você deseja jogar na modalidade Field?(Sim OU Não)")
    modalidade_ac = input("Você deseja jogar na modalidade Any Craps?(Sim OU Não)")
    modalidade_t = input("Você deseja jogar na modalidade Twelve?(Sim OU Não)")


else:
    ficha = 0
    print("O jogo acabou! Seu número de fichas é {0}".format(ficha))