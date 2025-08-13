class biblioteca:
    def __init__(self, titulo,autor,publicacion,codigo):
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion
        self.codigo = codigo
    def mostrar(self):
        return f"Código: {self.codigo} - Nombre: {self.titulo} - Autor: {self.autor} - Publicacion: {self.publicacion}"
class manipulacionBiblioteca:
    def __init__(self):
        self.libros=[]
    def agregar(self):
        try:
            codigo = input("Código de la libro: ")
            titulo = input("Titulo del libro: ")
            autor = input("Autor del libro: ")
            publicacion = int(input("Año de publicacion del libro: "))
            print("Libro agregado con exito.")
        except ValueError:
            print("Error: El año de publicacion del libro debe ser un número entero.")
    def mostrar(self):
        if not self.libros:
            print("No hay libros para mostrar.")
        else:
            print("\nListado de libros")
            for j, est in enumerate(self.libros, start=1):
                print(f"{j}. {est.mostrar()}")
            print()
    def eliminar(self):
        nombre=input("Ingrese el nombre del libro a eliminar: ")
        for est in self.libros:
            if est.autor.lower() == nombre.lower():
                self.libros.remove(est)
                print("Libro eliminado con exito.")
                return
            print("Error: El libro no existe")
class estudiante:
    def __init__(self, carnet,nombre,carrera):
        self.carnet = carnet
        self.nombre = nombre
        self.carrera = carrera
    def mostrar(self):
        return f"Carnet: {self.carnet} - Nombre: {self.nombre} - Carrera: {self.carrera}"
class manipulacionEstudiante:
    def __init__(self):
        self.estudiante=[]
    def agregar(self):
        try:
            carnet = int(input("Carnet del estudiante: "))
            nombre = input("Nombre del estudiante: ")
            carrera = input("Carrera del estudiante: ")
            print("Libro agregado con exito.")
        except ValueError:
            print("Error: El carnet del estudiante debe ser un número entero.")
    def mostrar(self):
        if not self.estudiante:
            print("No hay estudiantes para mostrar.")
        else:
            print("\nListado de estudiantes")
            for i, est in enumerate(self.estudiante, start=1):
                print(f"{i}. {est.mostrar()}")
            print()
    def eliminar(self):
        buscar=input("Ingrese el nombre del estudiante a eliminar: ")
        for est in self.estudiante:
            if est.nombre.lower() == buscar.lower():
                self.estudiante.remove(est)
                print("Estudiante eliminado con exito.")
                return
            print("Error: El estudiante no existe")

agregarlibro = manipulacionBiblioteca()
agregarestudiante = manipulacionEstudiante()
while True:
    print("•••••MENÚ•••••")
    print("1. Agregar libro")
    print("2. Agregar estudiante")
    print("3. Mostrar libro")
    print("4. Mostrar estudiante")
    print("5. Eliminar libro")
    print("6. Eliminar estudiante")
    print("7. Salir")
    try:
        opcion=int