print("April Arzaba Diaz")
print("1173")
print("3W")
class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    def mostrar_datos(self):
        """
        muestra los datos del alumno y si ha aprobado o no.
        """
        print(f"Nombre: {self.nombre}")
        print(f"Nota: {self.nota}")
        
        if self.nota >= 5:
            print("¡Aprobado!")
        else:
            print("Reprobado")

#esta linea dara un ejemplo de uso:
alumno = Alumno("April Arzaba Diaz", 6.5)
alumno.mostrar_datos()
