from Interfaces.Base_Interface import BaseInterface
from Models.Taxi import Taxi
from Dict_to_Json import Dict_to_Json
from MongoHandler import MongoHandler
import os
import json

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
        if success is False:
            self.taxi_model.agregar_objeto(taxi)
            self.jsonHandler.parse_to_dict(self.taxi_model)
            self.jsonHandler.to_json(self.taxi_model, "../rsc/Taxi.json")
            print("Taxi creado localmente: ", taxi, "\n")
        else:
            print("Viaje creado e insertado en la colección:", taxi, "\n")
            self.sync_json("../rsc/Taxi.json")

    def read(self):
        success = self.mongoHandler.mongoShowDocs(DB_NAME, COLLECTION_NAME)
        if success is False:
            print("\nLectura realizada localmente:\n")
            self.taxi_model.load('rsc/Taxi.json', Taxi)
            self.taxi_model.imprimir_objetos()
            return False

    def update(self):
        success = self.read()
        if success is False:
            index = int(input("Seleccione el índice del taxi a actualizar (localmente): ")) - 1
            taxi = self.create_instance()
            self.taxi_model.editar_objeto(index, taxi)
            self.jsonHandler.parse_to_dict(self.taxi_model)
            self.jsonHandler.to_json(self.taxi_model, "../rsc/Taxi.json")
            print("Taxi actualizado localmente\n:", taxi)
        else:
            idObjeto = input("Ingrese el _id del objeto a modificar: ")
            taxi = self.create_instance()
            taxi_dict = self.jsonHandler.parse_to_dict(taxi)
            self.mongoHandler.mongoUpdateOne(DB_NAME, COLLECTION_NAME, idObjeto, taxi_dict)

    def delete(self):
        success = self.read()
        if success is False:
            index = int(input("Seleccione el índice del taxi a eliminar: ")) - 1
            self.taxi_model.eliminar_objeto(index)
            self.jsonHandler.parse_to_dict(self.taxi_model)
            self.jsonHandler.to_json(self.taxi_model, "../rsc/Taxi.json")
            print("Taxi eliminado")
        else:
            idObjeto = input("Ingrese el _id del objeto a eliminar: ")
            self.mongoHandler.mongoDeleteOne(DB_NAME, COLLECTION_NAME, idObjeto)

    def sync_json(self, json_filepath):
        if os.path.exists(json_filepath):
            with open(json_filepath, 'r') as file:
                try:
                    data = json.load(file)
                    if data:
                        insert_success = self.mongoHandler.mongoInsertMany(DB_NAME, COLLECTION_NAME, data)
                        if insert_success:
                            with open(json_filepath, 'w') as file:
                                json.dump([], file)
                            print("Contenido del JSON insertado en la colección y archivo JSON vaciado.")
                        else:
                            print("Error al insertar el contenido del JSON en la colección.")
                except json.JSONDecodeError:
                    print("Error al leer el archivo JSON.")

if __name__ == "__main__":
    interface = TaxiInterface()
    interface.run()
