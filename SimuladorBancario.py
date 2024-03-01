from CDT import CDT
from CuentaAhorros import CuentaAhorros
from CuentaCorriente import CuentaCorriente

class SimuladorBancario:
    #aqui va el codigo

    '''-----------------------------------
    # Atributos
    -------------------------------------'''
    cedula=0
    nombre=''
    mesActual=0
    '''-----------------------------------------
    # Asociaciones
    --------------------------------------------'''

    saldoAhorros = CuentaAhorros()
    saldoCorriente = CuentaCorriente() 

    '''-----------------------------------------
    # Metodo
    --------------------------------------------'''

    def ConsultarSaldoTotal (self):
        #aqui va el codigo
        return "su saldo total es: "+ self.CuentaCorriente.saldoCorriente() + self.CuentaAhorros.saldoAhorros()
    
    def ConsignarCuentaCorriente(self, deposito):
        #aqui va el codigo 
        return self.CuentaCorriente.DepositarValor(deposito)
    
    def CuentaAhorrosCorriente(self):
        #aqui va el codigo 
        saldoAhorros= self.CuentaAhorros.ConsultarSaldo()
        self.CuentaAhorros.RetirarValor(saldoAhorros)
        self.CuentaCorriente.DepositarValor(saldoAhorros)
        return "usted ha depositado"+ self.saldoAhorros + " en cuenta corriente"
    
    def ConsultarCuentaCorriente(self):
        # aqui va el codigo
        return "su saldo es: " + self.CuentaCorriente.saldoCorriente()
    
    def retirarAhorro(self, retiro):
        # aqui va el codigo 
        return "usted a retirado:" + retiro + "sus saldo en cuenta es:" + self.CuentaAhorros.saldoAhorros()
    
    def retiroAhorrosCorriente(self):
        # aqui va el codigo
        saldoAhorros= self.CuentaAhorros.ConsultarSaldo()
        saldoCorriente= self.CuentaCorriente.ConsultarSaldo()
        self.CuentaAhorros.RetirarValor(saldoAhorros)
        self.CuentaCorriente.RetirarValor(saldoCorriente)
        return "a retirado un valor de " + self.saldoAhorros + "de su cuenta de ahorros y " + self.saldoCorriente + "de su cuenta corriente."
    
    def duplicarSaldoAhorros(self):
        #aqui va el codigo 
        return "el saldo duplicado es de " + self.saldoAhorros()*2