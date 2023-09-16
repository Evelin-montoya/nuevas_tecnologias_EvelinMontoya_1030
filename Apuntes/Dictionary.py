# Los diccionarios esatn compuestos de clave valor 
# son mutables 
#no admiten claves repetidas
# desde python 3.7 son ordemnados 

user1 = {"name: ": "Juan",
        "LastName: " :"Castro ",
        "email: " :"JuanCastro@gmail.com "}

print(len(user1))
print(type(user1))

#Podemos agregar elemnetos 
user1["password"] = "xyz123"
print(user1.keys())
print(user1.values())
print(user1.items())

print(user1.get("name: "))

#para remover 
user1.pop("email: ")
print(user1.items)

print(user1.get("password: "))


#Podemos usar un for para imprimir e diccionario ya sea solo claves, solo valores o ambos 

for x,y in user1.items():
    print(x,y)
    
#acceder solo a claves 
for x in user1.keys():
    print(x)

#acceder a los valores 

for y in user1.values():
    print(y)
    
    
user1 = {"name: ": "Juan","LastName: " :"Castro ","email: " :"juanCastro@gmail.com ","password ": "juan123"}

user2 = {"name: ": "Pepito","LastName: " :"Lopez ","email: " :"pepitolopez@gmail.com ","password ": "pepito123"}

user3 = {"name: ": "Evelin", "LastName: " :"Montoya","email: " :"evelinmontoya@gmail.com ","password ": "evelin123"}

users={"userA":user1, "userB":user2,"userC":user3}

print(users)
print(type(users))

print(users["userB"]["lastname"])