#Como declarar una variable en python
#siempre todo en minuscula
myvariable="Esta es mi variable del tipo String"
print(myvariable)

my_variable="Esta es otra variable del tipo String"
print(my_variable)

my_int_variable = 10
print(my_int_variable)

my_bool_variable = True
print(my_bool_variable)

my_float_variable = 10.5
print(my_float_variable)

my_complex_variable = 10 + 5
print(my_complex_variable)

#Pasando diferentes argumentos a print(conviertiendo una cadena de texto)

print(my_bool_variable, my_float_variable, my_int_variable, my_complex_variable) 

print("Este es el valor de la variable:", my_complex_variable)

#Variables en una sola linea
nombre, apellido, alias, edad = "Hans", "Rubio", "Docente", 38
print("Mi nombre es: ",nombre, "Mi apellido es: ",apellido, "Mi alias: ",alias, "Miedad es: ",edad)