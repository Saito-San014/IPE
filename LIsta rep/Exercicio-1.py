maiorIdade = 0
for i in range(1,11):
    idade = int(input("Pessoa {} com a Idade:".format(i)))
    if idade >= 18:
        maiorIdade += 1

print("São {} pessoas com idade maior que 18 anos".format(maiorIdade))