# Autor: Alan Alvarez 
# 1. Inicio
# 2. Definir suma, resta, resultado, entrada, num1, num2
# 3. Imprimir "Que operacion quieres hacer?"
print("Que operacion quieres hacer?")
# 4. entrada = entrada de usuario
entrada = input()
# 5. imprimir "dame el primer numero"
print("Dame el primer numero")
# 6. num1 = entrada del usuario 
num1 = float(input())
# 7. Imprimir "dame el segundo numero"
print("Dame el segundo numero")
# 8. num2 = entrada de usuario
num2 = float(input())
# 9. Si entrada = "suma" entonces, 
resultado = 0
if entrada == "suma":
  resultado = num1 + num2 # 9.1. suma = num1 + num2, 
else:
  resultado = num1 - num2# 9.1. de lo contrario, resta = num1 - num2
# 10. "imprimir "el resultado de la " entrada "es " resultado
print("El resultado de la ", entrada, " es ", resultado)
# 11. Fin
