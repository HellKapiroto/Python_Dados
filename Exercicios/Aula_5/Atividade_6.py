qtd_alunos = 29
capacidade_grupos = 4
grupos = qtd_alunos // capacidade_grupos
sobra = qtd_alunos % capacidade_grupos
print(f'A quantidade de grupos inteiros é {grupos} e sobram {sobra} alunos')