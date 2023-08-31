# Feito por: Vinícius Costa Pan

def strToSet(linha):
    result = set([])
    valor = ""
    for i in range(len(linha)):
        if linha[i] != ',' and linha[i] != " " and linha[i] != "\n":
            valor += linha[i]
        if linha[i] == ',' or linha[i] == '\n':
            result.add(valor)
            valor = ""
    return result

def prodCartesiano(set1, set2):
    set3 = set([])
    for i in set1:
        for j in set2:
            set3.add((i, j))
    return set3

filename = input("Digite o nome do arquivo txt de entrada (sem o .txt): ")
file = open("{}.txt".format(filename))

num_op = int(file.readline().replace("\n", ""))

for i in range(num_op):
    op = file.readline().replace("\n", "")
    set1 = strToSet(file.readline())
    set2 = strToSet(file.readline())
    if op == "U":
        print("União: conjunto 1 {}, conjunto 2 {}. Resultado: {}".format(set1, set2, set1 | set2))
    elif op == "I":
        print("Interseção: conjunto 1 {}, conjunto 2 {}. Resultado: {}".format(set1, set2, set1 & set2))
    elif op == "D":
        print("Diferença: conjunto 1 {}, conjunto 2 {}. Resultado: {}".format(set1, set2, set1 - set2))
    else:
        print("Produto cartesiano: conjunto 1 {}, conjunto 2 {}. Resultado: {}".format(set1, set2, prodCartesiano(set1, set2)))

file.close()