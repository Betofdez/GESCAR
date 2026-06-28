class Operacion:
    def __init__(self, id, valor, tipo, numero_acciones, precio, gastos, fecha):
        self.id = id
        self.valor = valor
        self.tipo = tipo
        self.numero_acciones = numero_acciones
        self.precio = precio
        self.gastos = gastos
        self.fecha = fecha

    def calcular_total(self):
        return self.numero_acciones * self.precio

    def calcular_cargo(self):
        return self.calcular_total() + self.gastos