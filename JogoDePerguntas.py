"""
JOGO DE PERGUNTAS, 5 PERGUNTAS COM 4 ALTERNATIVAS CADA


"""

print("REGRAS DO JOGO")
print("O JOGADOR TEM A OBRIGAÇÃO DE ACERTAR TODAS AS 5 QUESTÕES!")
print("CASO CONTRÁRIO O JOGADOR SERA OBRIGADO A REINICIAR TODO O JOGO")
print("RESPONDA APENAS COM  ([a], [b], [c] ou [d]")
print("RESPONDA APENAS COM LETRAS MINÚSCULAS")

print("Tenha um ótimo jogo! ")


print("Ola, vamos começar nosso jogo de perguntas!, poderia nos informar seu nome? ")

nome = input()


print(" Olá %s, você ira participar de um jogo de 5 perguntas!, cada questão tera 4 alternativas,"  
"selecione apenas uma alternativa!" % nome)

print("Questão numero 1! ")

print("Quem descobriu o Brasil?:")
print("(a) Pedro Álvares Cabral")
print("(b) Ayrton Sena")
print("(c) Luciano Hulk")
print("(d) Ricardo")

resposta = input("digite uma das opções: ")

if resposta == 'a':
    print("Parabéns, você acertou!, Próxima pergunta! ")

else:
    print("Ops..., você errou a questão!, vamos reiniciar o jogo!")
    exit("Fim de jogo por erro da questão 1")



print("Questão numero 2! ")

print("Qual o animal mais rapido do mundo ?:")
print("(a) Leão")
print("(b) Onça")
print("(c) Guepardo")
print("(d) Tigre")

resposta = input("digite uma das opções: ")

if resposta == 'c':
    print("Parabéns, você acertou!, próxima pergunta! ")

else:
    print("Ops..., você errou a questão!, vamos reiniciar o jogo!")
    exit("Fim de jogo por erro da questão 2")



print("Questão numero 3! ")

print("Quem foi Albert Einstein  ?:")
print("(a) Foi um grande cientista que desenvolveu o método de Lei da inércia ")
print("(b) Foi um grnade psicólogo")
print("(c) Foi um grande cantor sertanejo")
print("(d) Albert Einstein foi um físico teórico alemão que desenvolveu a teoria da relatividade geral," 
"um dos pilares da física moderna ao lado da mecânica quântica.")

resposta = input("digite uma das opções: ")

if resposta == 'd':
    print("Parabéns, você acertou!, próxima pergunta! ")

else:
    print("Ops..., você errou a questão!, vamos reiniciar o jogo!")
    exit("Fim de jogo por erro da questão 3")



print("Questão numero 4! ")

print("Qual o valor dessa expressão  ?:")

print("20 +(28 - 10 + 7)= ?")

print("(a) 300")
print("(b) 45")
print("(c) 27")
print("(d) 23")

resposta = input("digite uma das opções: ")

if resposta == 'b':
    print("Parabéns, você acertou!, próxima pergunta! ")

else:
    print("Ops..., você errou a questão!, vamos reiniciar o jogo!")
    exit("Fim de jogo por erro da questão 4")



print("Questão numero 5! ")

print("Quais são os componentes do gas de cozinha  ?:")

print("(a)  Metano (CH4), propano (C3H8)")
print("(b) Propano (C3H8), Propeno (C3H6), Butano (C4H10) e Buteno (C4H8)")
print("(c) Butano (C4H10) e Buteno (C4H8)")
print("(d) (C3H8), Propeno (C3H6)")

resposta = input("digite uma das opções: ")

if resposta == 'b':
    print("Parabéns, você acertou!")

else:
    print("Ops..., você errou a questão!, vamos reiniciar o jogo!")
    exit("Fim de jogo por erro da questão 5")


print(" Olha só!, se você chegou até aqui, provavelmente acertou todas as respostas, Parabéns!!!")