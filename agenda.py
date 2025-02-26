import sys
#A aplicação deve iniciar mostrando uma lista de opções do que é possível fazer com o app e permitir 
# que o usuário digite uma escolha para iniciar a aplicação.
# Deve ser possível adicionar um contato checked
    #O contato pode ter os dados:
    #Nome checked
    # Telefone checked
    # Email checked
    # Favorito (está opção é para poder marcar um contato como favorito)
# Deve ser possível visualizar a lista de contatos cadastrados checked
# Deve ser possível editar um contato checked
# Deve ser possível marcar/desmarcar um contato como favorito checked
# Deve ser possível ver uma lista de contatos favoritos checked
# Deve ser possível apagar um contato

contatos = {}

def menu():
    print("Menu:")
    print("1. Adicionar Contato")
    print("2. Vizualizar Contatos")
    print("3. Vizualizar Contatos Favoritos")
    print("4. Apagar contatos")
    print("5. Sair")

def add_contato():
    while True:
       nome = input("Nome:").strip()
       telefone = input("Telefone:").strip()
       email = input("E-mail:").strip()
       
       contatos[nome] = {
           "nome": nome,
           "telefone": telefone,
           "email": email,
           "favorito": False
       }

       sair = input("Deseja adicionar outro contato? (s/n):").strip().lower()
       if sair == "n":
           break # Sai do loop


def vizualizar_contato():
    print(contatos)
    while True:
        behold = input("Deseja editar algum contato? (s/n):").strip().lower()
        if behold == "s":
            nomePesquisa = input("Digite o nome do contato que deseja editar: ").strip()
            if nomePesquisa in contatos:
                print(f"Nome atual: {contatos[nomePesquisa]['nome']}")
                novo_nome = input("Novo nome (pressione Enter para manter o mesmo): ").strip()

                print(f"Telefone atual: {contatos[nomePesquisa]['telefone']}")
                novo_telefone = input("Novo telefone (pressione Enter para manter o mesmo): ").strip()

                print(f"E-mail atual: {contatos[nomePesquisa]['email']}")
                novo_email = input("Novo e-mail (pressione Enter para manter o mesmo): ").strip()

                if novo_nome:
                    contatos[novo_nome] = contatos.pop(nomePesquisa)
                    nomePesquisa = novo_nome

                if novo_telefone:
                    contatos[nomePesquisa]["telefone"] = novo_telefone
                
                if novo_email:
                    contatos[nomePesquisa]["email"] = novo_email
                
                print("contato atualizado com sucesso")



            else:
                print("Contato não encontrado.")
        else:
            break

def vizualizar_Favoritos():
    print("DEBUG - Contatos salvos:", contatos)
    favoritos = {nome: dados for nome, dados in contatos.items() if dados["favorito"]}

    if not favoritos:
        print("Nenhum contato favorito")
        favoritar = input("Deseja favoritar algum? (s/n):")
        if favoritar == "s":
            nome = input("Digite o nome do contato").strip()

            if nome in contatos:
                contatos[nome]["favorito"] = not contatos[nome]["favorito"]
                status = "favorito" if contatos[nome]["favorito"] else "não favorito"
                print(f"O contato {nome} agora é {status}.")
            else:
                print("contato não encontrado.")
        return
    
    print("\nLista de Contatos Favoritos:")
    for nome, dados in favoritos.items():
        print(f"⭐ Nome: {dados['nome']}, Telefone: {dados['telefone']}, Email: {dados['email']}")
    
    favoritar = input("Deseja favoritar/desfavoritar algum? (s/n):")
    if favoritar == "s":
        nome = input("Digite o nome do contato").strip()

        if nome in contatos:
            contatos[nome]["favorito"] = not contatos[nome]["favorito"]
            status = "favorito" if contatos[nome]["favorito"] else "não favorito"
            print(f"O contato {nome} agora é {status}.")
        else:
            print("contato não encontrado.")
    return

def apagar_contato():
    while True:
        begone = input("Deseja apagar algum contato? (s/n): ").strip().lower()
        if begone == "s":
            nomePesquisa = input("Digite o nome do contato que deseja apagar: ").strip()
            if nomePesquisa in contatos:
                contatos.pop(nomePesquisa)  # Corrigido o uso do nome da variável
                print(f"Contato {nomePesquisa} apagado com sucesso.")
            else:
                print("Contato não identificado.")
        else:
            break  # Sai do loop se o usuário não quiser apagar mais contatos

    

                


def main():
    while True:
        menu()
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            add_contato()
        elif opcao == "2":
            vizualizar_contato()
        elif opcao == "3":
            vizualizar_Favoritos()
        elif opcao == "4":
            apagar_contato()
        elif opcao == "5":
            sys.exit()
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
