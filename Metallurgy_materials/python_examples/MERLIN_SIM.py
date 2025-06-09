import math
import matplotlib.pyplot as plt

# Parámetros
m = 1000  # masa del vehículo en kg
t_total = 100  # segundos de simulación
dt = 1  # intervalo de tiempo en segundos

# Condiciones iniciales
v = 0  # velocidad inicial m/s
x = 0  # posición inicial m
consumo_total = 0  # consumo acumulado combustible

# Listas para graficar
tiempos = []
velocidades = []
consumos = []


# Función para calcular fuerza gravitacional (modelo hipotético)
def fuerza_gravitacional(t):
    # Ejemplo: fuerza que varía sinusoidalmente (motor gravitacional)
    return 200 * math.sin(0.1 * t) + 300  # Newtons


# Función para calcular fuerza convencional requerida para acelerar
def fuerza_convencional(v, F_grav):
    # Supongamos que queremos acelerar hasta 20 m/s^2 y mantener velocidad
    objetivo_velocidad = 20  # m/s
    aceleracion_objetivo = 0.5  # m/s² (constante)

    # Fuerza neta necesaria para mantener aceleración deseada
    F_total_requerida = m * aceleracion_objetivo

    # Restamos fuerza gravitacional disponible
    F_conv = max(0, F_total_requerida - F_grav)

    return F_conv


# Modelo consumo combustible: consumo proporcional a fuerza convencional aplicada
def consumo_combustible(F_conv, dt):
    # coeficiente arbitrario para consumo
    coef_consumo = 0.0005  # kg/Ns (kilogramos por Newton-segundo)
    return coef_consumo * F_conv * dt


# Simulación
for t in range(0, t_total, dt):
    F_grav = fuerza_gravitacional(t)
    F_conv = fuerza_convencional(v, F_grav)
    consumo = consumo_combustible(F_conv, dt)

    # Actualizar consumo total
    consumo_total += consumo

    # Actualizar velocidad con aceleración neta (F = m*a)
    a = (F_conv + F_grav) / m
    v += a * dt

    # Guardar datos para graficar
    tiempos.append(t)
    velocidades.append(v)
    consumos.append(consumo_total)

# Graficar resultados
plt.figure(figsize=(12, 6))

plt.subplot(2, 1, 1)
plt.plot(tiempos, velocidades, label='Velocidad (m/s)')
plt.xlabel('Tiempo (s)')
plt.ylabel('Velocidad (m/s)')
plt.legend()
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(tiempos, consumos, label='Consumo combustible (kg)', color='orange')
plt.xlabel('Tiempo (s)')
plt.ylabel('Consumo acumulado (kg)')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
