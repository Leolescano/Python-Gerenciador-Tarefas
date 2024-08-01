tarefas = []
def adicionar_tarefa(nome_tarefa: str = "tarefa padrão", tarefas: list = tarefas) -> None:
    tarefa = {
        "nome": nome_tarefa,
        "completada": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    return

while True:
    print("\nMenu do Gerenciador de Lista de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Actualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair do programa")

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar:\n")
        adicionar_tarefa(nome_tarefa, tarefas)
    elif escolha == "6":
        break

print("Programa finalizado")


