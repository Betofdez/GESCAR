class Posicion:
    def __init__(self, valor):
        self.valor = valor
        self.numero_acciones = 0
        self.inversion_total = 0

    def agregar_compra(self, operacion):
        self.numero_acciones += operacion.numero_acciones
        self.inversion_total += operacion.calcular_cargo()

    def agregar_venta(self, operacion):
        if self.numero_acciones <= 0:
            return

        precio_medio = self.precio_medio()
        coste_acciones_vendidas = operacion.numero_acciones * precio_medio

        self.numero_acciones -= operacion.numero_acciones
        self.inversion_total -= coste_acciones_vendidas

        if self.numero_acciones <= 0:
            self.numero_acciones = 0
            self.inversion_total = 0

    def precio_medio(self):
        if self.numero_acciones == 0:
            return 0

        return self.inversion_total / self.numero_acciones

    def valor_actual(self):
        return self.numero_acciones * self.valor.cotizacion_actual

    def rentabilidad(self):
        return self.valor_actual() - self.inversion_total

    def rentabilidad_porcentaje(self):
        if self.inversion_total == 0:
            return 0

        return (self.rentabilidad() / self.inversion_total) * 100