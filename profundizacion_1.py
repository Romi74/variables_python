# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio

#Intento realizar ejercio de avanzada

numero_1 = float(input("ingrese un valor: "))
numero_2 = float(input("ingrese un valor: "))

suma = numero_1 + numero_2
resta = numero_1 - numero_2
Multiplicacion = numero_1 * numero_2
división = numero_1 / numero_2
Exponente = numero_1 ** numero_2


operacion = input("seleccione la operacion a realizar\n\
  S s = suma\n\
  R r = resta\n\
  M m = multiplicación\n\
  D d = división\n\
  P p = potencia: ")



if operacion == "s" or operacion == "S" :
  print("el resultado de la suma entre {} y {} es {} ".format(numero_1, numero_2, suma))
elif operacion == "r" or operacion == "R" :
  print("el resultado de la resta entre {} y {} es {} ".format(numero_1, numero_2, resta))
elif operacion =="M" or operacion == "m" :
  print("el resultado de la multiplicacin entre {} y {} es {} ".format(numero_1, numero_2, Multiplicacion))
elif operacion == "d" or operacion == "D" :
  print("el resultado de la division entre {} y {} es {} ".format(numero_1, numero_2, división))
elif operacion == "P" or operacion == "p" :
  print("el resultado de la potencia entre {} y {} es {} ".format(numero_1, numero_2, Exponente))
else: 
  print("la operacion seleccionada no es valida")

print("esto es mi primera calculadora")
