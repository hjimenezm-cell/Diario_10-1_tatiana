#SYSTEMA DE CONTROL DE AFORO DEL CENAC
#Autor: tatiana jimenez
#fecha: 2024-06-10

CAPACIDAD_MAXIMA = 700
UMBRAL_PREVENTIVO = 560

grupos_aceptados =[]
grupos_rechazados = []
ocupacion_actual = 0


print("CONTROL DE INGRESO - ANFITEATRO DEL CENAC")
print("capacidad maxima: 700 prsonas ")
print("escriba 'fin' paracerrar el programa \n")

entrada = input("cantidad de personas del grupo: ").lower().strip()

while entrada != 'fin':
    try:
        cantidad_grupo = int(entrada)
    except ValueError:
        print("Entrada invalida: escriba un entero o'fin'")
    else:
        if cantidad_grupo < 0:
            print("EROR: cantidad de personas no valida.")
        elif cantidad_grupo + ocupacion_actual <= CAPACIDAD_MAXIMA:
            grupos_aceptados.append(cantidad_grupo)
            ocupacion_actual += cantidad_grupo
            espacios_disponibles = CAPACIDAD_MAXIMA - ocupacion_actual
            print(f"Grupo aceptado: ingresan {cantidad_grupo}personas")
            print(f"ocupacion actual: {ocupacion_actual} ")
            print(f"Espacios disponibles : {espacios_disponibles} ")
        else:
            grupos_rechazados.append(cantidad_grupo)
            espacios_disponibls = CAPACIDAD_MAXIMA - ocupacion_actual
            print(f"Grupo rechazado: no hay espacio para {cantidad_grupo} personas")
            print(f"ocupacion actual: {ocupacion_actual} ")
            print(f"Espacios disponibles : {espacios_disponibles} ")
            
        
    
    entrada = input("cantidad de personas del grupo: ").lower().strip()
    
    
