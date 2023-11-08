# Importa o Módulo Requests para Fazer Requisições HTTP (Avá é Mesmo?)
import requests as req

# Caso Você Troucou a Porta no Outro Código Favor Mudar Aqui Também. Desde já Agradecido
port = 7620
link = f'http://localhost:{port}/http/response'

# Lógica do Testador Parte 2
for i in range(100, 999):
	conclue = False
	try:
		require = req.get(f'{link}/{i}')
		conclue = True
	except:
		require = req.get('https://google.com')

	if conclue == True:
		if require.reason == 'unknown':
			pass
		else:
			print(f'{i}:')
			print(require.reason)
			print(' ')

# Favor Ligar O Outro Código Antes Desse

# Nota do Escritor Fiz o Testador em Python Devido Preguiça
