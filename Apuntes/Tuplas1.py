#Las tuplas se encierran en parentesis 
# son inmutables 
# si se requiere que tengan algun cambio se debe casquear a lista 
#se puede acceder a los elementos 
#permiten dublicado 
# y distintos tipos de datos 

colores = ("Amarrillo","Azul","Rojo")
print(type(colores))
print(len(colores))
print(type(colores[0]))
print(type(colores[1]))
print(type(colores[2]))

#casquear

colores_lista = list(colores)

print(type(colores_lista))

colores_lista.append("verde")

print(colores_lista[0:])

colores=tuple(colores_lista)
print(type(colores))

#Recorrer una tupla
for i in range(len(colores)):
    print(colores[i])
    
#slicing

print(colores[1:4])
print(colores[:-1])