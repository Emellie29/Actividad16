class biblioteca:
    def __init__(self, titulo,autor,publicacion,codigo):
        self.titulo = titulo
        self.autor = autor
        self.publicacion = publicacion
        self.codigo = codigo
    def mostrarlibro(self):
        return f"Código: {self.codigo} - Nombre: {self.titulo} - Autor: {self.autor} - Publicacion: {self.publicacion}"
class manipulacionBiblioteca:
    def __init__(self):
        self.libros=[]
    def agregarlibro(self):
        try:
            codigo = input("Código del libro: ")
            titulo = input("Titulo del libro: ")
            autor = input("Autor del libro: ")
            publicacion = int(input("Año de publicacion del libro: "))
            nuevo_libro = biblioteca(titulo, autor, publicacion, codigo)
            self.libros.append(nuevo_libro)
            print("Libro agregado con éxito.")
        except ValueError:
            print("Error: El año de publicación del libro debe ser un número entero.")
    def mostrarlibros(self):
        if not self.libros:
            print("No hay libros para mostrar.")
        else:
            print("\nListado de libros")
            for j, est in enumerate(self.libros, start=1):
                print(f"{j}. {est.mostrarlibro()}")
            print()
    def eliminarlibro(self):
        nombre = input("Ingrese el nombre del libro a eliminar: ")
        for est in self.libros:
            if est.titulo.lower() == nombre.lower():
                self.libros.remove(est)
                print("Libro eliminado con éxito.")
                return
        print("Error: El libro no existe.")
class estudiante:
    def __init__(self, carnet,nombre,carrera):
        self.carnet = carnet
        self.nombre = nombre
        self.carrera = carrera
    def mostrarestudiante(self):
        return f"Carnet: {self.carnet} - Nombre: {self.nombre} - Carrera: {self.carrera}"
class manipulacionEstudiante:
    def __init__(self):
        self.estudiantes=[]
    def agregar(self):
        try:
            carnet = int(input("Carnet del estudiante: "))
            nombre = input("Nombre del estudiante: ")
            carrera = input("Carrera del estudiante: ")
            nuevo_estudiante = estudiante(carnet, nombre, carrera)
            self.estudiantes.append(nuevo_estudiante)
            print("Estudiante agregado con éxito.")
        except ValueError:
            print("Error: El carnet del estudiante debe ser un número entero.")
    def mostrar(self):
        if not self.estudiantes:
            print("No hay estudiantes para mostrar.")
        else:
            print("\nListado de estudiantes")
            for i, est in enumerate(self.estudiantes, start=1):
                print(f"{i}. {est.mostrarestudiante()}")
            print()
    def eliminar(self):
        buscar = input("Ingrese el nombre del estudiante a eliminar: ")
        for est in self.estudiantes:
            if est.nombre.lower() == buscar.lower():
                self.estudiantes.remove(est)
                print("Estudiante eliminado con éxito.")
                return
        print("Error: El estudiante no existe.")

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
        opcion=int(input("Seleccione una opción: "))
        match opcion:
            case 1:
                agregarlibro.agregarlibro()
            case 2:
                agregarestudiante.agregar()
            case 3:
                agregarlibro.mostrarlibros()
            case 4:
                agregarestudiante.mostrar()
            case 5:
                agregarlibro.eliminarlibro()
            case 6:
                agregarestudiante.eliminar()
            case 7:
                print("Saliendo del programa")
                break
            case _:
                print("Opcion invalida")
    except ValueError:
        print("Debe ingresar un número entero.")