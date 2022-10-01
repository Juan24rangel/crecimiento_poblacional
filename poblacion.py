print("En 1980 la ciudad A tenía 3.5 millones de habitantes y una rata de crecimiento del (7%) anual; y la ciudad B tenía 5 millones y una rata de crecimiento del (5%) anual. Si el crecimiento poblacional se mantiene constante en las dos ciudades, hacer el diagrama de flujo y el programa en Python, que calculé e imprima, en qué año la población de la ciudad A es mayor a la de la ciudad B.")

#processing
A = 3.5
B = 5
n = 1980

while B > A:
    A = A + (A*0.07)
    B = B + (B* 0.05)
    n = n + 1
    
#output
print ("el año es: "+str(n))