from tkinter import * #Importa a GUI
from tkinter import messagebox
import requests #Captura a URL
import json #Exibe o conteúdo do json

tela = Tk()
tela.title('Busca de Endereço pelo CEP')

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
        messagebox.showerror(title='Mensagem de erro', message='Verifique o CEP digitado')
        

rotulo = Label(tela, text='    Digite o CEP: ', font='Arial 15')
rotulo.grid(row=0, column=1, sticky = 'W', pady = 2, padx=2)

entrada = Entry(tela, font='Arial 15')
entrada.grid(row=0, column=2, sticky = W, pady = 2, padx=2)

botao = Button(tela, text='Clique aqui', font='Arial 15', command=buscaCep)
botao.grid(row=0, column=3, sticky = 'W', pady = 2, padx=2)

rotulo1 = Label(tela, text='', font='Arial 15')
rotulo1.grid(row=1, column=1, sticky = 'W', pady = 4, padx=2)

rotulo2 = Label(tela, text='', font='Arial 15')
rotulo2.grid(row=1, column=2, sticky = 'W', pady = 4, padx=2)

rotulo3 = Label(tela, text='', font='Arial 15')
rotulo3.grid(row=2, column=1, sticky = 'W', pady = 4, padx=2)

rotulo4 = Label(tela, text='', font='Arial 15')
rotulo4.grid(row=2, column=2, sticky = 'W', pady = 4, padx=2)

tela.geometry('650x150')
tela.mainloop()