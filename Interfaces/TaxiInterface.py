from Interfaces.Base_Interface import BaseInterface
from Models.Taxi import Taxi
from Dict_to_Json import Dict_to_Json
from MongoHandler import MongoHandler

# Consts
DB_NAME = 'iotDB'
COLLECTION_NAME = 'Taxis'

class TaxiInterface(BaseInterface):
    def __init__(self):
        self.taxi_model = Taxi()
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
        matricula = input("Ingrese la matrícula del taxi: ")
        color = input("Ingrese el color del taxi: ")
        marca = input("Ingrese la marca del taxi: ")
        modelo = input("Ingrese el modelo del taxi: ")
        submarca = input("Ingrese la submarca del taxi: ")
        return Taxi(matricula, color, marca, modelo, submarca)

    def show_menu(self):
        print("\nMenú de Taxi:")
        print("1. Crear Taxi")
        print("2. Leer Taxis")
        print("3. Actualizar Taxi")
        print("4. Eliminar Taxi")
        print("5. Volver al menú principal")

    def create(self):
        taxi = self.create_instance()
        taxi_dict = self.jsonHandler.parse_to_dict(taxi)
        success = self.mongoHandler.mongoInsertOne(DB_NAME, COLLECTION_NAME, taxi_dict)
        if success == False:
            self.taxi_model.agregar_objeto(taxi)
            self.jsonHandler.parse_to_dict(self.taxi_model)
            self.jsonHandler.to_json(self.taxi_model, "../rsc/Taxi.json")
            print("Taxi creado localmente: ", taxi, "\n")
        else:
            print("Viaje creado e insertado en la colección:", taxi, "\n")

    def read(self):
        self.taxi_model.load('rsc/Taxi.json', Taxi)
        self.taxi_model.imprimir_objetos()

    def update(self):
        self.read()
        index = int(input("Seleccione el índice del taxi a actualizar: ")) - 1
        taxi = self.create_instance()
        self.taxi_model.editar_objeto(index, taxi)
        self.jsonHandler.parse_to_dict(self.taxi_model)
        self.jsonHandler.to_json(self.taxi_model, "../rsc/Taxi.json")
        print("Taxi actualizado:", taxi)

    def delete(self):
        self.read()
        index = int(input("Seleccione el índice del taxi a eliminar: ")) - 1
        self.taxi_model.eliminar_objeto(index)
        self.jsonHandler.parse_to_dict(self.taxi_model)
        self.jsonHandler.to_json(self.taxi_model, "../rsc/Taxi.json")
        print("Taxi eliminado")

if __name__ == "__main__":
    interface = TaxiInterface()
    interface.run()
