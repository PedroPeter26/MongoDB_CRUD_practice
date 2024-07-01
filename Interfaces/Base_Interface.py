class BaseInterface:
    def create_instance(self):
        raise NotImplementedError("Este método debe ser implementado por subclases")

    def show_menu(self):
        raise NotImplementedError("Este método debe ser implementado por subclases")

    def run(self):
        while True:
            self.show_menu()
            choice = input("Seleccione una opción: ")
            if choice == '5':
                print("Volviendo al menú principal...")
                break
            elif choice in self.options:
                self.options[choice]()
            else:
                print("Opción no válida, por favor intente nuevamente.")
