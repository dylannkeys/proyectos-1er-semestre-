from random import sample

def password_generator(longitud):

    abc_minusculas = "abcdefghijklmnopqrstuvwxyz"
    abc_mayusculas = abc_minusculas.upper()
    simbolos = "{}[]()*;/,_-@"
    numeros = "1234567890"
    secuencia= abc_minusculas + abc_mayusculas + simbolos + numeros

    password_union = sample (secuencia, longitud)
    password_result = "".join(password_union)
    return password_result

password = password_generator(12)

print ("Contraseña ", password)

    