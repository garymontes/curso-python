# Datos ficticios de estudiantes
estudiantes = {
    1: {
        'nombre': 'Juan Pérez',
        'edad': 15,
        'grado': 10,
        'correo': 'juan.perez@example.com',
        'notas': {'matemáticas': 85, 'ciencias': 90, 'literatura': 88}
    },
    2: {
        'nombre': 'María Gómez',
        'edad': 14,
        'grado': 9,
        'correo': 'maria.gomez@example.com',
        'notas': {'matemáticas': 92, 'ciencias': 89, 'literatura': 94}
    },
    3: {
        'nombre': 'Carlos López',
        'edad': 16,
        'grado': 11,
        'correo': 'carlos.lopez@example.com',
        'notas': {'matemáticas': 78, 'ciencias': 85, 'literatura': 80}
    },
    4: {
        'nombre': 'Ana Martínez',
        'edad': 15,
        'grado': 10,
        'correo': 'ana.martinez@example.com',
        'notas': {'matemáticas': 88, 'ciencias': 92, 'literatura': 91}
    },
    5: {
        'nombre': 'Luis Rodríguez',
        'edad': 14,
        'grado': 9,
        'correo': 'luis.rodriguez@example.com',
        'notas': {'matemáticas': 95, 'ciencias': 93, 'literatura': 89}
    }
}

# Imprimir los datos de los estudiantes
for id_estudiante, info in estudiantes.items():
    print(f"ID: {id_estudiante}")
    for clave, valor in info.items():
        if isinstance(valor, dict):
            print(f"  {clave.capitalize()}:")
            for materia, nota in valor.items():
                print(f"    {materia.capitalize()}: {nota}")
        else:
            print(f"  {clave.capitalize()}: {valor}")
    print()
