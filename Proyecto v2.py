import sqlite3

# Conectarse a la base de datos
# mi_conexion = sqlite3.connect('database.db')
# cursor = mi_conexion.cursor()


def mostrar_usuarios(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuario")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

def agregar_usuario(conn, id, nombre, apellido, estado, país, ciudad, telefono):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuario (id, nombre, apellido, estado, país, ciudad, telefono) VALUES (?, ?, ?, ?, ?, ?, ?)",
                   (id, nombre, apellido, estado, país, ciudad, telefono))
    conn.commit()
    print("Usuario agregado correctamente.")

def eliminar_usuario(conn, id_usuario):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuario WHERE id = ?", (id_usuario,))
    conn.commit()
    print("Usuario eliminado correctamente.")

def actualizar_usuario(conn, id_usuario, nombre):
    cursor = conn.cursor()
    cursor.execute("UPDATE usuario SET nombre = ? WHERE id = ?", (nombre, id_usuario))
    conn.commit()
    print("Usuario actualizado correctamente.")

# Conectarse a la base de datos
conn = sqlite3.connect('database.db')

while True:
    print("\n-- Menú Principal --")
    print("1. Agregar usuario")
    print("2. Mostrar usuarios")
    print("3. Eliminar usuario")
    print("4. Actualizar usuario")
    print("5. Salir")

    opcion = input("Ingrese laopción deseada: ")

    if opcion == "1":
        id = input("Ingrese el ID del usuario: ")
        nombre = input("Ingrese el nombre del usuario: ")
        apellido = input("Ingrese el apellido del usuario: ")
        estado = input("Ingrese el estado del usuario: ")
        país = input("Ingrese el país del usuario: ")
        ciudad = input("Ingrese la ciudad del usuario: ")
        telefono = input("Ingrese el teléfono del usuario: ")

        agregar_usuario(conn, id, nombre, apellido, estado, país, ciudad, telefono)

    elif opcion == "2":
        mostrar_usuarios(conn)

    elif opcion == "3":
        id = input("Ingrese el ID del usuario a eliminar: ")
        eliminar_usuario(conn, id)

    elif opcion == "4":
        id = input("Ingrese el ID del usuario a actualizar: ")
        nombre = input("Ingrese el nuevo nombre: ")
        actualizar_usuario(conn, id, nombre)

    elif opcion == "5":
        break

# Cerrar la conexión a la base de datos
conn.close()

