# Esste programa calcula el año en el que una personas puede retirarse del trabajo
# 13 de Octubre de 2021
# Autor: Alan Alvarez

#1. Inicio
#2. Definir el año actual = 2021
anio_actual = 2021
#3. Imprimir "Cual es tu edad?"
print("Cual es tu edad?")
#4. Hacer edad_actual = entrada del usuario
edad_actual = int(input())
#5. Imprimir "A que edad deseas retirarte"
print("A que edad deseas retirarte?")
#6 Hacer edad_retiro = entrada del usuario
edad_de_retiro = int(input())
#7. Hacer años_para_retiro = edad_retiro - edad_actual
anios_para_retiro = edad_de_retiro - edad_actual
#8. Hacer anio_de_retiro = anio_actual + anios_para_retiro
anio_de_retiro = anio_actual + anios_para_retiro
#9. imprimir "Tienes "anios_para_retiro " años antes de que te puedas retirar"
print("Tienes ", anios_para_retiro, "años antes de que te puedas retirar.")
#10. Imprimir "Lo podras hacer en el año" anio_de_retiro
print("Lo podrás hacer en el año", anio_de_retiro)
#11. Fin
