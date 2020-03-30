# HenGuiA
exercício programa da matéria Design de Software 

from random import randint

dado1 = randint(1,6)
dado2 = randint(1,6)
somad = dado1 + dado2
ganhou_aposta = True


ficha = 50


nome = input("Bem vindo!! Digite seu nome para começar a jogar Craps:")
apostar_ou_nn = input("{0}, você tem {1} fichas. Deseja apostar nessa rodada?(Sim ou Não)".format(nome, ficha))

if apostar_ou_nn == "Sim":
if apostar_ou_nn == "Não":
    ficha = 0
    print("O jogo acabou! Seu número de fichas é {0}".format(ficha))

else:
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

    print(dado1)
    print(dado2)

else:
    ficha = 0
    print("O jogo acabou! Seu número de fichas é {0}".format(ficha))    while ganhou_aposta:
    while ganhou_aposta:
        if modalidade_t == "Sim":
            def twelve (ficha, aposta):
                if somad == 12 : 
                    ficha = ficha+30*aposta
        elif modalidade_ac == "Sim":
            def anycraps (ficha, aposta):
                if somad == 12 or somad == 2 or somad == 3:
                    ficha = ficha + 7*aposta 
        elif modalidade_f == "Sim":
            def field (ficha, aposta):
                if somad == 5 or somad == 6 or somad == 7 or somad == 8:
                    ficha = ficha - aposta
                elif somad == 3 or somad == 4 or somad == 9 or somad == 10 or somad == 11:
                    ficha = ficha + aposta
                elif somad == 2:
                    ficha = ficha + 2*aposta
                else:
                    ficha = ficha + 3*aposta