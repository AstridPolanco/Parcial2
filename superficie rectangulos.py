#Ejercicio 2
def superficie_rectangulo(lado1, lado2):
    return lado1 * lado2

#bloque principal
lado1_rectangulo1= 15
lado2_rectangulo1= 20

lado1_rectangulo2=7
lado2_rectangulo2=12

superficie_rectangulo1 = superficie_rectangulo(lado1_rectangulo1, lado2_rectangulo1)
superficie_rectangulo2 = superficie_rectangulo(lado1_rectangulo2, lado2_rectangulo2)

print("La superficie del primer rectangulo es de: ", superficie_rectangulo1)
print("La superficie del segundo rectangulo es de: ", superficie_rectangulo2)


if superficie_rectangulo1 > superficie_rectangulo2:
    print("El primer rectangulo tiene una superficie mayor")
elif superficie_rectangulo2 > superficie_rectangulo1:
    print("El segundo  rectangulo tiene una superficie mayor")
else:
    print("Ambos rectangulos tienen la misma superficie")





 

    


    
