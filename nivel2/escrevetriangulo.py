def triangulo_valido(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    if a > (b + c):
        return False
    if b > (a + c):
        return False
    if c > (a + b):
        return False
    return True

with open("data/lados.txt", "r") as arq:
    linhas = arq.readlines()
respostas = []
for linha in linhas:
    partes = linha.strip().split()
    # convertendo cada parte para float
    for i in range(len(partes)):
        partes[i] = float(partes[i])
    resposta = triangulo_valido(partes[0], partes[1], partes[2])
    if resposta:
        respostas.append("SIM")
    else:
        respostas.append("NÃO")

with open("resposta-triangulos.txt", "w") as arq:
    for resp in respostas:
        arq.write(f"{resp}\n")


