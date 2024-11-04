import matplotlib.pyplot as plt

dias_da_semana = ['Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo']
quantidade_resgatados = [5, 8, 6, 7, 10, 12, 4]

plt.figure(figsize=(10, 6))
plt.bar(dias_da_semana, quantidade_resgatados, color='skyblue')

plt.title('Quantidade de Animais Resgatados Durante a Semana')
plt.xlabel('Dias da Semana')
plt.ylabel('Quantidade de Animais Resgatados')

plt.show()

# APLICAÇÃO SEM CONEXÃO COM O BANCO DE DADOS