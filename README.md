# Mini To-Do List (terminal)

CRUD simples de tarefas com menu interativo. As tarefas ficam guardadas numa
lista em memória (`tarefas`) — ou seja, ao fechar o programa, tudo se perde
(não salva em arquivo nem banco).

## Estrutura de uma tarefa

Cada tarefa é um dicionário:

```python
{"descricao": "Estudar SQL", "concluida": False}
```

## Funções

- `adicionar_tarefa()`: pede a descrição e adiciona à lista.
- `listar_tarefas()`: mostra todas as tarefas numeradas, com `[X]` para
  concluídas e `[ ]` para pendentes.
- `marcar_como_concluida()`: lista as tarefas, pede um número e marca
  `concluida = True`.
- `remover_tarefa()`: lista as tarefas, pede um número e remove da lista.
- `pedir_numero_tarefa()`: função auxiliar que valida a entrada do usuário
  (evita `IndexError` se digitar um número fora da lista, ou erro se digitar
  texto em vez de número).

## Como executar

```bash
python3 todo.py
```

Exemplo de uso:

```
===== MENU =====
1. Adicionar tarefa
2. Listar tarefas
3. Marcar tarefa como concluída
4. Remover tarefa
5. Sair
Escolha uma opção: 1
Descrição da tarefa: Estudar SQL
Tarefa adicionada!
```

## Possíveis melhorias futuras
- Salvar as tarefas em um arquivo (`.json` ou `.txt`) para não perder ao sair.
- Adicionar prazos ou prioridades para cada tarefa.
