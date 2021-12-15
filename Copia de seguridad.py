import random as rd

num = rd.randint(1, 100)
lista = [0,100]
maximo = [100]
minimo = [0]
a = 0
i = 0

M = 100
m = 0

while(bool(a)==False):

    num1 = input("Ingrese un número entero: ")

    if num1.isnumeric() != True:
        print("Ingrese un valor numerico")
        num1 = input("Ingrese un número entero: ")
    
    else:
        num1 = int(num1)
        lista.append(num1)

        if num1 != num:

            if num1 > num:
                bool(1)
                maximo.append(num1)
                M = min(maximo)
                print("\033[1;31m" + f"Error, el número está entre {M} y {m}")
                #print("\033[1;31m" + f"El número es incorrecto, está entre [{M}, {m}]")
                i += 1

            if num1 < num:
                minimo.append(num1)
                m = max(minimo)
                print("\033[1;31m" + f"Error, el número está entre {M} y {m}")
                #print("\033[1;31m" + f"El número está entre [{M}, {m}], elige nuevamente: ")
                i += 1

        
        else:

            if i == 1:
                bool(1)
                print("\033[1;31m" + f">>>>Correcto, el  número es {num}, lo realizó en 1 intento.")
                print(f"Los números que eligió durante el juego son: {lista}")
            else:
                bool(1)
                print("\033[1;32m" + f">>>>Correcto, el  número es {num}, lo realizó en {i+1} intentos.")
                print(f"Los números que eligió durante el juego son: {lista}")
            a = rd.random()

"""
Notas:

    -Hacer que si el valor ingresado expanda aún más el rango, el programa lo impida.
    - Almacenar el historial de los numeros ingresados 
    - Print cambie de colores ✓
    - Que se juege solo
    - poner musica 


"""