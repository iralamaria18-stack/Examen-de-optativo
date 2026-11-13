import psycopg2

try:
  # Conexión a la base de datos
  conexion = psycopg2.connect(
      dbname="Alumnos",
      user="postgres",
      password="123456",
      host="localhost",
      port="5432",
  )

  cursor = conexion.cursor()

  # Operación DELETE: Borrar al alumno con id_alumno = 2
  sql_delete = "DELETE FROM alumnos WHERE id_alumno = %s"
  cursor.execute(sql_delete, (2,))

  # Confirmamos los cambios
  conexion.commit()
  print("¡Alumno borrado correctamente!")

  # Consultamos de nuevo para mostrar que el alumno ya no está (evidencia requerida)
  cursor.execute(
      "SELECT id_alumno, nombre, cedula, carrera, promedio FROM alumnos"
  )
  alumnos = cursor.fetchall()

  print("\n--- LISTADO DESPUÉS DEL DELETE ---")
  for alumno in alumnos:
    print(
        f"ID: {alumno[0]} | Nombre: {alumno[1]} | Cédula: {alumno[2]} | Carrera:"
        f" {alumno[3]} | Promedio: {alumno[4]}"
    )

  # Cerramos cursor y conexión
  cursor.close()
  conexion.close()

except Exception as e:
  print("Ocurrio un error:", e)