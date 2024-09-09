
print("Ejemplo de listas")
arcoiris = ["verde","azul", "morado"]
print(arcoiris)
longitud = len(arcoiris)
print("ELementos que contiene la lista arcoiris:", longitud)
print(f"ELementos que contiene la lista arcoiris: {longitud}")

print("accediendo a un elemento de la lista")
print(arcoiris[1])
print(f"elemento en la posicion 1 es: {arcoiris[0]}")
print(f"El primer color del arcoirirs es: ", arcoiris[0])

print("agregar a un elemnto de la lista")
print(arcoiris)
arcoiris.append("naranja")
print(arcoiris)

print("Listar los elementos de la lista ciclo for")
for andres in arcoiris:
    print(andres)