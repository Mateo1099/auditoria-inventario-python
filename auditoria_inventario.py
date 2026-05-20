# *************************************************************************
# Universidad Nacional Abierta y a Distancia (UNAD)
# Curso: Fundamentos de Programación (213022)
# Fase 5 - Evaluación Final POA
# 
# Estudiante: Mateo Trujillo Estrada
# Edad: 26 años
# Grupo: 213022_237
# Tutor: Carlos A. Sánchez P.
# Problema Seleccionado: Problema 3 - Auditoría de Inventario
# *************************************************************************

def calcular_cantidad_a_pedir(stock_actual, stock_minimo):
    """
    Módulo (Función) encargado de aplicar la lógica de negocio.
    Recibe el inventario actual y el mínimo requerido de un artículo,
    y determina la cantidad exacta que se debe solicitar al proveedor.
    """
    # Condición principal: Si el stock actual está por debajo del mínimo establecido
    if stock_actual < stock_minimo:
        # Se calcula y retorna la diferencia exacta faltante
        return stock_minimo - stock_actual
    else:
        # Si el stock actual es igual o mayor al mínimo, no se requiere pedir nada (0)
        return 0


def ejecutar_auditoria():
    """
    Módulo principal que almacena la matriz de datos, realiza el procesamiento
    a través del ciclo e imprime el reporte final en pantalla.
    """
    # Definición de la matriz con 5 filas y 4 columnas según los datos aprobados:
    # Columnas: [0: Código (int), 1: Nombre (str), 2: Stock Actual (int), 3: Stock Mínimo (int)]
    matriz_inventario = [
        [101, "Teclado Mecanico", 15, 20],
        [102, "Raton Gamer      ", 35, 30],
        [103, "Auriculares Pro  ", 8, 12],
        [104, "Alfombrilla XL   ", 50, 25],
        [105, "Mando Control    ", 3, 10]
    ]
    
    # Impresión del encabezado del reporte para la terminal
    print("=======================================================================")
    print("                REPORTE DE AUDITORÍA DE INVENTARIO                     ")
    print("=======================================================================")
    print("CODIGO | PRODUCTO          | STOCK ACTUAL | STOCK MINIMO | A PEDIR     ")
    print("-----------------------------------------------------------------------")
    
    # Ciclo 'for' para recorrer la matriz fila por fila (cada fila representa un producto)
    for producto in matriz_inventario:
        # Extracción de los datos individuales de la fila usando sus posiciones (índices)
        codigo = producto[0]
        nombre = producto[1]
        stock_actual = producto[2]
        stock_minimo = producto[3]
        
        # Llamado al módulo de cálculo enviándole los datos específicos de este producto
        cantidad_a_pedir = calcular_cantidad_a_pedir(stock_actual, stock_minimo)
        
        # Impresión de la línea del producto con los datos alineados y el resultado obtenido
        print(f"{codigo}    | {nombre} |      {stock_actual:2d}      |      {stock_minimo:2d}      |   {cantidad_a_pedir:2d}")

    print("=======================================================================")


# Línea de control estándar en Python para asegurar que el programa se ejecute de forma ordenada
if __name__ == "__main__":
    ejecutar_auditoria()