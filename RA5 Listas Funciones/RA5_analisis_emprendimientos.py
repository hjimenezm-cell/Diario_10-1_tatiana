"""Practica Semana 07: analisis de emprendimientos costarricenses.

Complete los espacios marcados con TODO. El objetivo es generar un reporte por
sede usando listas, diccionarios, funciones, ciclos y condicionales.
"""

from sedes import sedes

def calcular_promedio(lista):
    """Recibo una lista, la sumo y retorno el promedio"""
    promedio = sum(lista) / len(lista)
    return promedio 

def calcular_logro_meta(lista_ventas,meta):
    """cálcula el porcentaje de logro de la meta"""
    total_ventas = (sum(lista_ventas))
    return (total_ventas * 100) / meta 

def calcular_clasificacion(porcentaje):
    if porcentaje >=100:
        mensaje = "Felicidades meta alcanzada, sigue asi "
    elif porcentaje >=80:
        mensaje = "Llamada atencion, debe trabajar por la meta..!"
    else:
        mensaje = "URGENTE, crisis de ventas. Atención prioritaria."
    return mensaje 

def imprirmir_reporte(datos_reporte):
    """Imprime el reporte final de ventas por sede,"""
    print("\n REPORTE FINAL")
    print("-" * 60)
    # se recorre cada fila del reporte .
    for fila in datos_reporte:
        print(f"sede: {fila['nombre']}")
        print(f"provincia: {fila['provincia']}")
        print(f"tipo: {fila['tipo']}")
        print(f"total semanal: ₵{fila['total']:,.0f}")
        #se imprime el promedio diario con formato de moneda 
        print(f"promedio diario: ₵{fila['promedio']:,.2f}")
        #se imprime el porcentaje  con dos decimales 
        print(f"cumplimiento: {fila['promedio']:,.2f}%")
        print(f"estado: {fila['estado']}")
        print("-" * 60)
    print("cantidad de sedes:", len(datos_reporte))

reporte = []
for emprendimiento in sedes:
    ventas = emprendimiento['ventas']
    meta = emprendimiento['meta']
    nombre = emprendimiento['nombre']
    promedio_diario = calcular_promedio(ventas)
    porcentaje_logro = calcular_logro_meta(ventas , meta)
    clasificacion = calcular_clasificacion(porcentaje_logro)  # --- clasificación
    
    reporte.append( 
        {
            "nombre": nombre,
            "provincia": emprendimiento["provincia"],
            "tipo":emprendimiento["tipo"],
            "total":sum(emprendimiento['ventas']),
            "promedio": promedio_diario,
            "porcentaje": porcentaje_logro,
            "estado": clasificacion
        }            
    )
    imprirmir_reporte(reporte)
    #print(f'\n---Emprendimiento {nombre}---')
    #print("promedio diario de ventas:" , promedio_diario)
    #print("porcentaje logro:" , porcentaje_logro)
    #print("clasificación:", clasificacion) # --- clasificación