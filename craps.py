#Boas vindas ao jogo
print("  \t !! Bem vindo ao jogo de CRAPS simplificado !! \n Este jogo foi feito pelos alunos Guilherme Rosada e Henrique Gabriel Oliveira Silva \n para a Disciplina de Design de Software, sob orientação do professor Andrew")

#PRESET DO GAME + VARIÁVEIS que vão acompanhar todo o programa
dado1 = 0
dado2 = 0
SOMA = dado1 + dado2
fichas = 100
JOGO = False
show_PLB = True
show_FIELD = True
show_ANY = True
show_TWELVE = True
valor_A = 0
valor_B = 0
valor_C = 0
valor_D = 0
#INFORMAÇÕES INICIAIS + INSTRUÇÕES
inicio = input(" \n => VOCÊ COMEÇA O JOGO COM {0} FICHAS. \n Deseja iniciar uma nova aposta? (digite 's' para SIM ou 'n' para NÃO) \n #: " .format(fichas))
if inicio == 's':
     JOGO = True
else:
    print ("Até a próxima!")

#NOVA RODADA:
while JOGO and fichas > 0:
    #COMEOUT
    print (" $$ FICHAS: {0} \n ==> Você está na fase: COMEOUT <== \n\n Nesta fase, você pode escolher entre várias modalidades diferentes de apostas. \n Após terminar suas apostas, digite 'jogar' para ROLAR OS DADOS e tentar a sorte!! " .format(fichas))
    if show_PLB:
        print (" _A-) PASS LINE BET" )
    if show_FIELD:
        print (" _B-) FIELD" )
    if show_ANY: 
        print (" _C-) ANY CRAPS" )
    if show_TWELVE:
        print (" _D-) TWELVE" ) 
    pergunta1 = input(" \n ¬ Para escolher a modalidade, digite a letra correspondente (em maiúscula). \n ¬ Para sair, digite SAIR. \n ¬ Para entender cada modalidade, digite 'ajuda' \n  \f Obs.: Em qualquer instante, você pode mudar sua aposta. Basta digitar novamente a letra equivalente à ela. \n\n ... Apostas terminadas? digite 'jogar' para ROLAR OS DADOS e tentar a sorte!! ($$)  \n #: ")
    if pergunta1 == 'A':
        show_PLB = False
        print ("você escolheu _A-) PASS LINE BET !")
        valor_A = int(input(" Que valor deseja apostar nesta modalidade? (digite 0 para desistir de apostar nesta modalidade) "))
        if valor_A == 0:
            show_PLB = True

    elif pergunta1 == 'B':
        show_FIELD = False
        print ("Você escolheu _B-) FIELD !")
        valor_B = int(input(" Que valor deseja apostar nesta modalidade? (digite 0 para desistir de apostar nesta modalidade) "))
        if valor_B == 0:
            show_FIELD = True

    elif pergunta1 == 'C':
        show_ANY = False
        print ("Você escolheu _C-) ANY CRAPS !")
        valor_C = int(input(" Que valor deseja apostar nesta modalidade? (digite 0 para desistir de apostar nesta modalidade) "))
        if valor_C == 0:
            show_ANY = True

    elif pergunta1 == 'D':
        show_TWELVE = False
        print ("Você escolheu _D-) TWELVE !")
        valor_D = int(input(" Que valor deseja apostar nesta modalidade? (digite 0 para desistir de apostar nesta modalidade) "))
        if valor_D == 0:
            show_TWELVE = True

    elif pergunta1 == 'jogar':
        valor_total = valor_A + valor_B + valor_C + valor_D 
        if valor_total > fichas:
            print (" \t !!! Você apostou mais fichas do que possui atualmente. Por favor, refaça suas apostas !!! ")
            valor_A = valor_B = valor_C = valor_D = 0
            show_PLB = True
            show_ANY = True
            show_FIELD = True
            show_TWELVE = True
        elif valor_total <= fichas:
            confirmar_apostas = input(" Você apostou os valores: \n \t {0} em PASS LIBE BET \n \t {1} em FIELD \n \t {2} em ANY CRAPS \n \t {3} em TWELVE \n ... Deseja confirmar as apostas? (digite 's' para CONFIRMAR ou 'n' para APOSTAR DE NOVO) " .format(valor_A, valor_B, valor_C, valor_D))
            if confirmar_apostas == 's':
                print ("ROOOOOOOOLLL THE DICE!!! ")
            elif confirmar_apostas == 'n':
                show_PLB = True
                show_ANY = True
                show_FIELD = True
                show_TWELVE = True
            else: 
                print ("Não entendi sua resposta. Refaça as apostas")
                show_PLB = True
                show_ANY = True
                show_FIELD = True
                show_TWELVE = True





    elif pergunta1 == 'ajuda':
   #BLOCO EXPLICATIVO
        print ("===========================================  Você pediu por ajuda. =========================================== \n  \n Cada modalidade funciona da seguinte maneira: \n ")
        print ("_A-) PASS LINE BET: (--#ESTA APOSTA SÓ PODE SER FEITA NA FASE 'COMEOUT'#--) \n \n Se a soma for (7 ou 11), você GANHA o que apostou.\n Se for (2,3 ou 12), você PERDE o que apostou.\n Se for (4, 5, 6, 8, 9 ou 10), o jogo vai para a fase 'POINT' \n  Nesta fase, novos dados serão rolados. \n Se a nova soma for a mesma que o valor inicial (4, 5, 6, 8, 9 ou 10), você GANHA o que apostou. \n Se sair uma soma 7, você PERDE TUDO! \n Se sair qualquer outro número, você continua na fase 'POINT' até acertar a soma inicial ou somar 7. \n")
        print ("_B-) FIELD: \n \n Se a soma for (5, 6, 7 ou 8), você PERDE TUDO! \n Se a soma for (3, 4, 9, 10 ou 11), você GANHA o que apostou. \n Se a soma for (2), você GANHA 2x do que apostou. \n Se a soma for (12), você GANHA 3x o que apostou. \n ")
        print ("_C-) ANY CRAPS: \n \n Se a soma for (2, 3 ou 12), você GANHA 7x o que apostou! \n Mas, se a soma der qualquer outro número, você PERDE a aposta. \n")
        print ("_D-) TWELVE: \n\n Se a soma der (12), você GANHA 30x o que apostou!! \n Mas, se der qualquer outro valor, você PERDE a aposta. \n")






    elif pergunta1 == 'SAIR':
        print ("O jogo foi bom! Espero te ver na próxima vez.. \n Você ficou com {0} fichas. " .format(fichas))
        JOGO = False
    else:
        print ("Não te entendi. Repita a resposta, por favor!")

if fichas <=0:
    print ("Que pena! Você não tem mais moedas. \n Até a próxima !!")