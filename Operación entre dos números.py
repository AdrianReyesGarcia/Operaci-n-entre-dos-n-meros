# -*- coding: utf-8 -*-
"""
Created on Sun Jul 14 17:33:29 2024

@author: Adrian
Operación entre dos números
"""
num1 = int (input ("Dame el número 1: "))
num2 = int (input ("Dame el número 2: "))

operacion = input ("Introduce una operación (+, -, *, /):")

match operacion:
    
    case "+": 
        res = num1 + num2
    case "-":
        res = num1 - num2
    case "*":
        res = num1 * num2
    case "/":
        res = num1 / num2
    
print(f"El Resultado de {num1} {operacion} {num2} es igual a: {res}")
