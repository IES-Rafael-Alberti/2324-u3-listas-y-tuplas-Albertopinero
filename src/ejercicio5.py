def CuentaAtras():
    for i in range(1, 11):
        return i
    
if __name__ == "__main__":
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #proceso
    for i in range(1,11):
    #salida
        print(numbers[-i], end=", ")