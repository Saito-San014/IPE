import random
maior18, menor18 = 0,0
for i in range(1,11):
    idade = random.randint(1, 50)
    print(f"Pessoa {i} com a idade {idade}")
    if idade >= 18:
        maior18 += 1
    else:
        menor18 += 1

print("São {} pessoas com idade maior que 18 anos".format(maior18))
print("Das dez pessoas, {}% têm mais que 18 e {}% têm menos que 18.".format(maior18/10*100, menor18/10*100))