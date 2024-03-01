class Fecha:
    # aqui va el codigo
    '''----------------------------------------------------------------
    # Atributos
    ----------------------------------------------------------------'''
    
    dia=0
    mes=0
    anio=0
    
    '''----------------------------------------------------------------
    # Metodos
    ----------------------------------------------------------------'''
    
    def ConsultarDia(self):
        return self.dia
    
    def ConsultarMes(self):
        return self.mes
    
    def ConsultarAnio(self):
        return self.anio
    
    def _init_(dia, mes ,anio):
        self.dia = dia
        self.mes = mes
        self.anio = anio
