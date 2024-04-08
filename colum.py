from ponerficha import valoresFC

nombre_jugador = input("Nombre del jugador : ")

tablero = [['.','.','.','.','.','.','.','.','.','.'],
           ['.','.','.','.','.','.','.','.','.','.'],
           ['.','.','.','.','.','.','.','.','.','.']]

print(f'Bienvenidos  {nombre_jugador}')
print('Este es el tablero: ')
print('porfavor ingre el numero de columna y fila en la cual pensas que esta el barco')

for fila in tablero:
    print(fila)

filaB = 0
columnaB = 0

for i in range(0,len(tablero)):
    for j in range(0,len(tablero)):
        valoresFC(fila=filaB,columna=columnaB)
        

