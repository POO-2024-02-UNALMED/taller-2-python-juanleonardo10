class Asiento:
    def _init_(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiar_color(self, nuevo_color):
        if nuevo_color in ["rojo", "verde", "amarillo", "negro", "blanco"]:
            self.color = nuevo_color

class Auto:

    def _init_(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos  # Lista de objetos Asiento
        self.marca = marca
        self.motor = motor  # Objeto Motor
        self.registro = registro
        cantidadCreados = 0

    def cantidad_asientos(self):
        # Cuenta cuántos elementos en 'asientos' son objetos de la clase Asiento
             return sum(1 for asiento in self.asientos if isinstance(asiento, Asiento))

    def verificar_integridad(self):
        # Verifica si el registro del Auto, Motor y cada Asiento es el mismo
        if self.registro != self.motor.registro:
            return "Las piezas no son originales"
        
        for asiento in self.asientos:
            if asiento is not None and asiento.registro != self.registro:
                return "Las piezas no son originales"
            else:
                return "Auto original"
    
    class Motor:
     def _init_(self, numero_cilindros, tipo, registro):
        self.numero_cilindros = numero_cilindros
        self.tipo = tipo
        self.registro = registro

     def cambiar_registro(self, nuevo_registro):
        # Cambia el número de registro
        self.registro = nuevo_registro

     def asignar_tipo(self, nuevo_tipo):
        # Solo permite cambiar a "eléctrico" o "gasolina"
        if nuevo_tipo in ["eléctrico", "gasolina"]:
            self.tipo = nuevo_tipo