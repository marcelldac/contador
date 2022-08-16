print('---------------CONTADOR---------------')

frase = input("Digite uma frase:\n") #frase
caracteres = len(frase.split()) #caracteres da frase
escolha = input("Digite [1] para saber a quantidade de letras ou caracteres.\n Digite [2] para saber a quantidade de palavras.\n") #variavel pra usar no switch case

match escolha: #switch case usando a var de cima
    case '1':
        print('A frase tem', len(frase), 'letra(s)') #caso 1 pra mostrar as letras
    case '2':
        print("A frase tem ",caracteres,"palavra(s)") #caso 2 pra mostrar as palavras  
    case '_':
        print("O numero digitado não foi cadastrado. ENCERRANDO PROGRAMA.") #caso 4 pra caso a pessoa tenha digitado errado