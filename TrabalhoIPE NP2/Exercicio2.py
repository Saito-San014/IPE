import random
from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()

cartela = []
while(len(cartela) < 5):
    linha = []
    while(len(linha)<5):
        if len(linha) == 4:
            num = random.randint(81,99)
        else:
            num = random.randint(20*(len(linha)+1)-20,20*(len(linha)+1))
        if(len(cartela) < 1):
            linha.append(num)
        else:
            for x, lin in enumerate(cartela):
                if lin[len(linha)] == num:
                    break
                if(x+1 == len(cartela)):
                    linha.append(num)
    cartela.append(linha)
cartela.sort()
fontSize = 50
fontType = "Arial"
ttk.Label(frm, text="B",font=(fontType, fontSize)).grid(column=0, row=0)
ttk.Label(frm, text="I",font=(fontType, fontSize)).grid(column=1, row=0)
ttk.Label(frm, text="N",font=(fontType, fontSize)).grid(column=2, row=0)
ttk.Label(frm, text="G",font=(fontType, fontSize)).grid(column=3, row=0)
ttk.Label(frm, text="O",font=(fontType, fontSize)).grid(column=4, row=0)

for x, linha in enumerate(cartela):
    for y, num in enumerate(linha):
        if x == 2 and y == 2:
            Label(frm, text="Gabriel",font=(fontType, 16),borderwidth=2, relief="groove", height=3, width=6, anchor="center").grid(column=y, row=x+1)
        else:
            ttk.Label(frm, text=str(num),font=(fontType, fontSize),borderwidth=2, relief="groove", width=2, anchor="center",justify=CENTER).grid(column=y, row=x+1)
print(cartela)
root.mainloop()
