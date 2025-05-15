#lista=[1,"P",True]
#estado=lista[2]
#print(estado) (muestra true xq empeza desde 0)
#len para mirar el numero de datos
lista=[2,"p","david",3.14,True,100,"@"]
print(type(lista))
print(lista)
numero=(lista[0])
print(numero)
decimal=(lista[3])
print(decimal)
#tamañno de la lista
tamaño=len(lista)
print(f"el tamaño de la lista es {tamaño}")
estado=lista[4]
print(estado)
dato=lista[-4]
print(dato)
datos=lista[0:3]
print(datos)
print(lista[2:6])
print(lista[:])
print(lista[2:])
print(lista[:4])
print(lista[-4:])
print(lista[-4:-1])
numeros=[]
print(numeros)
#añadir valores 
numeros.append(10)
numeros.append(1)
numeros.append(5)
numeros.append(input("ingrese un numero"))
print(numeros)
numeros.insert(0,"adrian")#numero en la lista y dato q se inserta
print(numeros)
numeros.insert(2,100)
numeros.insert(3,"bedoya")
numeros.insert(4,True)
numeros.append(3.14)
numeros.append("python")
print(numeros)
print(f"la cantidad de numeros es {len(numeros)}")
#eliminar datos
numeros.remove("adrian")
print(numeros)
print(f"la cantidad de numeros es {len(numeros)}")
numeros.pop()#elimina el ultimo
print(numeros)
numeros[1:4] = []
print(numeros)
#separar datos de la lista con for
for dato in numero:
    print(f"dato:"(dato))
lista1=[1,2,3,4,5]
lista1.reverse #invierta la lista
print(lista1)
lista3=[10,2,30,4,5,1]
lista3.sort()#ordena la lista accesente
print(lista3)
lista3.sort(reverse=True)#ordena la lista de forma descendente
print(lista3)
