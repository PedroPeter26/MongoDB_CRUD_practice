from Models.Taxi import Taxi
from CrudBoy import CrudBoy
from Dict_to_Json import Dict_to_Json

class Chofer(CrudBoy):
    def __init__(self, nombre = None, a_paterno = None, a_materno = None, rfc = None, Taxi = None, is_array = None):
        super().__init__()
        is_Array = nombre is None and rfc is None
        if is_Array:
            self.is_array = True
            self.content = []
            self.lista_objetos = []
        else:
            self.nombre = nombre
            self.a_paterno = a_paterno
            self.a_materno = a_materno
            self.rfc = rfc
            self.Taxi = Taxi
            self.is_array = False

    def __str__(self) -> str:
        if self.is_array is True:
            string_resultado = f"Tienes : {len(self.lista_objetos)} objetos.\n"
            for objeto in self.lista_objetos:
                string_resultado += str(objeto) + "\n"
            return string_resultado
        else:
            return f"Chofer: {self.nombre} {self.a_paterno} {self.a_materno}\n\tRFC: {self.rfc}\n\t\tTaxi: {self.Taxi}"

if __name__ == '__main__':
    handler = Chofer()
    jsonTransformer = Dict_to_Json()

    taxi0 = Taxi("GAA-004-A", "Verde", "Toyota", "Corolla", "LE")
    taxi1 = Taxi("FAA-012-A", "Amarillo", "Ram", "Ram 1500", "TRX")
    taxi2 = Taxi("FAA-311-A", "Rojo", "Ford", "Fusion", "SE")

    chofis0 = Chofer("Juan", "Rulfo", "Matrinez", "VECJ880326", taxi0)
    chofis1 = Chofer("Akira", "Toriyama", "Mifune", "BNPA510108XW3", taxi1)
    chofis2 = Chofer("Carlos", "Fuentes", "Macias", "RETD560101OU0", taxi2)

    handler.agregar_objeto(chofis0)
    handler.agregar_objeto(chofis1)
    handler.agregar_objeto(chofis2)

    jsonTransformer.parse_to_dict(handler)
    jsonTransformer.to_json(handler)
    print(jsonTransformer.list_dict)

    jsonTransformer.parse_to_dict(chofis2)
    jsonTransformer.to_json(chofis2)
    print(jsonTransformer.dict)
    # handler.imprimir_objetos()
    # handler.eliminar_objeto(1)
    # handler.imprimir_objeto(2)
    # handler.imprimir_objetos()
    # print("|")
    # print(handler)
    # print(chofis2)