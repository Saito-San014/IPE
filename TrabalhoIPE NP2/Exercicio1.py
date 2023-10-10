import random
import json
from pathlib import Path
import random
from tkinter import *
from tkinter import ttk

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

file_path = Path(r"C:/Users/gabil/OneDrive/Área de Trabalho/IPE/TrabalhoIPE NP2/JSON/produtos.json")

with open(file_path, encoding="utf8") as openfile:
    # Reading from json file
    JsonFile = json.load(openfile)
produtosJson = JsonFile['produtos']

class Produto:
    def __init__(self, codigo, nome, estoque, estoqueMin, estoqueMax, precoCusto, precoVenda, icms, ipi):
       self.codigo = codigo
       self.nome = nome
       self.estoque = estoque
       self.estoqueMin = estoqueMin
       self.estoqueMax = estoqueMax
       self.precoCusto = precoCusto
       self.precoVenda = precoVenda
       self.icms = icms
       self.ipi = ipi
def genereteFakersObject(quant):
    produtos = []
    while(len(produtos) != quant):
        cod = random.randint(1,len(produtosJson))
        nome = produtosJson[cod]['nome']
        estoqueMin = random.randint(1,100)
        estoqueMax = random.randint(estoqueMin,300)
        estoque = random.randint(estoqueMin,estoqueMax)
        precoCusto = random.uniform(produtosJson[cod]['faixa_de_preco'][0],produtosJson[cod]['faixa_de_preco'][1])
        precoVenda = random.uniform(precoCusto,produtosJson[cod]['faixa_de_preco'][1])
        icms = random.randint(0,50)
        ipi = random.randint(1,len(produtosJson))
        if(len(produtos)> 0):
            sair = True
            while(sair):
                for i, pro  in enumerate(produtos):
                    if pro.codigo == cod:
                        cod = random.randint(1,len(produtosJson))
                        break
                    if i+1 == len(produtos):
                        sair = False
            
        produto = Produto(cod, nome, estoque, estoqueMin, estoqueMax, precoCusto, precoVenda, icms, ipi)
        produtos.append(produto)
    return produtos
produtos = genereteFakersObject(10)
produtoMaiorPreco =  Produto(0,"",0,0,0,0,0,0,0) 
produtoMenorPreco =  Produto(0,"",0,0,0,0,0,0,0)
produtoMaiorEstoque =  Produto(0,"",0,0,0,0,0,0,0)
produtoMenorEstoque =  Produto(0,"",0,0,0,0,0,0,0)
produtoMaiorICMS =  Produto(0,"",0,0,0,0,0,0,0)
produtoMenorICMS =  Produto(0,"",0,0,0,0,0,51,0)
produtoMaiorLucro =  Produto(0,"",0,0,0,0,0,0,0)
produtoMenorLucro =  Produto(0,"",0,0,0,0,0,0,0)
for pro in produtos:
    if pro.precoVenda > produtoMaiorPreco.precoVenda:
        produtoMaiorPreco = pro
    if pro.precoVenda < produtoMenorPreco.precoVenda or produtoMenorPreco.precoVenda == 0:
        produtoMenorPreco = pro
    if pro.estoque > produtoMaiorEstoque.estoque:
        produtoMaiorEstoque = pro
    if pro.estoque < produtoMenorEstoque.estoque or produtoMenorEstoque.estoque == 0:
        produtoMenorEstoque = pro
    if pro.icms > produtoMaiorICMS.icms:
        produtoMaiorICMS = pro
    if pro.icms < produtoMenorICMS.icms and pro.icms > 0 or produtoMenorICMS.codigo == 0:
        produtoMenorICMS = pro
    if pro.precoVenda - pro.precoCusto > produtoMaiorLucro.precoVenda - produtoMaiorLucro.precoCusto:
        produtoMaiorLucro = pro
    if pro.precoVenda - pro.precoCusto < produtoMenorLucro.precoVenda - produtoMenorLucro.precoCusto or produtoMenorLucro.codigo == 0:
        produtoMenorLucro = pro
fontType = "Arial"
fontSize = 15
titulos = [
    "Produto de maior preço",
    "Produto de menor preço",
    "Produto com o maior estoque",
    "Produto com o menor estoque",
    "Produto com o maior ICMS",
    "Produto com o menor ICMS > 0",
    "Produto com o maior lucro",
    "Produto com o menor lucro"
    ]
#For para os Labels dos titulos
for x, titulo in enumerate(titulos):
    Label(frm, text=titulo,font=(fontType, fontSize),borderwidth=2, relief="groove", height=2, width=30, anchor="center").grid(column=0, row=x)
#Labels para o produto com o maior preço
Label(frm, text=produtoMaiorPreco.nome,font=(fontType, fontSize),borderwidth=2, relief="groove", height=2, width=30, anchor="center").grid(column=1, row=0)
Label(frm, text=f"{produtoMaiorPreco.precoVenda:.2f}R$",font=(fontType, fontSize),borderwidth=2, relief="groove", height=2, width=30, anchor="center").grid(column=2, row=0)
#Laels para o produto com o menor preço
Label(frm, text=produtoMenorPreco.nome,font=(fontType, fontSize),borderwidth=2, relief="groove", height=2, width=30, anchor="center").grid(column=1, row=1)
Label(frm, text=f"{produtoMenorPreco.precoVenda:.2f}R$",font=(fontType, fontSize),borderwidth=2, relief="groove", height=2, width=30, anchor="center").grid(column=2, row=1)
#Labels para o produto com o maior estoque
Label(frm, text=produtoMaiorEstoque.nome,font=(fontType, fontSize),borderwidth=2, relief="groove", height=2, width=30, anchor="center").grid(column=1, row=2)
Label(frm, text=produtoMaiorEstoque.estoque,font=(fontType, fontSize),borderwidth=2, relief="groove", height=2, width=30, anchor="center").grid(column=2, row=2)
#Labels para o produto com o menor estoque
Label(frm, text=produtoMenorEstoque.nome,font=(fontType, fontSize),borderwidth=2, relief="groove", height=2, width=30, anchor="center").grid(column=1, row=3)
Label(frm, text=produtoMenorEstoque.estoque,font=(fontType, fontSize),borderwidth=2, relief="groove", height=2, width=30, anchor="center").grid(column=2, row=3)
#Labels para o produto com o maior ICMS
Label(frm, text=produtoMaiorICMS.nome,font=(fontType, fontSize),borderwidth=2, relief="groove", height=2, width=30, anchor="center").grid(column=1, row=4)
Label(frm, text=f"{produtoMaiorICMS.icms}%",font=(fontType, fontSize),borderwidth=2, relief="groove", height=2, width=30, anchor="center").grid(column=2, row=4)
#Labels para o produto com o menor ICMS > 0
Label(frm, text=produtoMenorICMS.nome,font=(fontType, fontSize),borderwidth=2, relief="groove", height=2, width=30, anchor="center").grid(column=1, row=5)
Label(frm, text=f"{produtoMenorICMS.icms}%",font=(fontType, fontSize),borderwidth=2, relief="groove", height=2, width=30, anchor="center").grid(column=2, row=5)
#Labels para o produto com o maior lucro
Label(frm, text=produtoMaiorLucro.nome,font=(fontType, fontSize),borderwidth=2, relief="groove", height=2, width=30, anchor="center").grid(column=1, row=6)
Label(frm, text=f"{(produtoMaiorLucro.precoVenda - produtoMaiorLucro.precoCusto):.2f}R$",font=(fontType, fontSize),borderwidth=2, relief="groove", height=2, width=30, anchor="center").grid(column=2, row=6)
#Labels para o produto com o menor lucro
Label(frm, text=produtoMenorLucro.nome,font=(fontType, fontSize),borderwidth=2, relief="groove", height=2, width=30, anchor="center").grid(column=1, row=7)
Label(frm, text=f"{(produtoMenorLucro.precoVenda - produtoMenorLucro.precoCusto):.2f}R$",font=(fontType, fontSize),borderwidth=2, relief="groove", height=2, width=30, anchor="center").grid(column=2, row=7)

root.mainloop()




