def NotasCurso():
    subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    for asignatura in subjects:
        return asignatura
    for i in range(len(subjects)):
        return i
    
if __name__ == "__main__":
    subjects = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    notas = []
    for asignatura in subjects: 
    #salida
        puntuacion = input("¿Qué nota has sacado en " + asignatura + "?: ")

    #proceso
        notas.append(puntuacion)
    for i in range(len(subjects)):

    #salida
        print("En " + subjects[i] + " has sacado " + notas[i])