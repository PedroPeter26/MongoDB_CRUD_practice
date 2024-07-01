from CrudBoy import CrudBoy
from Dict_to_Json import Dict_to_Json

class Taxi(CrudBoy):
    def __init__(self, matricula = None, color = None, marca = None, modelo = None, submarca = None, is_array = None):
        super().__init__()
        is_array = matricula is None and color is None
        if is_array:
            self.is_array = True
            self.content = []
            self.lista_objetos = []
        else:
            self.matricula = matricula
            self.color = color
            self.marca = marca
            self.modelo = modelo
            self.submarca = submarca
            self.is_array = False

    def __str__(self):
        if self.is_array is True:
            string_resultado = f"Tienes : {len(self.lista_objetos)} objetos.\n"
            for i, objeto in enumerate(self.lista_objetos, start=1):
                string_resultado += f"{i}. {objeto}\n"
            return string_resultado
        else:
            return f"Matricula: {self.matricula}, Color: {self.color}, Marca: {self.marca}, Modelo: {self.modelo}, Submarca: {self.submarca}"

if __name__=='__main__':
    handler = Taxi()

    jsonTransformer = Dict_to_Json()

    taxi1 = Taxi("FAA-012-A", "Amarillo", "Ram", "Ram 1500", "TRX")
    taxi2 = Taxi("FAA-311-A", "Rojo", "Ford", "Fusion", "SE")
    taxi3 = Taxi("GAA-004-A", "Verde", "Toyota", "Corolla", "LE")
    taxi4 = Taxi("RKA-467-A", "Azul", "Chevrolet", "Spark", "LS")
    taxi5 = Taxi("RKA-200-A", "Blanco", "Nissan", "Versa", "Advance")

    taxi_nuevo = Taxi("FAA-357-A", "Plateado", "Toyota", "Highlander", "XLE")

    handler.agregar_objeto(taxi1)
    handler.agregar_objeto(taxi2)
    handler.agregar_objeto(taxi3)
    handler.agregar_objeto(taxi4)
    handler.agregar_objeto(taxi5)

    print(handler)
    print(taxi_nuevo)

    jsonTransformer.parse_to_dict(taxi_nuevo)
    jsonTransformer.parse_to_dict(handler)
    jsonTransformer.to_json(handler, "../rsc/Taxi.json")

    # print(jsonTransformer.list_dict)
    # print(jsonTransformer.dict)
