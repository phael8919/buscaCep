# buscaCep
Descrição: Script Python para buscar o endereço pelo número do Cep

- Passo 01: Para realizar essa tarefa, primeiro são importados as bibliotecas "requests" e "json".

Obs.: No Jupyter Notebook a biblioteca "requests" é importada normalmente, todavia pode ser necessário instalá-la manualmente no VsCode ou PyCharm.

Passo 01: Para realizar essa tarefa, primeiro são importados as bibliotecas "requests" e "json".

Obs.: No Jupyter Notebook a biblioteca "requests" é importada normalmente, todavia pode ser necessário instalá-la manualmente no VsCode ou PyCharm.

- Passo 02: É criada a função buscaCep( ) e, dentro dela, são usadas as palavras reservadas "try" para executar o código caso esse não apresente algum erro, e "except" que exibe uma mensagem caso algum erro ocorra.

- Passo 03: A variável "cep" exibe um input em que o usuário digita o nº do CEP

cep = input('Digite o cep: ')

- Passo 04: Na variável "url" é feita a captura da consulta do cep concatenando a url da API dos Correios com o CEP pesquisado. Para isso é utilizada biblioteca "requests" para buscar a consulta.

url = requests.get('https://viacep.com.br/ws/'+cep+'/json/').content


- Passo 05: A variável "dic" utiliza a biblioteca "json" para carregar a consulta no formato de dicionário.

dic = json.loads(url)

- Passo 06: Por fim, o resultado da consulta é exibida, demonstrando o logradouro, bairro, cidade e UF:

print(f'Logradouro: {dic["logradouro"]}'
      print(f'Bairro: {dic["bairro"]}')  
      print(f'Cidade: {dic["localidade"]}')
      print(f'UF: {dic["uf"]}'))
      
## Busca endereço pelo CEP - Interface Gráfica
No arquivo "cep_endereco.py", uma janela é exibida para o usuário digitar o número de CEP e o endereço é exibido.
