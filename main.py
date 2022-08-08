#Franklin.J.B.B.Vieira

txt = open("text.txt")

vet = []


for line in txt:
    StrippedLine = line.strip()
    vet.append(StrippedLine)


for i in range(len(vet)):

#União
    if vet[i] == "U":

        Conj1 = set(vet[i+1].split(', '))

        Conj2 = set(vet[i+2].split(', '))

        Uni = Conj1.union(Conj2)
        print("União: conjunto 1 %s, conjunto 2 %s. Resultado: %s"%(Conj1,Conj2,Uni),end="\n \n")

#Intercessão
    elif vet[i] == "I":

        Conj1 = (vet[i + 1].split(', '))

        Conj2 = (vet[i + 2].split(', '))

        Intersec = set(Conj1).intersection(set(Conj2))
        print("Intercessão: conjunto 1 %s, conjunto 2 %s. Resultado: %s"%(Conj1,Conj2,Intersec),end="\n \n")

#Diferença
    elif vet[i] == "D":
        Conj1 = set(vet[i + 1].split(', '))

        Conj2 = set(vet[i + 2].split(', '))

        Diff = Conj1.difference(Conj2)
        print("Diferença: conjunto 1 %s, conjunto 2 %s. Resultado: %s"%(Conj1,Conj2,Diff),end="\n \n")

#Cartesiano
    elif vet[i] == "C":
        Conj1 = vet[i+1].split(', ')

        Conj2 = vet[i+2].split(', ')

        print("Cartesiano: conjunto 1 %s, conjunto 2 %s. Resultado:"%(Conj1,Conj2),end='')

        for i in Conj1:
            for j in Conj2:
                print('[',i,',', j,'],', end='')
        print("\n")