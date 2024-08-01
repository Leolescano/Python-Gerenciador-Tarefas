from classe_Tarefa import Tarefa

def mostrar_menu()-> None:
    print("\nMenu do Gerenciador de Lista de Tarefas")
    print("1. Adicionar tarefa")
    print("2. Ver tarefas")
    print("3. Actualizar tarefa")
    print("4. Completar tarefa")
    print("5. Deletar tarefas completadas")
    print("6. Sair do programa")

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
        nome_tarefa: str = tarefa["nome"] 
        print(f"{i}. [{status}] {nome_tarefa}")
        
def atualizar_nome_tarefa(tarefas: list[Tarefa], indice_tarefa: int, novo_nome: str)-> None: 
    if indice_tarefa > 0 and indice_tarefa <= len(tarefas):
        tarefas[indice_tarefa - 1]["nome"] = novo_nome
        print(f"Tarefa {indice_tarefa} atualizada para {novo_nome}")
    else:
        print("Índice de tarefa invalido.")