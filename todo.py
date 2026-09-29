"""
Mini To-Do List no terminal.
CRUD simples de tarefas guardadas em uma lista em memória (some quando o
programa fecha).
"""

tarefas = []  # cada tarefa é um dicionário: {"descricao": str, "concluida": bool}


def adicionar_tarefa():
    descricao = input("Descrição da tarefa: ").strip()
    if not descricao:
        print("A descrição não pode ser vazia.")
        return

    tarefas.append({"descricao": descricao, "concluida": False})
    print("Tarefa adicionada!")


def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n--- Lista de tarefas ---")
    for indice, tarefa in enumerate(tarefas):
        status = "[X]" if tarefa["concluida"] else "[ ]"
        print(f"{indice + 1}. {status} {tarefa['descricao']}")


def marcar_como_concluida():
    listar_tarefas()
    if not tarefas:
        return

    numero = pedir_numero_tarefa()
    if numero is None:
        return

    tarefas[numero]["concluida"] = True
    print("Tarefa marcada como concluída!")


def remover_tarefa():
    listar_tarefas()
    if not tarefas:
        return

    numero = pedir_numero_tarefa()
    if numero is None:
        return

    tarefa_removida = tarefas.pop(numero)
    print(f"Tarefa removida: {tarefa_removida['descricao']}")


def pedir_numero_tarefa():
    """Pede o número de uma tarefa da lista e devolve o índice (0-based)."""
    entrada = input("Número da tarefa: ").strip()

    if not entrada.isdigit():
        print("Digite um número válido.")
        return None

    numero = int(entrada) - 1
    if numero < 0 or numero >= len(tarefas):
        print("Número fora da lista.")
        return None

    return numero


def mostrar_menu():
    print("\n===== MENU =====")
    print("1. Adicionar tarefa")
    print("2. Listar tarefas")
    print("3. Marcar tarefa como concluída")
    print("4. Remover tarefa")
    print("5. Sair")


def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_tarefa()
        elif opcao == "2":
            listar_tarefas()
        elif opcao == "3":
            marcar_como_concluida()
        elif opcao == "4":
            remover_tarefa()
        elif opcao == "5":
            print("Até mais!")
            break
        else:
            print("Opção inválida. Escolha um número de 1 a 5.")


if __name__ == "__main__":
    main()
