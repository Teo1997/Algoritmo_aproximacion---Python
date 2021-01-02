# numero al que se le calculara la raiz cuadrada
objetivo = int(input('Escoge un numero: '))

# margen de error para encontrar esa raiz
epsilon = 0.0001

# valor es que ira sumando secuencialmente hasta encontrar la raiz 
paso = epsilon**2 

# se comenzara a buscar la raiz desede 0.0 en adelante
respuesta = 0.0

# mientras que respuesta al cuadrado no sea igual al objetivop, este while se seguira ejecutando

while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
    print(abs(respuesta**2 - objetivo), respuesta)
    respuesta += paso

# respuesta <= objetivo: codigo defensivo; si respuesta es mayor a objetivo, el while seguira infinitamente, y nunca encontrarea la raiz
if abs(respuesta**2 - objetivo) >= epsilon:
    print(f'No se encontro la raiz cuadrada {objetivo}')
else:
    print(f'La raiz cudrada de {objetivo} es {respuesta}')