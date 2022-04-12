from src.logica.Operaciones import Operaciones

if __name__ == '__main__':
    print("CUSICUNA MUCHA GROZNY - RODRIGUEZ MALLQUI MAYCOL - ORDAYA LOO KIN")

    operacion = Operaciones()
    num1=0
    num2=0

    while True:
        num1 = operacion.ingresoDatos(input("INTRODUCE PRIMER NÚMERO: "))
        num2 = operacion.ingresoDatos(input("INTRODUCE SEGUNDO NÚMERO: "))
        if((type(num1) is float) or (type(num1) is int)) and ((type(num2) is float) or (type(num2) is int)):
            break

    resultado = operacion.suma(num1, num2)
    print("{0:.2f} + {1:.2f} = {2:.2f}".format(num1, num2, resultado))

    resultado = operacion.resta(num1, num2)
    print("{0:.2f} - {1:.2f} = {2:.2f}".format(num1, num2, resultado))

    resultado = operacion.multiplicacion(num1, num2)
    print("{0:.2f} x {1:.2f} = {2:.2f}".format(num1, num2, resultado))

    resultado = operacion.division(num1, num2)
    if (resultado == None):
        print()
    else:
        print("{0:.2f} / {1:.2f} = {2:.2f}".format(num1, num2, resultado))





