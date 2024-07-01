from Interfaces.Base_Interface import BaseInterface
from Interfaces.TaxiInterface import TaxiInterface
from Models.Chofer import Chofer
from Dict_to_Json import Dict_to_Json

class ChoferInterface(BaseInterface):
    def __init__(self):
        self.chofer_model = Chofer()
        self.options = {
            '1': self.create,
            '2': self.read,
            '3': self.update,
            '4': self.delete,
            '5': None  # Volver al menú principal
        }
        self.jsonHandler = Dict_to_Json()

    def create_instance(self):
        nombre = input("Ingrese el nombre del chofer: ")
        a_paterno = input("Ingrese el apellido paterno del chofer: ")
        a_materno = input("Ingrese el apellido materno del chofer: ")
        rfc = input("Ingrese el RFC del chofer: ")
        taxi_interface = TaxiInterface()
        taxi = taxi_interface.create_instance()
        return Chofer(nombre, a_paterno, a_materno, rfc, taxi)

    def show_menu(self):
        print("\nMenú de Chofer:")
        print("1. Crear Chofer")
        print("2. Leer Choferes")
        print("3. Actualizar Chofer")
        print("4. Eliminar Chofer")
        print("5. Volver al menú principal")

    def create(self):
        chofer = self.create_instance()
        self.chofer_model.agregar_objeto(chofer)
        self.jsonHandler.parse_to_dict(self.chofer_model)
        self.jsonHandler.to_json(self.chofer_model, "../rsc/Chofer.json")
        print("Chofer creado:", chofer)

    def read(self):
        self.chofer_model.load('rsc/Chofer.json', Chofer)
        self.chofer_model.imprimir_objetos()

    def update(self):
        self.read()
        index = int(input("Seleccione el índice del chofer a actualizar: ")) - 1
        chofer = self.create_instance()
        self.chofer_model.editar_objeto(index, chofer)
        self.jsonHandler.parse_to_dict(self.chofer_model)
        self.jsonHandler.to_json(self.chofer_model, "../rsc/Chofer.json")
        print("Chofer actualizado:", chofer)

    def delete(self):
        self.read()
        index = int(input("Seleccione el índice del chofer a eliminar: ")) - 1
        self.chofer_model.eliminar_objeto(index)
        self.jsonHandler.parse_to_dict(self.chofer_model)
        self.jsonHandler.to_json(self.chofer_model, "../rsc/Chofer.json")
        print("Chofer eliminado")

if __name__ == "__main__":
    interface = ChoferInterface()
    interface.run()
