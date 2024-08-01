from classe_Tarefa import Tarefa

tarefas: list[Tarefa] = []

def adicionar_tarefa(nome_tarefa: str = "tarefa padrão", tarefas: list[Tarefa] = None) -> None:
    tarefa: Tarefa  = {
        "nome": nome_tarefa,
        "completada": False
    }
    tarefas.append(tarefa)
    print(f"Tarefa {nome_tarefa} foi adicionada com sucesso!")
    
def ver_tarefas(tarefas: list[Tarefa]) -> None:
    print("\nLista de tarefas") 
    for i, tarefa in enumerate(tarefas, start = 1):
        status: str = "✓" if tarefa["completada"] == True else ""
        nome_tarefa: str = tarefa['nome'] 
        print(f"{i}. [{status}] {nome_tarefa}")
        
while True:
    print("\nMenu do Gerenciador de Lista de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Actualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair do programa")

    escolha: str = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefa : str = input("Digite o nome da tarefa que deseja adicionar:\n")
        adicionar_tarefa(nome_tarefa, tarefas)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "6":
        break

print("Programa finalizado")


