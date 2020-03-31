#Boas vindas ao jogo
print("  \t !! Bem vindo ao jogo de CRAPS simplificado !! \n Este jogo foi feito pelos alunos Guilherme Rosada e Henrique Gabriel Oliveira Silva \n para a Disciplina de Design de Software, sob orientação do professor Andrew")

#PRESET DO GAME + VARIÁVEIS que vão acompanhar todo o programa
dado1 = 0
dado2 = 0
SOMA = dado1 + dado2
fichas = 100
JOGO = False

#INFORMAÇÕES INICIAIS + INSTRUÇÕES
inicio = input(" \n => VOCÊ COMEÇA O JOGO COM {0} FICHAS. \n Deseja iniciar uma nova aposta? (digite 's' para SIM ou 'n' para NÃO) \n #: " .format(fichas))
if inicio == 's':
     JOGO = True
else:
    print ("Até a próxima!")

#NOVA RODADA:
while JOGO and fichas > 0:
    #COMEOUT
    print (" $$ FICHAS: {0} \n ==> Você está na fase: COMEOUT <== \n\n Nesta fase, você pode escolher entre várias modalidades diferentes de apostas: \n _A-) PASS LINE BET \n _B-) FIELD \n _C-) ANY CRAPS \n _D-) TWELVE" .format(fichas))
    pergunta1 = input(" ¬ Para escolher a modalidade, digite a letra correspondente (em maiúscula). \n ¬ Para sair, digite SAIR. \n ¬ Para entender cada modalidade, digite 'ajuda' \n #: ")
    if pergunta1 == 'A':
        print ("você escolheu A")
    elif pergunta1 == 'B':
        print ("Você escolheu B")
    elif pergunta1 == 'C':
        print ("Você escolheu C ")  
    elif pergunta1 == 'D':
        print ("Você escolheu D ")
    elif pergunta1 == 'ajuda':
   #BLOCO EXPLICATIVO
        print ("===========================================  Você pediu por ajuda. =========================================== \n  \n Cada modalidade funciona da seguinte maneira: \n ")
        print ("_A-) PASS LINE BET: (--#ESTA APOSTA SÓ PODE SER FEITA NA FASE 'COMEOUT'#--) \n \n Se a soma for (7 ou 11), você GANHA o que apostou.\n Se for (2,3 ou 12), você PERDE o que apostou.\n Se for (4, 5, 6, 8, 9 ou 10), o jogo vai para a fase 'POINT' \n  Nesta fase, novos dados serão rolados. \n Se a nova soma for a mesma que o valor inicial (4, 5, 6, 8, 9 ou 10), você GANHA o que apostou. \n Se sair uma soma 7, você PERDE TUDO! \n Se sair qualquer outro número, você continua na fase 'POINT' até acertar a soma inicial ou somar 7. \n")
        print ("_B-) FIELD: \n \n Se a soma for (5, 6, 7 ou 8), você PERDE TUDO! \n Se a soma for (3, 4, 9, 10 ou 11), você GANHA o que apostou. \n Se a soma for (2), você GANHA 2x do que apostou. \n Se a soma for (12), você GANHA 3x o que apostou. \n ")
        print ("_C-) ANY CRAPS: \n \n Se a soma for (2, 3 ou 12), você GANHA 7x o que apostou! \n Mas, se a soma der qualquer outro número, você PERDE a aposta. \n")
        print ("_D-) TWELVE: \n\n Se a soma der (12), você GANHA 30x o que apostou!! \n Mas, se der qualquer outro valor, você PERDE a aposta. \n")






    elif pergunta1 == 'SAIR':
        print ("O jogo foi bom! Espero te ver na próxima vez.. ")
        JOGO = False
    else:
        print ("Não te entendi. Até a próxima!")
        JOGO = False
