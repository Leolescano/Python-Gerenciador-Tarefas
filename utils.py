from classe_Tarefa import Tarefa

def validar_indice(tarefas: list[Tarefa], indice_tarefa: int) -> Tarefa | None:
    if 0 < indice_tarefa <= len(tarefas):
        return tarefas[indice_tarefa - 1]
    else:
        print("Índice de tarefa inválido.")
        return None