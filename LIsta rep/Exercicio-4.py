import random
name = [
    "Helena", "Alice", "Laura", "Maria Alice", "Sophia", "Manuela", "Maitê", "Liz", 
    "Cecília", "Isabella", "Luísa", "Eloá", "Heloísa", "Júlia", "Ayla", "Maria Luísa", 
    "Isis", "Elisa", "Antonella", "Valentina", "Maya", "Maria Júlia", "Aurora", "Lara", 
    "Maria Clara", "Lívia", "Esther", "Giovanna", "Sarah", "Maria Cecília", "Lorena", 
    "Beatriz", "Rebecca", "Luna", "Olívia", "Maria Helena", "Mariana", "Isadora", 
    "Melissa", "Maria", "Catarina", "Lavínia", "Alícia", "Maria Eduarda", "Agatha", 
    "Ana Liz", "Yasmin", "Emanuelly", "Ana Clara", "Clara", "Ana Júlia", "Marina", 
    "Stella", "Jade", "Maria Liz", "Ana Laura", "Maria Isis", "Ana Luísa", "Gabriela", 
    "Alana", "Rafaela", "Vitória", "Isabelly", "Bella", "Milena", "Clarice", "Mirella", 
    "Ana", "Emilly", "Betina", "Mariah", "Zoe", "Maria Vitória", "Nicole", "Laís", 
    "Melina", "Bianca", "Louise", "Ana Beatriz", "Heloíse", "Malu", "Melinda", 
    "Letícia", "Maria Valentina", "Chloe", "Maria Elisa", "Maria Heloísa", "Maria Laura", 
    "Maria Fernanda", "Ana Cecília", "Hadassa", "Ana Vitória", "Diana", "Ayla Sophia", 
    "Eduarda", "Ana Lívia", "Isabel", "Elis", "Pérola", "Joana",
    "Miguel", "Arthur", "Gael", "Théo", "Heitor", "Ravi", "Davi", "Bernardo", 
    "Noah", "Gabriel", "Samuel", "Pedro", "Anthony", "Isaac", "Benício", "Benjamin", 
    "Matheus", "Lucas", "Joaquim", "Nicolas", "Lucca", "Lorenzo", "Henrique", 
    "João Miguel", "Rafael", "Henry", "Murilo", "Levi", "Guilherme", "Vicente", 
    "Felipe", "Bryan", "Matteo", "Bento", "João Pedro", "Pietro", "Leonardo", 
    "Daniel", "Gustavo", "Pedro Henrique", "João Lucas", "Emanuel", "João", "Caleb", 
    "Davi Lucca", "Antônio", "Eduardo", "Enrico", "Caio", "José", "Enzo Gabriel", 
    "Augusto", "Mathias", "Vitor", "Enzo", "Cauã", "Francisco", "Rael", 
    "João Guilherme", "Thomas", "Yuri", "Yan", "Anthony Gabriel", "Oliver", "Otávio", 
    "João Gabriel", "Nathan", "Davi Lucas", "Vinícius", "Theodoro", "Valentim", 
    "Ryan", "Luiz Miguel", "Arthur Miguel", "João Vitor", "Léo", "Ravi Lucca", 
    "Apollo", "Thiago", "Tomás", "Martin", "José Miguel", "Erick", "Liam", "Josué", 
    "Luan", "Asafe", "Raul", "José Pedro", "Dominic", "Kauê", "Kalel", 
    "Luiz Henrique", "Dom", "Davi Miguel", "Estevão", "Breno", "Davi Luiz", "Thales", 
    "Isreal"
]
somaAltura, pesoInferior, altura1020 = 0,0,0
pessoas, pessoasIdade50, pessoasMediaAltura, pessoasPesoInferior = [], [], [], []
autoTeste = input("Auto testar: s/n")
if autoTeste == "s":
    xPessoas = int(input("Quantidade de pessoas:"))
    for i in range(0, xPessoas):
        pessoa = {
            "nome": name[random.randint(0,len(name)-1)],
            "idade": random.randint(0,100),
            "altura": random.uniform(1.40,2.20), 
            "peso": random.uniform(40.0, 150.00)
        }
        pessoas.append(pessoa)
        if pessoa["idade"] > 50:
            pessoasIdade50.append(pessoa)
        if pessoa["idade"] >= 10 and pessoa["idade"] <= 20:
            pessoasMediaAltura.append(pessoa)
            somaAltura += pessoa["altura"]
        if pessoa["altura"] < 40:
            pessoasPesoInferior.append(pessoa)
    print(pessoas[i])
    print(f"Têm {len(pessoasIdade50)} com ida")
    for pessoa in pessoasIdade50:
        print(f"A pessoa {pessoa['nome']} têm {pessoa['idade']} anos")
    for pessoa in pessoasMediaAltura:
        print(f"A pessoa {pessoa['nome']} têm {pessoa['altura']:.2f} metros de altura")
    for pessoa in pessoasPesoInferior:
        print(f"A pessoa {pessoa['nome']} têm {pessoa['peso']:.2f}kg")
else:
    
    for i in range(3):
        peso =float(input("peso"))
        altura =float(input("altura"))
        idade =int(input("idade"))
        if idade >= 10 and idade <= 20:
            altura1020 += 1
            somaAltura += altura

    print(somaAltura/altura1020)