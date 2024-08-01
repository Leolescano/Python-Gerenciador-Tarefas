from classe_Tarefa import Tarefa
from funcoes import *

tarefas: list[Tarefa] = []

while True:
    mostrar_menu()

    escolha = input("Digite a sua escolha: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa que deseja adicionar:\n")
        adicionar_tarefa(nome_tarefa, tarefas)
    elif escolha == "2":
        ver_tarefas(tarefas)
    elif escolha == "3":
        ver_tarefas(tarefas)
        indice_tarefa = int (input("Digite o número da tarefa que deseja atualizar: "))
        novo_nome: str = input("Digite o novo nome da tarefa: ")
        atualizar_nome_tarefa(tarefas, indice_tarefa, novo_nome)
    elif escolha == "4":
        ver_tarefas(tarefas)
        indice_tarefa = int (input("Digite o número da tarefa que deseja completar: "))
        completar_tarefa(tarefas, indice_tarefa)
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        ver_tarefas(tarefas)
    elif escolha == "6":
        break

print("Programa finalizado")


