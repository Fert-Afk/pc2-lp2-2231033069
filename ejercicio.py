class Pasajero:
    """Pasajero de embarcación fluvial en rutas de Loreto."""
    RUTAS_VALIDAS = ["Iquitos-Nauta", "Iquitos-Yurimaguas",
                     "Iquitos-Pucallpa", "Iquitos-Sta. Rosa"]
    PESO_LIBRE = 15.0
    PESO_MAXIMO = 25.0

    def __init__(self, dni, nombre_completo, edad, peso_equipaje, ruta):
        self.dni = dni
        self.nombre_completo = nombre_completo
        self.edad = edad
        self.peso_equipaje = peso_equipaje
        self.ruta = ruta

    @property
    def dni(self):
        return self.__dni

    @dni.setter
    def dni(self, valor):
        if isinstance(valor, str) and valor.isdigit() and len(valor) == 8:
            self.__dni = valor
        else:
            raise ValueError("DNI no válido: solo 8 digitos permitidos.")

    # Nombre completo
    @property
    def nombre_completo(self):
        return self.__nombre_completo

    @nombre_completo.setter
    def nombre_completo(self, valor):
        if isinstance(valor, str) and len(valor.strip()) > 0:
            self.__nombre_completo = valor.strip()
        else:
            raise ValueError("Nombre completo no válido.")

    # Edad
    @property
    def edad(self):
        return self.__edad

    @edad.setter
    def edad(self, valor):
        if isinstance(valor, int) and valor > 0:
            self.__edad = valor
        else:
            raise ValueError("Edad no válida: debe ser un entero positivo.")

    # Peso del equipaje
    @property
    def peso_equipaje(self):
        return self.__peso_equipaje

    @peso_equipaje.setter
    def peso_equipaje(self, valor):
        if isinstance(valor, (int, float)) and 0 <= valor <= Pasajero.PESO_MAXIMO:
            self.__peso_equipaje = float(valor)
        else:
            raise ValueError(f"Peso no válido: debe estar entre 0 y {Pasajero.PESO_MAXIMO} kg.")

    # Rutas válidas
    @property
    def ruta(self):
        return self.__ruta

    @ruta.setter
    def ruta(self, valor):
        if valor in Pasajero.RUTAS_VALIDAS:
            self.__ruta = valor
        else:
            raise ValueError("Ruta no válida. Revise las rutas válidas en RUTAS_VALIDAS.")
        
    