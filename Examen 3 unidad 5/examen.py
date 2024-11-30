print("April Arzaba Diaz")
print("1173")
print("3W")
class Agenda:
    def __init__(self):
        self.contactos = []

    def agregar_contacto(self, nombre, telefono, email):
        self.contactos.append({'nombre': nombre, 'telefono': telefono, 'email': email})

    def listar_contactos(self):
        if not self.contactos:
            print("No hay contactos.")
        else:
            for c in self.contactos:
                print(f"Nombre: {c['nombre']}, Teléfono: {c['telefono']}, Email: {c['email']}")

#esta linea dara un ejemplo de uso:
agenda = Agenda()
agenda.agregar_contacto("April Arzaba", "6562360205", "april@example.com")
agenda.agregar_contacto("Oliver Rodriguez", "6562603242", "oliver@example.com")

agenda.listar_contactos()
