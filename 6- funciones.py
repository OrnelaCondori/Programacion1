#El error es que dentro de una funcion tiene que utlizar los parametros con los que sea crea
#luego estos valores son remplazados por los ingresados
#(Cuando se llama a la funcion)
#por eso en el cuerpo, tiene que hacerse referencia a y b(los parametros definidos). no x o y (estos son los valores con los que trabaja cuando se llama a la funcion)
def most(a, b):
    if (a>b):
        return a
    else:
        return b

def least(a,b):
    if (a>b):
        return b
    else:
        return a

x = int(input("Un número : "))
y = int(input("Ingrese otro numero: "))

print(most(x-3, least(x+2, y-5)))
