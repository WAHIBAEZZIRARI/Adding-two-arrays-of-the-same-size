N = int(input("Entrez la taille des tableaux T1 et T2 : "))
T1 = []
T2 = []
T = []

print("Entrez les éléments de T1 :")
for _ in range(N):
    element = int(input())
    T1.append(element)

print("Entrez les éléments de T2 :")
for _ in range(N):
    element = int(input())
    T2.append(element)

for i in range(N):
    T.append(T1[i] + T2[i])

print("Le tableau T résultant est :", T)
