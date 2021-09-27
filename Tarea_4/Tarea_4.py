lista=[]
numero=[]
for i in range(24):
	for j in range(60):
		lista.append((i , j))
for w in range(3):
    a=n=670*w
    v=lista.pop(a)
    numero.append(v)
print("el numero de palindromos que ahy en las 24 horas del dia son;",len(numero),"y son;",numero)
    
    
            