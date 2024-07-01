from Interfaces.TaxiInterface import TaxiInterface
from Interfaces.ChoferInterface import ChoferInterface
from Interfaces.ViajeInterface import ViajeInterface

class Menu:
    def __init__(self):
        self.options = {
            '1': ('Gestionar Taxis', TaxiInterface),
            '2': ('Gestionar Choferes', ChoferInterface),
            '3': ('Gestionar Viajes', ViajeInterface),
            '4': ('Salir', None)
        }

    def display_menu(self):
        print("\nMenú Principal:")
        for key, (description, _) in self.options.items():
            print(f"{key}. {description}")

    def run(self):
        while True:
            self.display_menu()
            choice = input("Seleccione una opción: ")
            if choice == '4':
                print("Saliendo...")
                break
            elif choice in self.options:
                _, interface_class = self.options[choice]
                if interface_class:
                    interface_instance = interface_class()
                    interface_instance.run()
            else:
                print("Opción no válida, por favor intente nuevamente.")

if __name__ == "__main__":
    menu = Menu()
    menu.run()