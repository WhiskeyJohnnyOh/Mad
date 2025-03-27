lista_de_compras = []

def adicionar_item():
    nome = input("O que você quer adicionar?\n")
    preco = float(input("Qual o valor do produto?\n"))
    item = {'nome' : nome, 'preco_unitario' : preco}
    lista_de_compras.append(item)

while True:
        adicionar_item() 

        print("\nLista de compras:")
        for item in lista_de_compras:
            print(f"Item: {item['nome']}, Preço: R${item['preco_unitario']:.2f}")
            print("Valor total: R$" {'preco_unitario' + 'preco_unitario'})

        continuar = input("Deseja adicionar mais algum item? (s/n): ").strip().lower()

        if continuar == 'n':
             break
