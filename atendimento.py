import os # Biblioteca para limpar a tela e ficar organizado

fila_geral = [] # Aqui vamos guardar o nome e o tipo do serviço
historico = []

while True:
    # Este comando limpa o terminal para parecer um sistema de verdade
    os.system('cls' if os.name == 'nt' else 'clear')

    print("========================================")
    print("   CENTRAL DE ATENDIMENTO SENAI GAMA    ")
    print("========================================")
    
    # Visualização do Painel (Item 4.c.ii)
    print("\n--- ÚLTIMOS CHAMADOS ---")
    if len(historico) >= 1: print(f" 1º: {historico[-1]}")
    if len(historico) >= 2: print(f" 2º: {historico[-2]}")
    
    print("\n--- MENU ---")
    print("1 - Retirar Senha")
    print("2 - Chamar Próximo")
    print("3 - Pular/Desistência (Item 4.b.iii)")
    print("0 - Sair")

    opcao = input("\nEscolha: ")

    if opcao == "1":
        nome = input("Nome do Cliente: ")
        print("SERVIÇOS: (C)onvencional, (P)rioritário, (M)atrícula, (I)nformação")
        servico = input("Tipo de Serviço: ").upper()
        
        # Guardamos como um 'dicionário' para saber quem é quem
        cliente = {"nome": nome, "tipo": servico}
        
        # Se for Prioritário, entra na frente de todo mundo (Item 4.b.iv)
        if servico == "P":
            fila_geral.insert(0, cliente)
        else:
            fila_geral.append(cliente)
        print(f"\nSenha gerada para {nome}!")

    elif opcao == "2":
        if fila_geral:
            atendido = fila_geral.pop(0)
            chamada_texto = f"{atendido['nome']} [{atendido['tipo']}]"
            print(f"\n>>> CHAMANDO: {chamada_texto} <<<")
            historico.append(chamada_texto)
            input("\nPresione Enter para finalizar o atendimento...") # Simula a execução (3.d)
        else:
            print("\nFila vazia!")
            input("\nEnter para voltar...")

    elif opcao == "3":
        if fila_geral:
            desistente = fila_geral.pop(0)
            print(f"\nCliente {desistente['nome']} removido (Desistência).")
        else:
            print("\nNinguém para remover.")
        input("\nEnter para voltar...")

    elif opcao == "0":
        break