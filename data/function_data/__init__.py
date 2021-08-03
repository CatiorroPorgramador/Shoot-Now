'''
linha 1: moedas
linha 2: kills totais
linha 3: lista de itens (kits médicos)
linha 4: indice de background (quantos vc tem)
linha 5: indice de background (selecionado)
	
'''
def read(file):
	pass

def write():
	values = open("qbdata.txt", "r").readlines()
	new_values = open("qbdata.txt", "w")

	new_values.close()

def vec():
	try:
		write()

	except:
		FILE = open("qbdata.txt", "wt+")

		FILE.close()

		write()

vec()

