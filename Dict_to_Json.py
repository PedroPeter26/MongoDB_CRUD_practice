import json
import os

class Dict_to_Json():
    def __init__(self):
        super().__init__()
        self.dict = {}
        self.list_dict = []

    def parse_to_dict(self, obj):
        if hasattr(obj, 'is_array') and obj.is_array is False:
            self.dict = self._object_to_dict(obj)
            return self.dict
        elif hasattr(obj, 'lista_objetos'):
            self.list_dict = [self._object_to_dict(item) for item in obj.lista_objetos]
            return self.list_dict

    def _object_to_dict(self, obj):
        if isinstance(obj, list):
            return [self._object_to_dict(item) for item in obj]
        elif isinstance(obj, dict):
            return {key: self._object_to_dict(value) for key, value in obj.items()}
        elif hasattr(obj, '__dict__'):
            result = {}
            for key, value in obj.__dict__.items():
                if isinstance(value, list):
                    result[key] = [self._object_to_dict(item) for item in value]
                elif hasattr(value, '__dict__'):
                    result[key] = self._object_to_dict(value)
                else:
                    result[key] = value
            return result
        else:
            return obj

    def to_json(self, data, filepath):
        if hasattr(data, 'is_array') and data.is_array is False:
            ruta_archivo = filepath
            with open(ruta_archivo, "w") as file:
                json.dump(self.dict, file, indent=4)
        else:
            ruta_archivo = filepath
            with open(ruta_archivo, "w") as file:
                json.dump(self.list_dict, file, indent=4)
