# HenGuiA
exercício programa da matéria Design de Software 

ficha = 50

apostar_ou_nn = input("Você deseja apostar nessa rodada?(Sim ou Não")

if apostar_ou_nn == "Sim":
    aposta = int(input("Quanta fichas deseja apostar?"))
    while aposta >= ficha:
        print("Você tem somente {0} fichas disponíveis para apostar".format(ficha))
        aposta = int(input("Quanta fichas deseja apostar?"))

else apostar_ou_nn == "Não":
    ficha = 0
    print("O jogo acabou! Seu numero de fichas é {0}".format(ficha))
