while True:
	
	menu = int(input("""
 Digite oque deseja
 1- Criar 
 2- Ler  
 3- Atualizar 
 0- Sair
 -> """))
	if menu == 0:
		break
		
	elif menu == 1:
		nome = str(input('Digite seu nome: '))
		idade = (input('Digite sua idade: '))
		with open ('pessoas.txt', 'a') as arquivo:
			arquivo.write(f" {nome} {idade} anos\n")
			
	elif menu == 2:
		with open('pessoas.txt', 'r') as arquivo:
			pessoas = arquivo.readlines()
		for pessoa in pessoas:
			print(f"{pessoa}", end="")
			
	elif menu == 3:
		
