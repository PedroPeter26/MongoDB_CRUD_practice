from Models.Chofer import Chofer
from Models.Taxi import Taxi
from CrudBoy import CrudBoy
from Dict_to_Json import Dict_to_Json

class Viaje(CrudBoy):
    def __init__(self, distancia = None, destino = None, precio = None, Chofer = None, is_array = None):
        super().__init__()
        is_array = distancia is None and destino is None
        if is_array:
            self.is_array = True
            self.content = []
            self.lista_objetos = []
        else:
            self.distancia = distancia
            self.destino = destino
            self.precio = precio
            self.Chofer = Chofer
            self.is_array = False

    def __str__(self):
        if self.is_array is True:
            string_resultado = f"Tienes : {len(self.lista_objetos)} objetos.\n"
            for objeto in self.lista_objetos:
                string_resultado += str(objeto) + "\n"
            return string_resultado
        else:
            return f"Viaje a: {self.destino}, Distancia: {self.distancia} km, Precio: $ {self.precio}\n\tChofer: {self.Chofer}"

if __name__ == "__main__":
    handler = Viaje(None, None, None, None)
    jsonTransformer = Dict_to_Json()

    taxi0 = Taxi("FAA-012-A", "Amarillo", "Ram", "Ram 1500", "TRX")
    taxi1 = Taxi("RKA-467-A", "Azul", "Chevrolet", "Spark", "LS")
    taxi2 = Taxi("RKA-200-A", "Blanco", "Nissan", "Versa", "Advance")

    chofis0 = Chofer("Juan", "Rulfo", "Matrinez", "VECJ880326", taxi0)
    chofis1 = Chofer("Akira", "Toriyama", "Mifune", "BNPA510108XW3", taxi1)
    chofis2 = Chofer("Carlos", "Fuentes", "Macias", "RETD560101OU0", taxi2)

    viaje0 = Viaje(50, "Conney Islan", 350, chofis0)
    viaje1 = Viaje(20, "Edo. Mex", 250, chofis1)
    viaje2 = Viaje(62, "Guadalupe, NL", 400, chofis2)

    handler.agregar_objeto(viaje0)
    handler.agregar_objeto(viaje1)
    handler.agregar_objeto(viaje2)

    jsonTransformer.parse_to_dict(handler)
    jsonTransformer.to_json(handler, "../rsc/Viaje.json")
    print(jsonTransformer.list_dict)

    handler.load('rsc/Viaje.json', Viaje)
    print(handler)
