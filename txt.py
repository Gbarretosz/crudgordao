nome = str(input('Digite seu nome: '))
idade = (input('Digite sua idade: '))


with open ('nomes.txt', 'w') as arquivo:
    arquivo.write(nome)

with open ('idades.txt', 'w') as arquivo:
    arquivo.write(idade)

with open('nomes.txt', 'r') as arquivo:
    nomes = arquivo.read()
print(nomes)

with open('idades.txt', 'r') as arquivo:
    idades = arquivo.read()
print(f'{idades} anos')

cname = 1
oidade = 2
nada = 3
cname = str(input('Você deseja mudar alguma coisa?\n1-Nome \n2-Idade\n3-Nada\n->'))

if cname ==  'nome':
    othername = str(input('Digite outro nome: '))
    with open ('nomes.txt', 'w') as arquivo:
        arquivo.write (othername)
elif cname == 'idade':
    oidade = str(input('Digite outra idade:'))
    with open('idades.txt', 'w') as arquivo:
        arquivo.write(oidade)

with open('nomes.txt', 'r') as arquivo:
    nomes = arquivo.read()
print(nomes)

with open('idades.txt', 'r') as arquivo:
    idades = arquivo.read()
print(f'{idades} anos')
