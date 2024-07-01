from Interfaces.Base_Interface import BaseInterface
from Interfaces.ChoferInterface import ChoferInterface
from Models.Viaje import Viaje
from Dict_to_Json import Dict_to_Json
from MongoHandler import MongoHandler

# Consts
DB_NAME = 'iotDB'
COLLECTION_NAME = 'Viajes'

class ViajeInterface(BaseInterface):
    def __init__(self):
        self.viaje_model = Viaje()
        self.options = {
            '1': self.create,
            '2': self.read,
            '3': self.update,
            '4': self.delete,
            '5': None  # Volver al menú principal
        }
        self.jsonHandler = Dict_to_Json()
        self.mongoHandler = MongoHandler()

    def create_instance(self):
        distancia = input("Ingrese la distancia del viaje: ")
        destino = input("Ingrese el destino del viaje: ")
        precio = input("Ingrese el precio del viaje: ")
        chofer_interface = ChoferInterface()
        chofer = chofer_interface.create_instance()
        return Viaje(distancia, destino, precio, chofer)

    def show_menu(self):
        print("\nMenú de Viaje:")
        print("1. Crear Viaje")
        print("2. Leer Viajes")
        print("3. Actualizar Viaje")
        print("4. Eliminar Viaje")
        print("5. Volver al menú principal")

    def create(self):
        viaje = self.create_instance()
        viaje_dict = self.jsonHandler.parse_to_dict(viaje)
        success = self.mongoHandler.mongoInsertOne(DB_NAME, COLLECTION_NAME, viaje_dict)
        if success == False:
            self.viaje_model.agregar_objeto(viaje)
            self.jsonHandler.parse_to_dict(self.viaje_model)
            self.jsonHandler.to_json(self.viaje_model, "../rsc/Viaje.json")
            print("Viaje creado localmente:", viaje, "\n")
        else:
            print("Viaje creado e insertado en la colección:", viaje, "\n")

    def read(self):
        self.viaje_model.load('rsc/Viaje.json', Viaje)
        self.viaje_model.imprimir_objetos()

    def update(self):
        self.read()
        index = int(input("Seleccione el índice del viaje a actualizar: ")) - 1
        viaje = self.create_instance()
        self.viaje_model.editar_objeto(index, viaje)
        self.jsonHandler.parse_to_dict(self.viaje_model)
        self.jsonHandler.to_json(self.viaje_model, "../rsc/Viaje.json")
        print("Viaje actualizado:", viaje)

    def delete(self):
        self.read()
        index = int(input("Seleccione el índice del viaje a eliminar: ")) - 1
        self.viaje_model.eliminar_objeto(index)
        self.jsonHandler.parse_to_dict(self.viaje_model)
        self.jsonHandler.to_json(self.viaje_model, "../rsc/Viaje.json")
        print("Viaje eliminado")


if __name__ == "__main__":
    interface = ViajeInterface()
    interface.run()
