
def somme(t):
    s=0
    for i in t:
        s += i
    return s

Data=[1,3,5]
som=sum(Data)
print("La somme des éléments de la liste est:", som)

if not Data:
    print("La liste est vide.")
else:
    print("le min de la liste est:", min(Data))
    print("le max de la liste est:", max(Data))
    print("La somme des éléments de la liste est:", sum(Data))

