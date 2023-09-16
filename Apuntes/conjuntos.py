#los conjuntos son incambiables (item)
#son no ordenados
#no permiten duplicados
#son iterables 
# se construyen usando llaves {}
# si permiten agregar o eliminar elementos o items

usuarios = {"user1", "user2","user3", "user4"}

# usuario[1]="usern" no se puede hacer 

#Podemos agregar usuarios 
usuarios.add("user5")
print(usuarios)

#se puede valodar si un elemttento existe o no en el set 
print("user2" in usuarios)
print("user6" in usuarios)

#se puede remover elemntos 
usuarios.remove("user3")
print(usuarios)

for i in usuarios:
    print(i)
    
# se unen ambos conjuntos 
usuariosNuevos={"user6","user7"}
usuarios.union(usuariosNuevos)
for i in usuarios:
    print(i)


otrosUsuarios = {"user1","user3","user7","user9","user8",}
print("------------------------")
usuarios.update(otrosUsuarios)
for i in usuarios:
    print(i)
    
usuarios = frozenset([ "user1","user2","user10"])
usuarios2 = {usuarios, "user11","user12"}
print(usuarios2)

print("------------------------")
print(usuarios.intersection(otrosUsuarios))
print("------------------------") 
print(usuarios.symmetric_difference(otrosUsuarios))