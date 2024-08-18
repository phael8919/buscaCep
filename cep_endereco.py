from tkinter import * #Importa a GUI
from tkinter import messagebox #Exibe uma mensagem de erro caso o cep não seja localizado
import requests #Captura a URL
import json #Exibe o conteúdo do json

tela = Tk()
tela.title('Busca de Endereço pelo CEP')

#Função para capturar o endereço via API
def buscaCep():
    try:
        cep = entrada.get()
    
        #Fazendo requisiçao a API dos Correios pela url e capturando o conteúdo da busca
        url = requests.get('https://viacep.com.br/ws/'+cep+'/json/').content
    
        #Exibe o dicionário
        dic = json.loads(url) 
        
        rotulo1['text'] = f'    Logradouro: {dic["logradouro"]}'
        rotulo2['text'] = f'Bairro: {dic["bairro"]}'
        rotulo3['text'] = f'    Cidade: {dic["localidade"]}'
        rotulo4['text'] = f'UF: {dic["uf"]}'
    except:
        messagebox.showerror(title='Mensagem de erro', message='Verifique o CEP digitado!')
        

rotulo = Label(tela, text='Digite o CEP: ', font='Arial 15', width=45)
rotulo.grid(row=0, column=1, sticky = 'W', pady = 20, padx=10)

#Input para receber o nº do CEP
entrada = Entry(tela, font='Arial 15', width=45)
entrada.grid(row=0, column=2, sticky = W, pady = 20, padx=10)

#Botão para executar a função que busca o CEP
botao = Button(tela, text='Clique aqui', font='Arial 15', command=buscaCep)
botao.grid(row=1,column=1, pady=10, padx=10, sticky='NSEW', columnspan=2)

#Grupo de rótulos que exibem o endereço do CEP buscado
rotulo1 = Label(tela, text='', font='Arial 15')
rotulo1.grid(row=2, column=1, sticky = 'W', pady = 8)

rotulo2 = Label(tela, text='', font='Arial 15')
rotulo2.grid(row=2, column=2, sticky = 'W', pady = 8)

rotulo3 = Label(tela, text='', font='Arial 15')
rotulo3.grid(row=3, column=1, sticky = 'W', pady = 8)

rotulo4 = Label(tela, text='', font='Arial 15')
rotulo4.grid(row=3, column=2, sticky = 'W', pady = 8)

#Tamanho da tela
tela.geometry('1045x250')
tela.mainloop()