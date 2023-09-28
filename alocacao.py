num_pessoas = int(input("Quantas pessoas no grupo? "))

tem_fumante = input("Alguém do grupo fuma? (sim/nao) ")
tem_animal = input("Alguém traz animal de estimação? (sim/nao) ")

if tem_fumante.lower() == "sim" or tem_animal.lower() == "sim":
   area = "área externa"

elif num_pessoas >= 5:
   area = "1o andar"

else:
   area = "térreo"

print("O grupo deve ser alocado na", area)