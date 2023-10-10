import random


produtos = []
print("inicio",len(produtos))
while(len(produtos) < 3):
    print("teste")
    cod = random.randint(1,5)
    estoqueMin = random.randint(0,1000)
    estoqueMax = random.randint(estoqueMin,1000)
    estoque = random.randint(estoqueMin, estoqueMax)
    precoCusto = random.uniform(0.1,1000)
    ipi = random.uniform(0,1)
    icms = random.uniform(0,1)
    precoVenda = precoCusto*(icms*ipi+1)
    
    if(len(produtos) == 0):
        print("if1")
        produtos.append(produto)
    else:
        print(produtos, cod)
        sair = True
        while(sair):
            for x, pro in enumerate(produtos):
                if pro[0] == cod:
                    print("rep",pro[0])
                    cod = random.randint(1,5)
                    break
                if x+1 == len(produtos):
                    sair = False
        produto = [cod]
        produtos.append(produto) 
print(produtos)
    


