import random
import time

def read_vibration():
    # Simulación de una lectura de sensor
    return round(random.uniform(0.01, 0.05), 4)

while True:
    vibration = read_vibration()
    if vibration > 0.04:
        print(f"[ALERTA] Alta vibración detectada: {vibration} g")
    else:
        print(f"Vibración estable: {vibration} g")
    time.sleep(1)
