'''Ejercicio 3.1.2¶
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> sobre cada una de las asignaturas de la lista.'''
def Asignaturas(asignatura):
    subjects = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
    for asignatura in subjects:
        return asignatura


if __name__ == "__main__":
    subjects = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
    #proceso
    for asignatura in subjects:
    #salida
        print("Yo estudio " + asignatura)