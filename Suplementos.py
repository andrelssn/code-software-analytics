import matplotlib.pyplot as plt

dias_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
quantidade_racao = [20, 35, 30, 25, 40, 50, 45]
quantidade_suplementos = [5, 10, 8, 7, 12, 15, 10]

plt.figure(figsize=(10, 6))
plt.bar(dias_da_semana, quantidade_racao, color='lightgreen', label='Ração')
plt.bar(dias_da_semana, quantidade_suplementos, bottom=quantidade_racao, color='orange', label='Suplementos')

plt.title('Quantidade de Ração e Suplementos Arrecadados Durante a Semana')
plt.xlabel('Dias da Semana')
plt.ylabel('Quantidade Arrecadada')
plt.legend()

plt.show()

# APLICAÇÃO SEM CONEXÃO COM O BANCO DE DADOS