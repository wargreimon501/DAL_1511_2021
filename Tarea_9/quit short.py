lista=[2423,5,151,154,1214,12654,15642,2,51,4,154,5464]

def particion(lista):
    pivote=lista[0]
    menores=[]
    mayores=[]
    for i in range (1,len(lista)):
        if lista[i]<pivote:
            menores.append(lista[i])
            
        else:
            mayores.append(lista[i])
    return menores,pivote,mayores


def quickshort(lista):
    if len(lista)<2:
        return lista
    menores,pivote,mayores=particion(lista)
    return quickshort(menores)+[pivote]+quickshort(mayores)
print(quickshort(lista))
    