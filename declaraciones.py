# Hace un salto de linea
print("¿Cómo se llama?")
nombre = input()
# La letra f en el print(): Es una forma de formatear cadenas de texto en Python que se 
# introdujo en la versión 3.6. Permite incluir expresiones dentro 
# de una cadena de texto que se evalúan en tiempo de ejecución.
print(f"Me alegro de conocerle, {nombre}")

# Sin un salto de linea
print("¿Cómo se llama? ", end="")
nombre = input()
print(f"Me alegro de conocerle, {nombre}")

# Otra solución, más compacta, es aprovechar que a la función input() se le puede enviar un argumento 
# que se escribe en la pantalla (sin añadir un salto de línea)
nombre = input("¿Cómo se llama? ")
print(f"Me alegro de conocerle, {nombre}")