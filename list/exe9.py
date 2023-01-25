'''
Faça um programa para gerenciar um cadastro de produtos, armazenados
em uma lista de dicionários, contendo: Código do Produto (int), 
Descrição (string) e Preço (float). O programa deve apresentar um
menu de opções ao usuário (laço), onde as opções disponíveis são: 
(1) Inserir um produto novo; (2) Procurar um produto pelo seu 
Código; (3) Remover um produto, considerando seu código; (4) 
Listar os produtos cadastrados; (5) FIM. Veja o exemplo abaixo do 
funcionamento do programa: (*) O menu pode ser re-exibido toda 
vez que for lida uma nova opção
'''

produtos = []

while(0 < 1):
    print("\nMenu:")
    print("1. Inserir um produto novo")
    print("2. Procurar um produto pelo seu Código")
    print("3. Remover um produto pelo código")
    print("4. Listar produtos cadastrados")
    print("5. FIM")

    op = input("Entre com sua opcao: ")

    if(op == "1"):
        c = int(input("Código: "))
        i = input("Descrição: ")
        p = float(input("Preço: "))
        produtos.append({"codigo": c, "descricao": i, "preco": p})
    elif(op == "2"):
        existe = 0
        c = int(input("Código: "))
        for i in produtos:
            if(i["codigo"] == c):
                existe = 1
                print("Codigo: {c} -".format(c = i["codigo"]), end = " ")
                print("Produto: {p} -".format(p = i["descricao"]), end = " ")
                print("Preco: {p}".format(p = i["preco"]))
                break
        if(existe == 0): print("produto inexistente")
    elif(op == "3"):
        c = int(input("Código: "))
        acumulador = 0
        for i in produtos:
            if(i["codigo"] == c):
                produtos.pop(acumulador)
            acumulador+=1
    elif(op == "4"):
        for i in produtos:
            print("Codigo: {c} -".format(c = i["codigo"]), end = " ")
            print("Produto: {p} -".format(p = i["descricao"]), end = " ")
            print("Preco: {p}".format(p = i["preco"]))
    elif(op == "5"):
        break
