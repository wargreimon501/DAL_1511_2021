r=float(input("dama la cvantidad de dinero  quiera que te convierta en billetes  ")) #O(1)   O(1|)
def encontrar_denominacion_moneda(n):
    lista=[500,200,100,20,10,5,1,0.5] # O(1)   O(1)
    for i in lista:
        if n >=i:
            q= n // i # O=(1) O(8*4)=32
            print(str(q)+(' billetes' if n>=10 else ' monedas')+" de "+str(i)+" pesos") #O(1)    O(8)
            n=n % i #O(1) O(8*4)=32
encontrar_denominacion_moneda(r)
#procesamiento O(1+8+32+32) -->O(73)
#complejidad O(1+1+1+1) -->O(4)