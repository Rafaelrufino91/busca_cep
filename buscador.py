import requests

print('='*50)
cep_corrigido = ''
cep = str(input('Digite o cep que deseja: ')).strip()
print('='*50)
for l in cep:
    if l.isnumeric():
        cep_corrigido += l

while True:
    if len(cep_corrigido) < 8:
        cep_corrigido += '0'
    elif len(cep_corrigido) == 8:
        break

try:
    print(f'O cep digitado foi: {cep_corrigido}')
    requisicao = requests.get(f'http://viacep.com.br/ws/{cep_corrigido}/json/')
    endereco = requisicao.json()
    rua = endereco['logradouro']
    uf = endereco['uf']
    cidade = endereco['localidade']
    print(f'{rua}, {cidade} - {uf}')
except KeyError:
    print('Cep não encontrado ou inválido')
