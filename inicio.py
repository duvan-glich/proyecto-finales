import pandas as pd
import matplotlib.pyplot as plt

# Datos en formato de lista de diccionarios
data = [
    {'Nombre': 'Ana', 'Edad': 18, 'Género': 'Mujer', 'Calificación': 8.5},
    {'Nombre': 'Juan', 'Edad': 19, 'Género': 'Hombre', 'Calificación': 7.0},
    {'Nombre': 'Pedro', 'Edad': 18, 'Género': 'Hombre', 'Calificación': 9.2},
    {'Nombre': 'Sofía', 'Edad': 17, 'Mujer': 'Mujer', 'Calificación': 9.8},  # Corregido: 'Mujer' como valor
    {'Nombre': 'Carlos', 'Edad': 20, 'Género': 'Hombre', 'Calificación': 6.5},
    {'Nombre': 'María', 'Edad': 18, 'Género': 'Mujer', 'Calificación': 8.0},
    {'Nombre': 'Luis', 'Edad': 19, 'Género': 'Hombre', 'Calificación': 7.8}
]

# Crear el DataFrame
df = pd.DataFrame(data)
print(df)

# Agrupar por género y calcular estadísticas
grouped = df.groupby('Género')
resumen = grouped.agg({'Edad': 'mean', 'Calificación': ['mean', 'max']})

# Renombrar columnas para mejor legibilidad
