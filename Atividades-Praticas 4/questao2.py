# 2 - Criar um código que registre as notas de alunos e calcular a média da turma.

# Variaveis de ambiente
notas = []
soma = 0

#Laço de repetição
while True:
    try:
        nota = input("Digite uma nota ou digite fim para calcular a media: ")
        if nota.lower() == "fim":
            for n in notas:
                soma = soma + n
            media  = soma / len(notas)
            print (media)

            #Resultado
            print("a media da turma é: ")
            break
        
        nota = float(nota)
        if nota < 0 or nota > 10:
            raise Exception("Digite um numero de 0 a 10")
        notas.append(nota)
        print (notas)

    #Tratativa de erros
    except ValueError:
        print("Digite um caracter valido")
    except Exception as e:
        print(f'Erro: "{e}"')