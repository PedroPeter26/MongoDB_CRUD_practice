import json
import os
class CrudBoy:
    def __init__(self):
        pass

    def agregar_objeto(self, nuevo_objeto):
        if hasattr(self, 'is_array') and self.is_array:
            if not hasattr(self, 'lista_objetos'):
                self.lista_objetos = []
            self.lista_objetos.append(nuevo_objeto)
        else:
            return

    def imprimir_objetos(self):
        if hasattr(self, 'is_array') and self.is_array:
            if not hasattr(self, 'lista_objetos'):
                self.lista_objetos = []
            for objeto in self.lista_objetos:
                print(objeto)
        else:
            return

    def imprimir_objeto(self, indice):
        if hasattr(self, 'is_array') and self.is_array:
            if not hasattr(self, 'lista_objetos'):
                self.lista_objetos = []
            if indice > len(self.lista_objetos) - 1:
                print("Objeto inválido")
            else:
                objeto = self.lista_objetos[indice]
                print(objeto)
        else:
            return

    def eliminar_objeto(self, indice):
        if hasattr(self, 'is_array') and self.is_array:
            if not hasattr(self, 'lista_objetos'):
                self.lista_objetos = []
            if indice > len(self.lista_objetos) - 1:
                print("Índice inválido.")
            else:
                objeto_eliminado = self.lista_objetos.pop(indice)
                print(f"Objeto eliminado: {objeto_eliminado}")
        else:
            return

    def editar_objeto(self, indice, nuevo_objeto):
        if hasattr(self, 'is_array') and self.is_array:
            if not hasattr(self, 'lista_objetos'):
                self.lista_objetos = []
            if indice > len(self.lista_objetos) - 1:
                print("Índice inválido.")
            else:
                self.lista_objetos[indice] = nuevo_objeto
                print(f"Objeto en el índice {indice} editado correctamente.")
        else:
            return

    def convertToObj(self,data,cls):
        if isinstance(data, list):
            result = [cls(**item) for item in data]
            self.lista_objetos = result
        else:
            result = cls(**data)
        return result

    def load(self, filepath, cls):
        try:
            full_path = os.path.join(os.path.dirname(__file__), filepath)
            with open(full_path, "r", encoding='utf-8') as file:
                data = json.load(file)
                self.content = self.convertToObj(data, cls)

            print(f"Datos cargados desde '{filepath}' correctamente")
        except Exception as e:
            print(f"Error al cargar los datos desde '{filepath}': {e}'")
