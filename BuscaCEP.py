import requests #Captura a URL
import json #Exibe o conteúdo do json

def buscaCep():
    try:
        #Caixa de diálogo para digitar o cep
        cep = input('Digite o cep: ')

        #Fazendo requisiçao a API dos Correios pela url e capturando o conteúdo da busca
        url = requests.get('https://viacep.com.br/ws/'+cep+'/json/').content

        #Exibe o dicionário
        dic = json.loads(url)    
       
        #Exibe o endereço completo de acordo com o cep
        print(f'Logradouro: {dic["logradouro"]}')
        print(f'Bairro: {dic["bairro"]}')  
        print(f'Cidade: {dic["localidade"]}')
        print(f'UF: {dic["uf"]}')
    except:
        print('Verifique se o cep foi digitado corretamente e tente novamente')

buscaCep()