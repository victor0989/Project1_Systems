import cantera as ct

# Definir mezcla de hidrazina (N2H4) y aire
gas = ct.Solution('gri30.yaml')  # gri30 tiene muchos compuestos, quizá tengas que definir hidrazina o usar un archivo específico

# Configurar condiciones iniciales
gas.TPX = 300, ct.one_atm, 'CH4:1, O2:2'

# Calcular propiedades a equilibrio
gas.equilibrate('HP')

print(f"Temperatura de llama: {gas.T} K")
print(f"Presión: {gas.P} Pa")
print(f"Composición de productos: {gas.X}")
