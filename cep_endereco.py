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

        rotuloA['text'] = 'Logradouro'
        rotuloB['text'] = 'Bairro'
        rotuloC['text'] = 'Cidade'
        rotuloD['text'] = 'Estado'
        
        rotulo1['text'] = dic["logradouro"]
        rotulo2['text'] = dic["bairro"]
        rotulo3['text'] = dic["localidade"]
        rotulo4['text'] = dic["uf"]
    except:
        messagebox.showerror(title='Mensagem de erro', message='Verifique o CEP digitado!')
        

rotulo = Label(tela, text='Digite o CEP: ', font='Arial 15', width=30)
rotulo.grid(row=0, column=1, sticky = 'W', pady = 20, padx=10)

#Input para receber o nº do CEP
entrada = Entry(tela, font='Arial 15', width=30)
entrada.grid(row=0, column=2, sticky = W, pady = 20, padx=10)

#Botão para executar a função que busca o CEP
botao = Button(tela, text='Clique aqui', font='Arial 15', command=buscaCep)
botao.grid(row=1,column=1, pady=10, padx=10, sticky='NSEW', columnspan=2)

#Grupo de rótulos que exibem o endereço do CEP buscado
rotuloA = Label(tela, text='', font='Arial 15 bold')
rotuloA.grid(row=2, column=1, sticky = 'W', padx =7)
rotuloB = Label(tela, text='', font='Arial 15 bold')
rotuloB.grid(row=2, column=2, sticky = 'W', padx = 7)

rotulo1 = Label(tela, text='', font='Arial 15')
rotulo1.grid(row=3, column=1, sticky = 'W', pady = 8, padx = 7)

rotulo2 = Label(tela, text='', font='Arial 15')
rotulo2.grid(row=3, column=2, sticky = 'W', pady = 8, padx = 7)

rotuloC = Label(tela, text='', font='Arial 15 bold')
rotuloC.grid(row=4, column=1, sticky = 'W', padx = 7)
rotuloD = Label(tela, text='', font='Arial 15 bold')
rotuloD.grid(row=4, column=2, sticky = 'W', padx = 7)

rotulo3 = Label(tela, text='', font='Arial 15')
rotulo3.grid(row=5, column=1, sticky = 'W', pady = 8, padx = 7)

rotulo4 = Label(tela, text='', font='Arial 15')
rotulo4.grid(row=5, column=2, sticky = 'W', pady = 8, padx = 7)

#Tamanho da tela
tela.geometry('715x300')
tela.mainloop()