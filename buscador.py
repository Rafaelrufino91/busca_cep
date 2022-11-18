import requests
from tkinter import *

class main:
    def __init__(self, master=None):
        self.resultado = Frame(master)
        self.resultado["pady"] = 5
        self.resultado.pack()

        self.tela = Frame(master)
        self.tela.pack()

        self.titulo = Label(self.tela, text='Digite o cep')
        self.titulo.pack()

        self.cep = Entry(self.tela)
        self.cep["width"] = 12
        self.cep.pack()

        self.pesquisar = Button(self.tela)
        self.pesquisar["text"] = "Pesquisar"
        self.pesquisar["command"] = self.ConsultaCep
        self.pesquisar.pack()

        self.msg = Label(self.resultado, text="", font="Arial")
        self.msg.pack()
    
    #metodo consulta cep
    def ConsultaCep(self):
        cep_corrigido = ''
        cep = self.cep.get()
        for l in cep:
            if l.isnumeric():
                cep_corrigido += l
        while True:
            if len(cep_corrigido) < 8:
                cep_corrigido += '0'
            elif len(cep_corrigido) == 8:
                break
        try:
            requisicao = requests.get(f'http://viacep.com.br/ws/{cep_corrigido}/json/')
            endereco = requisicao.json()
            if cep:
                rua = endereco['logradouro']
                uf = endereco['uf']
                cidade = endereco['localidade']
                self.msg["text"] = rua+uf+cidade
        except KeyError:
            self.msg["text"] = "Cep não encontrado ou inválido"

root = Tk()
main(root)
root.mainloop()
