file = open('miarchivo.txt', 'w')
file.write('Este es mi primer archivo txt \n')
file.close()

file = open('miarchivo.txt', 'r+')
file.readline()
file.write('Segunda vez que ingreso a mi archivo txt.\n')

file.seek(0)
print(file.read())
file.close()