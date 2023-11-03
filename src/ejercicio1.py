'''Ejercicio 3.1.1¶
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) 
en una lista y la muestre por pantalla'''
import time
def AsignaturasCurso(subjects):
    subjects = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
    return subjects
    


if __name__ == "__main__":
    #salida
    subjects = ['Matemáticas', 'Física', 'Química', 'Historia', 'Lengua']
    print("Las asignaturas de este año son:...")
    time.sleep(2)
    print(subjects)