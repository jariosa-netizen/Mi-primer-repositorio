peliculas =  {
    'P101': ['Luz de Otoño', 'drama', 110, 'B', 'Español', False],
    'P102': ['Noche Neón', 'acción', 125, 'C', 'Ingles', True],
    'P103': ['Planeta Agua', 'documental', 90, 'A', 'Español', False],
    'P104': ['Risa Total', 'comedia', 105, 'A', 'Español', True],
    'P105': ['Código Zero', 'thriller', 118, 'C', 'Ingles', True],
    'P106': ['Viaje Lunar', 'ciencia ficción', 132, 'B', 'Ingles', False],
}


cartelera = {
    'P101': [5990, 40],
    'P102': [7990, 0],
    'P103': [4990, 25],
    'P104': [6990, 12],
    'P105': [8990, 8],
    'P106': [7490, 3],
}


# --- FUNCIONES DE VALIDACIÓN INDEPENDIENTES (RETORNAN TRUE/FALSE) ---

def validar_codigo(codigo):
    cod_limpio = codigo.strip().upper()
    if cod_limpio == "":
        return False
    return cod_limpio not in peliculas

def validar_titulo(titulo):
    return titulo.strip() != ""

def validar_genero(genero):
    return genero.strip() != ""

def validar_duracion(duracion):
    try:
        return int(duracion) > 0
    except ValueError:
        return False

def validar_clasificacion(clasificacion):
    return clasificacion.strip().upper() in ['A', 'B', 'C']

def validar_idioma(idioma):
    return idioma.strip() != ""

def validar_es_3d(es_3d):
    return es_3d.strip().lower() in ['s', 'n']

def validar_precio(precio):
    try:
        return int(precio) > 0
    except ValueError:
        return False

def validar_cupos(cupos):
    try:
        return int(cupos) >= 0
    except ValueError:
        return False


# --- FUNCIÓN LECTURA DE OPCIÓN ---

def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe seleccionar una opción válida")
        except ValueError:
            print("Debe seleccionar una opción válida")


# --- OPCIÓN 1: CUPOS POR GÉNERO ---

def cupos_genero(genero):
    genero_buscado = genero.strip().lower()
    total_cupos = 0
    
    for codigo, datos in peliculas.items():
        if datos[1].lower() == genero_buscado:
            total_cupos += cartelera[codigo][1]
            
    print(f"El total de cupos disponibles es: {total_cupos}")


# --- OPCIÓN 2: RANGO DE PRECIO ---

def busqueda_precio(p_min, p_max):
    lista_resultados = []
    for codigo, datos_operativos in cartelera.items():
        precio = datos_operativos[0]
        cupos = datos_operativos[1]
        
        if p_min <= precio <= p_max and cupos > 0:
            titulo = peliculas[codigo][0]
            lista_resultados.append(f"{titulo}--{codigo}")
            
    if len(lista_resultados) > 0:
        lista_resultados.sort()
        print(f"Las películas encontradas son: {lista_resultados}")
    else:
        print("No hay películas en ese rango de precios.")


# --- OPCIÓN 3: ACTUALIZAR PRECIO ---

def buscar_codigo(codigo):
    return codigo.strip().upper() in cartelera

def actualizar_precio(codigo, nuevo_precio):
    cod_limpio = codigo.strip().upper()
    if buscar_codigo(cod_limpio):
        cartelera[cod_limpio][0] = nuevo_precio
        return True
    return False


# --- OPCIÓN 4: AGREGAR PELÍCULA ---

def agregar_pelicula(codigo, titulo, genero, duracion, clasificacion, idioma, es_3d, precio, cupos):
    cod_limpio = codigo.strip().upper()
    if cod_limpio in peliculas:
        return False
        
    bool_3d = True if es_3d.strip().lower() == 's' else False
    
    peliculas[cod_limpio] = [titulo.strip(), genero.strip(), int(duracion), clasificacion.strip().upper(), idioma.strip(), bool_3d]
    cartelera[cod_limpio] = [int(precio), int(cupos)]
    return True


# --- OPCIÓN 5: ELIMINAR PELÍCULA ---

def eliminar_pelicula(codigo):
    cod_limpio = codigo.strip().upper()
    if cod_limpio in peliculas:
        del peliculas[cod_limpio]
        del cartelera[cod_limpio]
        print("Película eliminada")
    else:
        print("El código no existe")


# --- CONTROLADOR PRINCIPAL ---

def main():
    while True:
        print("\n====================================")
        opcion = leer_opcion()
        
        if opcion == 1:
            gen = input("Ingrese género a consultar: ")
            cupos_genero(gen)
            
        elif opcion == 2:
            while True:
                try:
                    p_min_str = input("Ingrese precio mínimo: ")
                    p_min = int(p_min_str)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")
                    
            while True:
                try:
                    p_max_str = input("Ingrese precio máximo: ")
                    p_max = int(p_max_str)
                    break
                except ValueError:
                    print("Debe ingresar valores enteros")
            
            busqueda_precio(p_min, p_max)
            
        elif opcion == 3:
            while True:
                cod = input("Ingrese código de película: ")
                
                while True:
                    np_str = input("Ingrese nuevo precio: ")
                    try:
                        precio_nue = int(np_str)
                        if precio_nue > 0:
                            break
                        print("Error: El precio debe ser mayor a cero.")
                    except ValueError:
                        print("Error: Ingrese un entero válido.")
                
                if actualizar_precio(cod, precio_nue):
                    print("Precio actualizado")
                else:
                    print("El código no existe")
                    
                repetir = input("¿Desea actualizar otro precio (s/n)?: ").strip().lower()
                if repetir != 's':
                    break
                    
        elif opcion == 4:
            cod = input("Ingrese código de película: ")
            if not validar_codigo(cod):
                print("El código ya existe")
                continue
                
            tit = input("Ingrese título: ")
            if not validar_titulo(tit):
                continue
                
            gen = input("Ingrese género: ")
            if not validar_genero(gen):
                continue
                
            dur = input("Ingrese duración (minutos): ")
            if not validar_duracion(dur):
                continue
                
            cla = input("Ingrese clasificación: ")
            if not validar_clasificacion(cla):
                continue
                
            idi = input("Ingrese idioma: ")
            if not validar_idioma(idi):
                continue
                
            e3d = input("¿Es 3D? (s/n): ")
            if not validar_es_3d(e3d):
                continue
                
            pre = input("Ingrese precio: ")
            if not validar_precio(pre):
                continue
                
            cup = input("Ingrese cupos: ")
            if not validar_cupos(cup):
                continue
            
            if agregar_pelicula(cod, tit, gen, dur, cla, idi, e3d, pre, cup):
                print("Película agregada")
            else:
                print("El código ya existe")
            
        elif opcion == 5:
            cod_eliminar = input("Ingrese código de película a eliminar: ")
            eliminar_pelicula(cod_eliminar)
            
        elif opcion == 6:
            print("Programa finalizado.")
            break

if __name__ == "__main__":
    main()


