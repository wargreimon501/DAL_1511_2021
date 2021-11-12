

def string_match_brute(A , P):
  for i in range(len(A)-len(P) + 1 ):
    for j in range(len(P)):
      if P[j] == A[i+j]:
         pass
      else:
        break
    if j+1 == len(P) and A[i+j] == P[j]:
      print(f"se encontro en la pocicion: {i}")
    
arch=open('el_quijote_ii.txt', encoding="utf8")
f=arch.read() 
p=int(input("que deceas buscar hidalfo preciona ;1 ,molino preciona; 2,merced preciona 3  ;"))
if p==1:
    patron="hidalfo"
    entrada=f
    S=string_match_brute(entrada,patron)
if p==2:
    patron="molino"
    entrada=f
    S=string_match_brute(entrada,patron)
if p==3:
    patron="merced"
    entrada=f
