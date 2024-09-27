nome = input("informe o nome: ")
idade = int(input("informe a idade: "))
while True:
    # Exibindo a lista de filmes   
    print("sala 1- O Poderoso Chefão livre")
    print("sala 2 -Lower and Order 12 anos")
    print("sala 3 - O Senhor dos Anéis 16 anos")
    #recebe a sala desejada pelo usuario
    sala = input("informe a sala desejada: ")

    #verifica a sala do usuario
    match sala:
        case "1":
            idade_minima = 0
        case "2":
            idade_minima = 12
        case "3":
            idade_minima = 16
        # default
        # nao tem espaço no case
        case _:
            print("sala inexistente")
            continue

#idade para ver s o usuario ver o filme basicamente isso é o ingresso
#na duvida nao use o operador ternario
    if idade >= idade_minima:
      print(f"entrada de {nome} está autorizado.")
      break
    else:
        print(f"entrada de {nome} não está autorizado.")
        print("favor escolher outro filme.")
        continue