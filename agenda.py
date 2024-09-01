import os 

ARQUIVO_CONTATOS = "agenda_telefonica.txt"

def carregar_contatos():
    contatos = {}
    if os.path.exists(ARQUIVO_CONTATOS):
        with open(ARQUIVO_CONTATOS, 'r') as arquivo:
            for linha in arquivo:
                if linha.strip():
                    dados = linha.strip().split(',')
                    nome = dados[0]
                    telefone = dados[1]
                    email = dados[2]
                    favorito = dados[3] == "True"
                    contatos[nome] = {'telefone': telefone, 'email':email, 'favorito': favorito}
    else:
        with open(ARQUIVO_CONTATOS, 'w') as arquivo:
            pass
    return contatos

def salvar_contatos(contatos):
    with open(ARQUIVO_CONTATOS, 'w') as arquivo:
        for nome, dados in contatos.items():
            arquivo.write(f"{nome},{dados['telefone']},{dados['email']}\n")

def adicionar_contato():
    nome = input("digite o nome do contato: ")
    telefone = int(input("digite o numero deste contato: "))
    email = input("Digite o e-mail: ")

    contatos[nome] = {'telefone': telefone, 'email':email, 'favorito': False}
    salvar_contatos(contatos)
    print(f"contato {nome} salvo com sucesso!")

def listar_contatos():
    if contatos:
        print("\nAgenda Telefônica:")
        for nome, dados in contatos.items():
            status_favorito = " (Favorito)" if dados['favorito'] else ""
            print(f"Nome: {nome}, Telefone: {dados['telefone']}, E-mail: {dados['email']}{status_favorito}")
    else:
        print("A agenda não possuí nenhum contato ainda")

def listar_favoritos():
    favoritos = {nome: dados for nome, dados in contatos.items() if dados['favorito']}
    if favoritos:
        print("\nContatos Favoritos:")
        for nome, dados in favoritos.items():
            print(f"Nome: {nome}, Telefone: {dados['telefone']}, E-mail: {dados['email']}")
    else:
        print("Nenhum contato favorito encontrado.")

def editar_contato():
    nome = input("Digite o nome do contato que deseja editar: ")

    if nome in contatos:
        print(f"Contato atual: Nome: {nome}, Telefone: {contatos[nome]['telefone']}, E-mail: {contatos[nome]['email']}")
        novo_telefone = input("Digite o novo telefone (ou pressione Enter para manter o atual): ")
        novo_email = input("Digite o novo e-mail (ou pressione Enter para manter o atual): ")

        # Mantém os valores atuais se o usuário não fornecer novas entradas
        if novo_telefone:
            contatos[nome]['telefone'] = novo_telefone
        if novo_email:
            contatos[nome]['email'] = novo_email

        salvar_contatos(contatos)
        print(f"Contato {nome} atualizado com sucesso!")
    else:
        print(f"Contato {nome} não encontrado.")
        
def excluir_contato():
    nome = input("Digite o nome do contato que deseja excluir: ")

    if nome in contatos:
        del contatos[nome]
        salvar_contatos(contatos)
        print(f"Contato {nome} excluído com sucesso!")
    else:
        print(f"Contato {nome} não encontrado.")

def favoritar_contato():
    nome = input("Digite o nome do contato que deseja favoritar: ")

    if nome in contatos:
        contatos[nome]['favorito'] = True
        salvar_contatos(contatos)
        print(f"Contato {nome} marcado como favorito!")
    else:
        print(f"Contato {nome} não encontrado.")

def desfavoritar_contato():
    nome = input("Digite o nome do contato que deseja desfavoritar: ")

    if nome in contatos:
        contatos[nome]['favorito'] = False
        salvar_contatos(contatos)
        print(f"Contato {nome} removido dos favoritos!")
    else:
        print(f"Contato {nome} não encontrado.")

def menu():
    while True:
        print("\n1. Adicionar Contato")
        print("\n2. Listar Contatos")
        print("\n3. Editar Contato")
        print("\n4. Favoritar Contato")
        print("\n5. Desfavoritar Contato")
        print("\n6. Listar Favoritos")
        print("\n7. Excluir Contato")
        print("\n8. Sair")
        escolha = input("\nEscolha uma opção: ")

        if escolha == '1':
            adicionar_contato()
        elif escolha == '2':
            listar_contatos()
        elif escolha == '3':
            editar_contato()
        elif escolha == '4':
            favoritar_contato()
        elif escolha == '5':
            desfavoritar_contato()
        elif escolha == '6':
            listar_favoritos()
        elif escolha == '7':
            excluir_contato()
        elif escolha == '8':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")

contatos = carregar_contatos()
menu()