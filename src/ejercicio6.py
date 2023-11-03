def NotasFinalCurso():
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    aprobada = []
    for subject in asignaturas:
        nota = float(input("¿Qué nota has sacado en " + subject + "?"))
        if nota >= 5:
            aprobada.append(subject)
    for subject in aprobada:
        asignaturas.remove(subject)
    return subject  


if __name__ == "__man__":
    asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
    aprobada = []
    #proceso
    for subject in asignaturas:
        nota = float(input("¿Qué nota has sacado en " + subject + "?"))
        if nota >= 5:
            aprobada.append(subject)
    for subject in aprobada:
        asignaturas.remove(subject)

    #salida
    print("Tienes que repetir " + str(asignaturas))