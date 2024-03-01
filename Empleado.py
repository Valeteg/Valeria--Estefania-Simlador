from Fecha import Fecha
class Empleado:
    #aqui va el codigo

    '''------------------
    #Atributos
    ------------------'''

    nombre=''
    apellidos=''
    '''-----------------
    # 1 = Masculino y 2 = Femenino
    -----------------'''
    sexo=0
    salario=0

    '''---------------------------
    # Asoiaciaciones
    ----------------------------'''

    fechaNacimiento = Fecha()
    fechaIngreso = Fecha()

    """-----------------------------
    Metodos
    -----------------------------"""

    def CambiarSalaraio(self, nSalario):
        #Aquí va el codigo
        self.salario = nSalario
        return  'su nuevo salario es: '+self.salario

    def ConsultarSalario(self):
        #Aquí va el codigo
        return self.salario

    def AumentoSalarial(self):
        #Aquí va el codigo
        aumento = self.salario*0.05
        nSalario = self.salario+aumento
        self.salario = nSalario
        return  'su nuevo salario es: '+self.salario

    def DuplicarSalario(self):
        # Forma 1
        nuevoSalario = self.salario*2
        self.salario = nuevoSalario
        # # forma2
        # self.salario *= 2

    def CalcularSalarioAnual(self):
        #Forma 1
        salarioAnual=self.salario*12
        return salarioAnual
        #Forma2
        # return self.salario*12

    def ConsultarDiaCumpleaños(self):
        return self.FechaNacimiento.ConsultarDia()

    def CalcularImpuesto(self):
        #Forma 1
        total = self.CalcularSalarioAnual()
        total = total * (19.5/100)
        return total

        #Forma 2

        return self.CalcularSalarioAnual()*0.195
