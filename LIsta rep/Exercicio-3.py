import random
faixas = [0,0,0,0,0]
for i in range(1,16):
    idade = random.randint(1, 99)
    print(f"Pessoa {i} com a idade {idade}")
    if idade < 16:
        #15 ou menos
        faixas[0] += 1
        print(f"Com esta pessoa totaliza {faixas[0]} pessoas com a idade de 15 ou menos")
    elif idade < 31:
        #16 a 30
        faixas[1] += 1
        print(f"Com esta pessoa totaliza {faixas[1]} pessoas com a idade de 16 á 30")
    elif idade < 46:
        #31 a 45
        faixas[2] += 1
        print(f"Com esta pessoa totaliza {faixas[2]} pessoas com a idade de 31 á 45")
    elif idade < 61:
        #46 a 60
        faixas[3] += 1
        print(f"Com esta pessoa totaliza {faixas[3]} pessoas com a idade de 46 á 60")
    else:
        #61 ou mais
        faixas[4] += 1
        print(f"Com esta pessoa totaliza {faixas[4]} pessoas com a idade de 61 ou mais")
print(f"São {faixas[0]} da faixa de 15 ou menos, sendo estes {faixas[0]/15*100:.2f}%")
print(f"São {faixas[1]} da faixa de 16 á 30 anos, sendo estes {faixas[1]/15*100:.2f}%")
print(f"São {faixas[2]} da faixa de 31 á 45 anos, sendo estes {faixas[2]/15*100:.2f}%")
print(f"São {faixas[3]} da faixa de 46 á 60 anos, sendo estes {faixas[3]/15*100:.2f}%")
print(f"São {faixas[4]} da faixa de 61 ou mais, sendo estes {faixas[4]/15*100:.2f}%")




