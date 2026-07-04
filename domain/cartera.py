from domain.posicion import Posicion

class Cartera:
    def __init__(self, operaciones):
        self.operaciones = operaciones
        self.posiciones = self._calcular_posiciones()

    def _calcular_posiciones(self):
        posiciones = {}

        for operacion in self.operaciones:
            ticker = operacion.valor.ticker

            if ticker not in posiciones:
                posiciones[ticker] = Posicion(operacion.valor)

            if operacion.tipo == "COMPRA":
                posiciones[ticker].agregar_compra(operacion)
            elif operacion.tipo == "VENTA":
                posiciones[ticker].agregar_venta(operacion)

        return [
            posicion
            for posicion in posiciones.values()
            if posicion.numero_acciones > 0
        ]

    def valor_total(self):
        return sum(posicion.valor_actual() for posicion in self.posiciones)

    def inversion_total(self):
        return sum(posicion.inversion_total for posicion in self.posiciones)

    def rentabilidad_total(self):
        return self.valor_total() - self.inversion_total()

    def rentabilidad_porcentaje_total(self):
        inversion = self.inversion_total()

        if inversion == 0:
            return 0

        return (self.rentabilidad_total() / inversion) * 100

    def numero_valores(self):
        return len(self.posiciones)
    
    def obtener_posicion_por_ticker(self, ticker):
        for posicion in self.posiciones:
            if posicion.valor.ticker == ticker:
                return posicion

        return None