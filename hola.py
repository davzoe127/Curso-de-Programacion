num1 = input("ingrese en primer numero: ")
num2 = input("ingrese el segundo numero: ")

if num1 < num2:
    print(f"{num1}, es menor que {num2}")
elif num1 == num2:
    print("son iguales")
else:
    print(f"{num1}, es mayor que {num2}") 

#segundo
"""
num1 = input("ingrese en primer numero: ")
num2 = input("ingrese el segundo numero: ")
num3 = input("ingrese el tercer numero: ")

if (num1 > num2 and num1 < num3) or (num2 < num3):
    print(f"{num1} es mayor que {num2} y menor que {num3}, o {num2} es menor que {num3}.")
elif (num2 > num1 and num2 < num3) or (num1 < num3):
    print(f"{num2} es mayor que {num1} y menor que {num3}, o {num1} es menor que {num3}.")
elif (num3 > num2 and num3 < num1) or ()
if num1 >= num2 and num1 >= num3: 
    print(f"{num1} es mayor") """

# no se que hice help


#segundo

num1 = 16    
num2 = 14
num3 = 19
if (num1 > num2 and num1 < num3) or (num2 < num3):
    print(f"{num1} es mayor que {num2} y menor que {num3}, o {num2} es menor que {num3}.")
else:
    print("Ninguna de las condiciones se cumplió.")


#tercer

nombre = input("cual es tu nombre?: ")
edad = input("cuantos años tienes?: ")
pais = input("de donde eres?: ")

print(f"hola mi nombre es {nombre}, tengo {edad} años y soy de {pais}")


#cuarto 



num = input("ingrese su calificacion: ")
calif_num = int(num)

if calif_num >= 90 and calif_num <= 100:
    print("obtuviste una A") 
elif calif_num >= 80 and calif_num <= 89:
    print("obtuviste una B")
elif calif_num >= 70 and calif_num <= 79:
    print("obtuviste una C")
elif calif_num >= 60 and calif_num <= 69:
    print("obtuviste una D")
elif calif_num >= 0 and calif_num <= 59:
    print("obtuviste una F")
else: 
    print("error")   



