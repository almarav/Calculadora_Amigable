""" Programa calculadora artimética amigable#
    Realiza las 4 operaciones (+,-,* /) 
    incorpora al modulo calculadora_aritmetica.py
    Almeiro Arango Avila
    Mayo 22-2021 """

#---------------- Zona librerias------------
import calculadora_aritmetica as calc

#======================================================================
#          E S P A C I O    D E    T R A B A J O     A L U M N O
# ====================================================================

#----------Definición de Funciones (Dividir)------------
def menu_operaciones():
  print("==================================================")
  print("| Menu")
  print("==================================================")
  print("| Ingresa un numero para realizar la operacion.")
  print("==================================================")
  print("| 1. Calcular suma: (1)")
  print("==================================================")
  print("| 2. Calcular la resta: (2)")
  print("==================================================")
  print("| 3. Calcular multiplicación: (3)")
  print("==================================================")
  print("==================================================")
  print("| 4. Calcular división: (4)")
  print("==================================================")
   
  opcion = input("Elija la operación a realizar: ")
  return opcion

operacion=menu_operaciones()

if operacion > "4":
  print("Opcion Invalida")
elif operacion <= "0":
  print("Opcion Invalida")
else:
  numero1 = float(input("Digite el primer numero: "))
  numero2 = float(input("Digite el segundo numero: "))
  if operacion == "1":
    print("El resultado de la suma es: ",calc.sumar_numeros(numero1,numero2))
  elif operacion == "2":
    print("El resultado de la resta es: ",calc.restar_numeros(numero1,numero2))
  elif operacion == "3":
    print("El resultado de la resta es: ",calc.multiplicar_numeros(numero1,numero2))
  elif operacion == "4":
    if numero1 ==0:
      print("No se puede dividir por cero")
    elif numero2 ==0:
      print("No se puede dividir por cero")
    else: 
      print("El resultado de la resta es: ",calc.dividir_numeros(numero1,numero2))
  
print('FIN DEL PROGRAMA')