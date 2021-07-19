from random import randint, seed




def merge(L, R):
  F = [0]*(len(L) + len(R))

  i = j = k = 0
  while i < len(L) and j < len(R):
    if L[i] <= R[j]:
      F[k] = L[i]
      i += 1
    else:
      F[k] = R[j]
      j += 1
    k += 1

  while i < len(L):
    F[k] = L[i]
    k += 1
    i += 1
  while j < len(R):
    F[k] = R[j]
    k += 1
    j += 1

  return F


def mergesort(T):
  n = len(T)

  if n > 1:
    c = n//2

    L = T[0:c]
    R = T[c:]

    L = mergesort(L)
    R = mergesort(R)

    return merge(L, R)
  else:
    return T
  
  
  

seed(42)

n = 10
T = [ randint(1,10) for i in range(10) ]

print("przed sortowaniem: T =", T) 
T = mergesort(T)
print("po sortowaniu    : T =", T)

for i in range(len(T)-1):
  if T[i] > T[i+1]:
    print("Błąd sortowania!")
    exit()
    
print("OK")