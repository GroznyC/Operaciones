class Operaciones():
    def suma(self, sumando1, sumando2):
        for n in (sumando1,sumando2):
            if not isinstance(n,int) and not isinstance(n,float):
                raise TypeError("No es un int, ni un float.")
        return sumando1+sumando2

    def resta(self, minuendo, sustraendo):
        for n in (minuendo,sustraendo):
            if not isinstance(n,int) and not isinstance(n,float):
                raise TypeError("No es un int, ni un float.")
        return minuendo-sustraendo

    def multiplicacion(self, multiplicando, multiplicador):
        for n in (multiplicando,multiplicador):
            if not isinstance(n,int) and not isinstance(n,float):
                raise TypeError("No es un int, ni un float.")
        return multiplicando*multiplicador


    def ingresoDatos(self,dato):
        if (not type(dato) is float) or (not type(dato) is int):
            try:
                dato=float(dato)
            except ValueError:
                print(f"El dato ingresado \"{dato}\" no se puede convertir a float")
                exit(2)
        return dato
    #TODO Falta hacer
    def validacionDatos(self,numero):
        while (not type(numero) is int) or (not type(numero) is int):
            numero=int(input)