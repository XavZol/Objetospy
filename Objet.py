#ewhile if

playlist = {}
playlist['canciones'] = []

#funcion principal

def app():
    
    agregar_playlist = True
    
    #agregar playlist
    while agregar_playlist:
        nombre_playlist = input('¿Como deseas nombrar la playlist?\r\n')
        
        if nombre_playlist:
            playlist['nombre'] = nombre_playlist

            #ya tenemos un nombre desactivar el true
            agregar_playlist = False
            
            agregar_canciones()

def agregar_canciones():
    agregar_cancion = True
    
    while agregar_cancion:
        
        nombre_playlist =  playlist['nombre']
        
        pregunta = f'Agrega canciones para la playlist {nombre_playlist}: \r\n'
        pregunta += 'Escribe "X" para dejar de agregar canciones\r\n'
        
        cancion = input(pregunta)
        
        if cancion == 'X':
            #Dejar de agregar canciones 
            agregar_cancion = False
            
            mostrar_resumen()
        else: 
            playlist['canciones'].append(cancion)
            
def mostrar_resumen():
    nombre_playlist = playlist['nombre']
    print(f'PLaylist: {nombre_playlist} \r\n')
    print('Canciones: \r\n')
    for cancion in playlist['canciones']:
        print(cancion)
            
app()