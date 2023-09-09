



#Definir al funcion 
def saludar():
    print("Hola")
    


# luego hacemos el llamado de la funcion

saludar()


#Funcion que recibe parametros 

def saludar2(name):
    print(f"Hola {name} ")


#Hacemos el llmado a la funcion 

saludar2("Evelin")

#Cuando no conocemos el numero de argumentos que requiere la funcion

def imprimir_lista(*args):
    print(f"Bienvenidos {args}")


imprimir_lista("Evelin","Alejandro", "Pandy")


#Fundiones con retorno

def sumar(num1,num2):
    return num1 + num2


resultado_suma = sumar(5,9)

print(resultado_suma)


usuario = ["1","Alejandro", "Perez","alejandrop@gmail.com", "123pea"]

def imprimirlista(lista):
    for i in range(len(lista)):
        print(lista[i])

print(usuario)