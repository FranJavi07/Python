
try:
    edad = int(input("Edad:"))

    if edad<12:

        precio : 5
    
    elif edad < 18:

        precio : 10
    
    elif edad > 65:

        precio : 4
    
    

except ValueError:
        print("No has introducido un número entero. Intenta de nuevo.")
    else:
            print("La entrada te costara", precio "€")






