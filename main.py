def Funcion(Estado_inicial, transiciones, caracteres_validos, estados_aceptacion):
    diccionario = {}
    lista_transiciones = []
    lista_Q_finales = []
    i= j = 0 
    estados_Q_nuevos = [cerradura_epsilon(Estado_inicial, transiciones)]
    diccionario.setdefault(chr(65+i),estados_Q_nuevos[i])
    i += 1  
    while j < len(estados_Q_nuevos):
        for c in caracteres_validos:  
            estado = ir_a(estados_Q_nuevos[j], c, transiciones) 
            if not estado in estados_Q_nuevos:
                estados_Q_nuevos.append(estado)
                diccionario.setdefault(chr(65+i),estado)
                sigma = [chr(65+j), c, chr(65+i)]
                lista_transiciones.append(sigma)
                i += 1 
                for n in estado:
                    if n in estados_aceptacion:
                        lista_Q_finales.append(chr(64+i))
                        continue 
            else:
                sigma = [chr(65+j), c, chr(65+(estados_Q_nuevos.index(estado))) ]
                lista_transiciones.append(sigma) 
        j += 1 
    print(f'Estados: {diccionario.keys()}')
    print(f'Simbolos validos: {caracteres_validos}')
    w = 0
    for key in diccionario:
        if w == 0:
            print(f'Estado inicial: {key}')
            w+=1 
    print(f'Estados finales: {lista_Q_finales}')
    print(f'Transiciones:')
    for n in lista_transiciones:
        print(f'{n}')

# def primer_epsilon(Estado, transiciones):
#     transicion = cerradura_epsilon(Estado, transiciones)
#     return transicion

def cerradura_epsilon(Estado, transiciones):
    transicion = []
    transicion.append(Estado) 
    for x in transiciones:
        if x[0] == Estado and x[1] == 'E':
            transicion.extend(cerradura_epsilon(x[2],transiciones))
    transicion = sorted(list(set(transicion)))
    return transicion 

def mover_a(Estado, caracter, transiciones ): 
    transicion = []
    for x in transiciones:
        if x[0] in Estado and x[1] == caracter:
            transicion.append(x[2])
    transicion = sorted(list(set(transicion)))
    return transicion

def ir_a(Estado, caracter, transiciones):
    subset = [] # Subconjunto que contendrá los elementos de la funcion mover 
    nuevo_subset = [] # Subconjunto con los estados que retornaremos 
    subset.extend(mover_a(Estado, caracter, transiciones)) # Adjuntamos los estados de la funcion mover_a 
    subset = set(subset) # Con esto nos aseguramos de que no se repitan estados en el conjunto
    for q in subset: # Iteramos en todos los estados del conjunto generado en la linea anterior
        nuevo_subset.extend(cerradura_epsilon(q,transiciones)) # Adjuntamos los estados resultantes de hacer la cerradura 
    nuevo_subset = sorted(list(nuevo_subset)) #Ordenamos
    nuevo_subset = set(nuevo_subset) # Eliminamos estados repetidos
    return nuevo_subset

def iterar(Estado, caracteres_validos, transiciones):         
    pass

# leer arcchivo txt
entrada = input("Introduce el nombre del archivo a leer en la carpeta, sin espasios y con la extencion (Ejemplo: 1.txt): ")
f = open(entrada, 'r')

EstadosQ = []
Epsilon = []
EdoInicial = ''
EdosAceptacion = []
Sigma = []

# Metemos los estados a nuestra lista de esados
mensaje = f.readline()
for caracter in mensaje:
    if caracter != ',' and caracter != '\n':
        EstadosQ.append(caracter)

# Metemos los simbolos a nuestra lista de Epsilon
mensaje = f.readline()
for caracter in mensaje:
    if caracter != ',' and caracter != '\n':
        Epsilon.append(caracter)

# Metemos el estado de start a nuestra lista de Epsilon
mensaje = f.readline()
for caracter in mensaje:
    if caracter != ',' and caracter != '\n':
        EdoInicial = caracter

# Metemos los estados finales a nuestra lista de estadosFinales
mensaje = f.readline()
x = ''
for caracter in mensaje:
    if caracter != ',' and caracter != '\n':
        x = x+caracter
    else:
        EdosAceptacion.append(x)
        x = ''
if x != '':
    EdosAceptacion.append(x)

# Sigue sigma UTF-8 = "\u03A3"
mensaje = f.readline() #Leemos linea del archivo txt
while(mensaje): # Si el resultado de intentar leer es exitoso, analizamos la linea de transicion 
    cadena_aux = '' #Si los estados/transiciones son de mas de un caracter aqui se acumularan 
    transicion = [] #Se adjuntará una lista con los datos de la transicion a la lista de transiciones Sigma
    x = 0 #Para leer cada transicion
    while x < len(mensaje): #Leemos cada transicion caracter por caracter
        if mensaje[x] != '\n' and mensaje[x] != ',': #Si el caracter es diferente que una coma o un salto de linea...
            cadena_aux = cadena_aux + mensaje[x] #... el caracter se añade a la cadena formada por los caracteres 
        elif mensaje[x] == '\n' or mensaje[x] == ',' or x == (len(mensaje) - 1): #Si es un salto de linea, coma o corchete de cierre...
            transicion.append(cadena_aux) #Se adjunta a la lista con los datos
            cadena_aux = '' # Se reinicia la cadena auxiliar 
        x +=  1  #Iteramos caracter
    if len(transicion) < 3: # Si el largo de la lista con los datos significa que nos falta uno; El ultimo
        transicion.append(cadena_aux) #Agregamos el ultimo dato
    Sigma.append(transicion) #Agregamos la transicion a la lista de transiciones Sigma
    mensaje = f.readline() #Leemos siguiente linea

f.close() # Cerramos el archivo

#print(f'\u03A3: {Sigma}') #Mostramos transiciones 
#print(f'EdosAceptacion: {EdosAceptacion}') #Mostramos transiciones 
#print(f'EdoInicial: {EdoInicial}') #Mostramos transiciones 

#Estado_final = funcion(Sigma, input("Introduzca cadena: "), Epsilon, EdoInicial, EdosAceptacion) #Pedimos la cadena y Comenzamos el analisis de la cadena con el automata 
#print(f'Estados finales:\n{Estado_final}') #Mostramos estados finales 

# prueba = [1,2,3,4] 
# print(f'{prueba}')
# stdy = []
# prueba.extend(stdy)
# print(f'{prueba}') 

# Probando el sorted
# prueba = ['11','10','12']
# prueba2 = ['11','12','10']
# if prueba2 == prueba:
#     print('son iguales')
# else:
#     print('no son iguales')
# print(prueba)
# prueba = sorted(list(prueba))
# prueba2 = sorted(list(prueba2))
# print(prueba)
# if prueba2 == prueba:
#     print('son iguales')
# else:
#     print('no son iguales')

## Letras ## 
# print(chr(97)) #a
# print(ord('11')) # Error
# print(ord('z')) #122
# print(ord('Z')) #90
# print(ord('A')) #65
# print('Minusculas')
# for x in range(97, 123):
#     print(chr(x))
# print('Mayusculas')
# for x in range(65, 91):
#     print(chr(x))

# lista_de_uno = [1]
# print(1 in lista_de_uno)
    
# lista_de_onces = ['11', '11', '11', '10']
# print(lista_de_onces)
# print(set(lista_de_onces))
# print(sorted(set(lista_de_onces)))

# diccionario = [[7,8],[1,2]]
# print([1,2] in diccionario) 
# auxiliar = 0
# while auxiliar < len(lista_de_onces):
#     print(f'Lista: {lista_de_onces}, auxiliar: {auxiliar}')
#     if auxiliar%3 == 0:
#         lista_de_onces.append(auxiliar)
#     auxiliar += 1 

Funcion(EdoInicial, Sigma, Epsilon, EdosAceptacion)