print()
print("***************** INICO DEL PROGRAMA *********************")
print()

frutas= []
contador = 0 
registro = 0 

registro = int(input("Ingrese la cantida de frutas a registrar = "))

while contador < registro:
    fruta = {}
    fruta["id"]     = contador+1
    print()
    print(f"---------------fruta  {contador+1}-----------------")
    fruta["nombre"] = input(f"Ingrese el nombre de la fruta      => ")
    fruta["color"]  = input(f"Ingrese el color de la fruta       => ")
    fruta["precio"] = int(input(f"Ingrese el nombre de la fruta      => "))
    print()
    contador+=1
    frutas.append(fruta)

print()
print("***************** RESULTADOS *********************")
print()
print(frutas)
print()
frutas.reverse()
print(frutas)
