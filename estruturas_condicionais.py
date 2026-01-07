MAIOR_IDADE = 18
IDADE_ESPECIAL = 17


idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar sua CNH.")

if idade <= MAIOR_IDADE:
    print("Idade não permitida para tirar sua CNH.")



if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar sua CNH.")
else:
    print("Idade não permitida para tirar sua CNH.")



if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar sua CNH.")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teóricas, mas não é permitido aula prática.")
else:
    print("Idade não permitida para tirar sua CNH.")
