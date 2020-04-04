#Boas vindas ao jogo
print("  \t !! Bem vindo ao jogo de CRAPS simplificado !! \n Este jogo foi feito pelos alunos Guilherme Rosada e Henrique Gabriel Oliveira Silva \n para a Disciplina de Design de Software, do curso de Engenharia do Insper \n sob orientação dos professores Andrew Toshiaki Nakayama Kurauchi e Barbara Tieko Agena")
# ------------ PRESET
#PRESET DO GAME + VARIÁVEIS que vão acompanhar todo o programa
from random import randint
dado1 = 0
dado2 = 0
somad=0
fichas = 100
JOGO = False #refere-se ao while interno => pra ficar perguntando a modalidade p/ apostar
CONTINUAR = True #refere-se ao jogo como um todo => pra ficar perguntando se fazer outra aposta.
show_PLB = True
show_FIELD = True
show_ANY = True
show_TWELVE = True
valor_A = 0
valor_B = 0
valor_C = 0
valor_D = 0
#FUNÇÕES DAS APOSTAS

#função para rodar a aposta passlinebet
#aposta A
def plb(valor_A):
    mao_A=0
    if somad == 7 or somad == 11 :
        print (" ==> PASS LINE BET: você tirou {0} e Ganhou! receberá {1} fichas" .format(somad, valor_A))
        mao_A += valor_A
    elif somad == 2 or somad == 3 or somad == 12:
        print (" ==> PASS LINE BET: você tirou {0} e Perdeu! será punido em {1} fichas" .format(somad, valor_A))
        mao_A -= valor_A
    else:
        print(" ==> PASS LINE BET: A soma dos dados foi {0}. Entraremos na fase POINT ! \n A sua aposta ainda é válida, mas agora os objetivos mudaram!! \n A soma obtida anteriormente está salva. \n Agora, para vencer, você deve ROLAR OS DADOS novamente e obter A MESMA SOMA. \n Se você obtiver 7, você perde sua aposta! \n Para deixar esta fase e terminar a rodada, você deve ROLAR OS DADOS até obter a soma obtida anteriormente ou até obter a soma 7" .format(somad)) 
        print ("...................................................... \n \n ==> Você está na fase: POINT <==.")
        fase_point = True
        while fase_point:
            iniciar_point = input("\n Para rolar os dados novamente, digite 'j' \n #: ")
            if iniciar_point == 'j': 
                print(" Que rufem os tambores e..... \n \t ROOOOOOOOLLL THE DICE!!! ")
                dado11 = randint(1,6)
                dado22 = randint(1,6)
                somad1 = dado11 + dado22
                print ("Você obteve: \n \t D1 = {0} \n \t D2 = {1}. \n \t SOMA = {2} " .format(dado11, dado22, somad1))

                if somad1 == somad:
                    print ("Parabéns! Você atingiu o valor da soma Anterior e Ganhou {0} fichas " .format(valor_A))
                    mao_A += valor_A
                    fase_point = False
                elif somad1 == 7:
                    print ("Você tirou a soma 7 e será punido em {0} fichas" .format(valor_A))
                    mao_A -= valor_A
                    fase_point = False
                else:
                    print ("Não foi dessa vez. Continue a rolar o dado até obter o valor da SOMA ANTERIOR ou 7")
                    iniciar_point = 'qlqer coisa'
            
    return mao_A

#função para rodar a aposta field
#aposta B
def field(valor_B):
    mao_B=0
    if somad == 5 or somad == 6 or somad == 7 or somad == 8:
        print (" ==> FIELD: você tirou {0} e Perdeu! será punido em {1} fichas" .format(somad, valor_B))
        mao_B -= valor_B
    elif somad == 3 or somad == 4 or somad == 9 or somad == 10 or somad == 11:
        print (" ==> FIELD: você tirou {0} e Ganhou! receberá {1} fichas" .format(somad, valor_B))
        mao_B += valor_B
    elif somad == 2:
        print (" ==> FIELD: você tirou {0} e Ganhou! receberá {1} fichas" .format(somad, 2*valor_B))
        mao_B += 2*valor_B
    else:
        print (" ==> FIELD: você tirou {0} e Ganhou! receberá {1} fichas" .format(somad, 3*valor_B))
        mao_B += 3*valor_B
    return mao_B

#função para rodar a aposta anycraft
#aposta C
def anycraft(valor_C):
    mao_C =0
    if somad == 12 or somad == 2 or somad == 3:
        print (" ==> ANYCRAFT: você tirou {0} e Ganhou! receberá {1} fichas" .format(somad, 7*valor_C))
        mao_C += 7*valor_C
    else:
        print (" ==> ANYCRAFT: você tirou {0} e Perdeu! Será punido em {1} fichas" .format(somad, valor_C))
        mao_C -= valor_C
    return mao_C

#função para rodar a aposta twelve
#Aposta D
def twelve (valor_D):  
    mao_D = 0
    if somad == 12 : 
        print (" ==> TWELVE: você tirou {0} e Ganhou! receberá {1} fichas" .format(somad, 30*valor_D))
        mao_D += 30*valor_D
    else:
        print (" ==> TWELVE: você tirou {0} e Perdeu! Será punido em {1} fichas" .format(somad, valor_D))
        mao_D -= valor_D
    return mao_D

# --------------------------- Jogo, de fato
#INFORMAÇÕES INICIAIS + INSTRUÇÕES

regras = input(" \n => VOCÊ COMEÇA O JOGO COM {0} FICHAS. \n Antes de apostar, quer conhecer as regras? (digite 's' para LER ou 'n' para PULAR e PROSSEGUIR \n #: " .format(fichas)) 
if regras == 's':
    print ("===========================================  Você pediu por ajuda. =========================================== \n  \n Cada modalidade funciona da seguinte maneira: \n ")
    print ("_A-) PASS LINE BET: (--#ESTA APOSTA SÓ PODE SER FEITA NA FASE 'COMEOUT'#--) \n \n Se a soma for (7 ou 11), você GANHA o que apostou.\n Se for (2,3 ou 12), você PERDE o que apostou.\n Se for (4, 5, 6, 8, 9 ou 10), o jogo vai para a fase 'POINT' \n  Nesta fase, novos dados serão rolados. \n Se a nova soma for a mesma que o valor inicial (4, 5, 6, 8, 9 ou 10), você GANHA o que apostou. \n Se sair uma soma 7, você PERDE! \n Se sair qualquer outro número, você continua na fase 'POINT' até acertar a soma inicial ou somar 7. \n")
    print ("_B-) FIELD: \n \n Se a soma for (5, 6, 7 ou 8), você PERDE! \n Se a soma for (3, 4, 9, 10 ou 11), você GANHA o que apostou. \n Se a soma for (2), você GANHA 2x do que apostou. \n Se a soma for (12), você GANHA 3x o que apostou. \n ")
    print ("_C-) ANY CRAPS: \n \n Se a soma for (2, 3 ou 12), você GANHA 7x o que apostou! \n Mas, se a soma der qualquer outro número, você PERDE a aposta. \n")
    print ("_D-) TWELVE: \n\n Se a soma der (12), você GANHA 30x o que apostou!! \n Mas, se der qualquer outro valor, você PERDE a aposta. \n")
#obs.: Nas regras do EP, há espaço para dupla interpretação da regra. Quando se diz 'perde tudo', pode-se entender que o jogador perde inclusive o valor que não tinha apostado ou perde somente o valor que tinha apostado. 
# Para ser um pouco mais próximo ao jogo real, decidimos que o jogador perderá somente o que ele apostou.

while not JOGO and CONTINUAR :  #perceba aqui, que para ter JOGO, ele deve estar em True! (por isso o 'not' na frente)
                                    #Então, qnd ele tiver False, o programa vai pedir se quer iniciar um novo jogo.
    inicio = input (" Deseja iniciar uma nova aposta? (digite 's' para SIM ou 'n' para NÃO) \n #: ")
    if inicio == 's':
         JOGO = True
    elif inicio == 'n':
        print ("Até a próxima! Você ficou com {0} fichas " .format(fichas))
        CONTINUAR = False
    else:
        print ("Não te entendi. ")


    #NOVA RODADA:
    while JOGO and fichas > 0:
        #COMEOUT 
        print ("................................................................. \n\n $$ FICHAS: {0} \n ==> Você está na fase: COMEOUT <== \n\n Nesta fase, você pode escolher entre várias modalidades diferentes de apostas. \n Após terminar suas apostas, digite 'jogar' para ROLAR OS DADOS e tentar a sorte!!  \n  \f Obs.: Em qualquer instante, você pode mudar sua aposta. Basta digitar novamente a letra equivalente à ela. \n \n ¬ Para entender cada modalidade, digite 'ajuda' \n  " .format(fichas))
        if show_PLB:
            print (" _A-) PASS LINE BET" )
        if show_FIELD: #quando o usuário escolhe alguma aposta, o show fica False. Aí, não aparece mais na proxima pergunta, até q ele aperte 'jogar'
            print (" _B-) FIELD" )
        if show_ANY: 
            print (" _C-) ANY CRAPS" )
        if show_TWELVE:
            print (" _D-) TWELVE" ) 
        pergunta1 = input(" \n ¬ Para escolher a modalidade, digite a letra correspondente (em maiúscula). \n ¬ Para sair, digite SAIR. \n Obs.: Você pode apostar em mais de uma modalidade, mas deve fazer uma aposta por vez e depois digitar 'jogar' \n\n ... Digite 'jogar' para ROLAR OS DADOS e tentar a sorte!! ($$)   \n  #: ")

        if pergunta1 == 'A':
            show_PLB = False
            print ("você escolheu _A-) PASS LINE BET !")
            valor_A = int(input(" Que valor deseja apostar nesta modalidade? (digite 0 para desistir de apostar nesta modalidade) \n #: "))
            if valor_A == 0:
                show_PLB = True

        elif pergunta1 == 'B':
            show_FIELD = False
            print ("Você escolheu _B-) FIELD !")
            valor_B = int(input(" Que valor deseja apostar nesta modalidade? (digite 0 para desistir de apostar nesta modalidade) \n #: "))
            if valor_B == 0:
                show_FIELD = True

        elif pergunta1 == 'C':
            show_ANY = False
            print ("Você escolheu _C-) ANY CRAPS !")
            valor_C = int(input(" Que valor deseja apostar nesta modalidade? (digite 0 para desistir de apostar nesta modalidade) \n #: "))
            if valor_C == 0:
                show_ANY = True

        elif pergunta1 == 'D':
            show_TWELVE = False
            print ("Você escolheu _D-) TWELVE !")
            valor_D = int(input(" Que valor deseja apostar nesta modalidade? (digite 0 para desistir de apostar nesta modalidade) \n #: "))
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
            elif valor_total == 0:
                print (" Você precisa apostar para poder jogar. Por favor, refaça as apostas! ")
                show_PLB = True
                show_ANY = True
                show_FIELD = True
                show_TWELVE = True
            elif valor_A <0 or valor_B <0 or valor_C <0 or valor_D <0:
                print (" Você apostou um valor que não é válido. Refaça suas apostas! ")
                show_PLB = True
                show_ANY = True
                show_FIELD = True
                show_TWELVE = True
                valor_A = valor_B = valor_C = valor_D = 0
            elif valor_total <= fichas:
                confirmar_apostas = input(" Você apostou os valores: \n \t {0} em PASS LIBE BET \n \t {1} em FIELD \n \t {2} em ANY CRAPS \n \t {3} em TWELVE \n ... Deseja confirmar as apostas? (digite 's' para CONFIRMAR ou 'n' para APOSTAR DE NOVO) \n #: " .format(valor_A, valor_B, valor_C, valor_D))
                if confirmar_apostas == 's':
                    print (" -----  \n Rufem os tambores e..... \n \t \t ROOOOOOOOLLL THE DICE!!! . \n .\n .\n .\n .\n .\n ")
                    JOGO = False
                    CONTINUAR = True 
#................... começando a executar as apostas
                    dado1 = randint(1,6)
                    dado2 = randint(1,6)
                    somad = dado1 + dado2
                    print("Os dados foram jogados! E obtivemos: \n \t D1 ={0} \n \t D2 = {1} \n \t SOMA = {2} ".format(dado1, dado2, somad))

                    if not show_FIELD:
                        fichas += field(valor_B)
                        print ("  $$ Você tem {0} fichas " .format (fichas))
                        
                    if not show_ANY:
                        fichas += anycraft(valor_C)
                        print ("  $$ Você tem {0} fichas " .format (fichas))
                        
                    if not show_TWELVE:
                        fichas += twelve(valor_D)
                        print ("  $$ Você tem {0} fichas " .format (fichas))
                        
                    if not show_PLB:
                        fichas += plb(valor_A)
                        print ("  $$ Você tem {0} fichas " .format (fichas))
                        
                    
                    show_PLB = True
                    show_ANY = True
                    show_FIELD = True
                    show_TWELVE = True    
# --------------------------------------- fim do bloco das apostas
# abaixo, é pra evitar que ocorram erros                    
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
                    valor_A = valor_B = valor_C = valor_D = 0





        elif pergunta1 == 'ajuda':
       #BLOCO EXPLICATIVO
            print ("===========================================  Você pediu por ajuda. =========================================== \n  \n Cada modalidade funciona da seguinte maneira: \n ")
            print ("_A-) PASS LINE BET: (--#ESTA APOSTA SÓ PODE SER FEITA NA FASE 'COMEOUT'#--) \n \n Se a soma for (7 ou 11), você GANHA o que apostou.\n Se for (2,3 ou 12), você PERDE o que apostou.\n Se for (4, 5, 6, 8, 9 ou 10), o jogo vai para a fase 'POINT' \n  Nesta fase, novos dados serão rolados. \n Se a nova soma for a mesma que o valor inicial (4, 5, 6, 8, 9 ou 10), você GANHA o que apostou. \n Se sair uma soma 7, você PERDE! \n Se sair qualquer outro número, você continua na fase 'POINT' até acertar a soma inicial ou somar 7. \n")
            print ("_B-) FIELD: \n \n Se a soma for (5, 6, 7 ou 8), você PERDE! \n Se a soma for (3, 4, 9, 10 ou 11), você GANHA o que apostou. \n Se a soma for (2), você GANHA 2x do que apostou. \n Se a soma for (12), você GANHA 3x o que apostou. \n ")
            print ("_C-) ANY CRAPS: \n \n Se a soma for (2, 3 ou 12), você GANHA 7x o que apostou! \n Mas, se a soma der qualquer outro número, você PERDE a aposta. \n")
            print ("_D-) TWELVE: \n\n Se a soma der (12), você GANHA 30x o que apostou!! \n Mas, se der qualquer outro valor, você PERDE a aposta. \n")






        elif pergunta1 == 'SAIR':
            print ("O jogo foi bom! Espero te ver na próxima vez.. \n Você ficou com {0} fichas. " .format(fichas))
            JOGO = False #aqui, tá intuitivo. O bloco interno vai parar
            CONTINUAR = False #E o bloco externo tbm.
        else:
            print ("Não te entendi. Repita a resposta, por favor!")

    if fichas <=0:
        print ("Que pena! Você não tem mais moedas. \n Até a próxima !!")
        CONTINUAR = False #aqui, o bloco maior para e tudo para