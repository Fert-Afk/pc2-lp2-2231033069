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
        
    @property
    def categoria_edad(self):
        """Clasificación por edad."""
        if self.edad < 12:
            return "Niño"
        elif self.edad < 60:
            return "Adulto"
        else:
            return "Adulto mayor"

    @property
    def tarifa_base(self):
        """Tarifa base según ruta."""
        tarifas = {
            "Iquitos-Nauta": 30.0,
            "Iquitos-Yurimaguas": 80.0,
            "Iquitos-Pucallpa": 100.0,
            "Iquitos-Sta. Rosa": 50.0
        }
        return tarifas[self.ruta]

    @property
    def recargo_equipaje(self):
        """S/. 2 por kg sobre los 15 kg libres."""
        exceso = max(0, self.peso_equipaje - Pasajero.PESO_LIBRE)
        return exceso * 2.0

    @property
    def tarifa_total(self):
        """Base + recargo, con descuento si aplica."""
        total = self.tarifa_base + self.recargo_equipaje
        # Descuento del 50% para niños
        if self.categoria_edad == "Niño":
            total *= 0.5
        return total
    
    def __str__(self):
        return (
            f"=== BOLETA DE EMBARQUE ===\n"
            f"DNI: {self.dni}\n"
            f"Nombre: {self.nombre_completo}\n"
            f"Edad: {self.edad} ({self.categoria_edad})\n"
            f"Ruta: {self.ruta}\n"
            f"Peso equipaje: {self.peso_equipaje} kg\n"
            f"Tarifa base: S/. {self.tarifa_base:.2f}\n"
            f"Recargo equipaje: S/. {self.recargo_equipaje:.2f}\n"
            f"TOTAL A PAGAR: S/. {self.tarifa_total:.2f}\n"
        )

# Programa de prueba
if __name__ == "__main__":
    p1 = Pasajero("12345678", "Juan Pérez", 25, 20, "Iquitos-Nauta")
    print(p1)
            
    p2 = Pasajero("87654321", "María López", 10, 18, "Iquitos-Pucallpa")
    print(p2)
    
