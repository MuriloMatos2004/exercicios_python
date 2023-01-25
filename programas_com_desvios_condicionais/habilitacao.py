'''
Ler os seguintes dados de uma pessoa: nome, sexo (M ou F), idade (0 a 150) e 
nacionalidade (brasileira ou estrangeira). Testar a validade dos dados fornecidos, 
indicando se o sexo, a idade e a nacionalidade são válidos ou inválidos. Se um dos 
dados fornecidos for inválido indicar ao usuário. Se todos os dados forem válidos, 
exibir uma mensagem como segue, considerando habilitados apenas os maiores de 18 anos, 
e onde aparecem os dados fornecidos: “José Silva, brasileiro do sexo masculino e
maior de idade, está habilitado a dirigir”

“Maria Silva, brasileira do sexo feminino e
maior de idade, está habilitada a dirigir”
“Junior Silva, brasileiro do sexo masculino e
menor de idade, não está habilitado a dirigir”.
'''

nome = input("Entre com um nome: ")
sexo = input("Entre com o sexo: ")
idade = input("Entre com a idade: ")
nacionalidade = input("Entre com a nacionalidade: ")

try:
    int(nome)
    int(sexo)
    int(nacionalidade)
    print("alguns dados sao invalidos")
except:
    if nacionalidade == "brasileiro" or nacionalidade == "estrangeiro":
        if sexo == "masculino" or sexo == "feminino":
            try:
                idade = int(idade)
                if idade > 0 and idade < 150:
                    if idade >= 18:
                        print("{nome}, {nacionalidade} do sexo {sexo} e maior de idade, esta habilitado a dirigir".format(nome = nome, nacionalidade = nacionalidade, sexo = sexo))
                    else:
                        print("{nome}, {nacionalidade} do sexo {sexo} e menor de idade, nao esta habilitado a dirigir".format(nome = nome, nacionalidade = nacionalidade, sexo = sexo))
                else:
                    print("idadde invalida")        
            except:
                print("idade invalida")
        else:
            print("sexo invalido")
    else:
        print("nacionalidade invalida")


