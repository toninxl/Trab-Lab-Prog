"""
Nome: Antonio Carlos dos Santos Ferreira
Registro: 1207085-1
Exercicio:
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4 - Votos para os respectivos candidatos(você deve montar a tabela ex: 1 - José/ 2- João/etc), 5 - Voto Nulo, 6 - Voto em Branco
Faça um programa que calcule e mostre:
O total de votos para cada candidato, o total de votos nulos, o total de votos em branco, a percentagem de votos nulos sobre o total de votos, a percentagem de votos em branco sobre o total de votos, o Candidato que venceu as eleições
Para finalizar o conjunto de votos tem-se o valor zero."""

candidatos = {1: "Antonio", 2: "Carlos", 3: "Santos", 4: "Ferreira"}

votos = {1: 0, 2: 0, 3: 0, 4: 0, "nulo": 0, "branco": 0}

print("Selecione o seu voto:")
for cod, nome in candidatos.items():
    print(f"{cod} - {nome}")
print("5 - Voto Nulo")
print("6 - Voto em Branco")
print("0 - Encerrar votação\n")

while True:
    try:  # usei try pra evitar valores inválidos dentro do input
        voto = int(input("Digite o código do voto: "))
    except ValueError:
        print("Voto inválido. Tente novamente.")
        continue
    if voto == 0:
        break  # encerra o lopp
    elif voto in candidatos:
        votos[voto] += 1
    elif voto == 5:
        votos["nulo"] += 1
    elif voto == 6:
        votos["branco"] += 1
    else:
        print("Voto inválido. Tente novamente.")

total_votos = sum(votos.values())

print("\nResultado da eleição:")
for cod, nome in candidatos.items():
    print(f"{nome}: {votos[cod]} votos")
print(f"Nulos: {votos['nulo']} votos")
print(f"Brancos: {votos['branco']} votos")

if total_votos > 0:
    quantidade_nulo = votos["nulo"]
    porcentagem_nulo = (quantidade_nulo / total_votos) * 100

    quantidade_branco = votos["branco"]
    porcentagem_branco = (quantidade_branco / total_votos) * 100
else:
    porcentagem_nulo = 0
    porcentagem_branco = 0

print(f"Percentual de votos nulos: {porcentagem_nulo:.2f}%")
print(f"Percentual de votos em branco: {porcentagem_branco:.2f}%")

maior_votos = 0
nome_vencedor = ""
for cod in candidatos:
    if votos[cod] > maior_votos:
        maior_votos = votos[cod]
        nome_vencedor = candidatos[cod]

empate = []
for cod in candidatos:
    if votos[cod] == maior_votos:
        empate.append(candidatos[cod])
if len(empate) > 1:
    print(f"Empate entre: {', '.join(empate)} com {maior_votos} votos.")
else:
    print(f"Vencedor: {nome_vencedor} com {maior_votos} votos.")


"""Obs: para resolução do trabalho utilizei os fundamentos ensinados em aula ealgumas práticas que estou acostumado no meu dia a dia no trabalho."""