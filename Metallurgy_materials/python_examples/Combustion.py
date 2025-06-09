import cantera as ct

# Define mezcla: 2 H2 + 1 O2
gas = ct.Solution('gri30.yaml')  # Modelo cinético detallado de gases

# Mezcla estequiométrica
gas.TPX = 300.0, ct.one_atm, {'H2': 2, 'O2': 1}

# Reactor constante a volumen
reactor = ct.IdealGasConstPressureReactor(gas)

# Simulador de tiempo
sim = ct.ReactorNet([reactor])

# Corre hasta alcanzar equilibrio
sim.advance_to_steady_state()

# Resultados
print("====== EQUILIBRIO H2 + O2 ======")
print(f"Temperatura final: {reactor.T:.2f} K")
print(f"Presión final: {reactor.thermo.P / 101325:.2f} atm")
print("Composición final (fracción molar):")
for species, fraction in zip(gas.species_names, reactor.thermo.X):
    if fraction > 1e-4:  # Muestra los relevantes
        print(f"{species}: {fraction:.4f}")
