# Hydrazine_CEA.py
# Ejemplo completo para cálculos termodinámicos con Cantera y N2H4

# Para notebooks Jupyter (comenta esta línea si usas PyCharm o consola)
# %matplotlib inline

import cantera as ct
import numpy as np
from matplotlib import pyplot as plt
from pint import UnitRegistry

# Inicializar la unidad de medida
ureg = UnitRegistry()
Q_ = ureg.Quantity

# Función para convertir cantidades Pint a magnitud en unidades SI base
def to_si(quant):
    return quant.to_base_units().magnitude

# Cargar todas las especies desde un archivo YAML (debes tener nasa_gas.yaml con N2H4)
full_species = {S.name: S for S in ct.Species.list_from_file('nasa_gas.yaml')}

# Seleccionar solo las especies relevantes para el cálculo
species = [full_species[S] for S in ('N2H4', 'N2', 'H2', 'H', 'N', 'NH')]

# Crear la solución Cantera con las especies seleccionadas
gas = ct.Solution(thermo='ideal-gas', species=species)

# Definir condiciones iniciales con Pint (temperatura y presión)
temperature = Q_(5000, 'K')      # temperatura en Kelvin
pressure = Q_(50, 'psi')         # presión en libras por pulgada cuadrada

# Asignar estado TP con mezcla de hidrazina (N2H4)
gas.TPX = to_si(temperature), to_si(pressure), 'N2H4:1.0'

# Calcular el equilibrio a temperatura y presión constantes
gas.equilibrate('TP')

# Imprimir resultados
print(f"Temperatura de equilibrio: {gas.T:.2f} K")
print(f"Presión de equilibrio: {gas.P/ct.one_atm:.2f} atm")
print(f"Composición en moles: {gas.X}")

# Ejemplo sencillo de gráfico: composición molar de cada especie
species_names = gas.species_names
mole_fractions = gas.X

plt.bar(species_names, mole_fractions)
plt.ylabel('Fracción molar')
plt.title('Composición de mezcla en equilibrio')
plt.show()
plt.savefig("equilibrio_hidrazina.png", dpi=300)

