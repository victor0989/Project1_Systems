from rocketcea.cea_obj_w_units import CEA_Obj
import cantera as ct
import matplotlib.pyplot as plt

# --- ROCKETCEA: cálculo del Isp y temperatura de combustión ---
ox_name = 'LOX'
fuel_name = 'RP-1'
isp_calculator = CEA_Obj(oxName=ox_name, fuelName=fuel_name)

# Parámetros del motor
pc = 100  # Presión de cámara en atm
pe = 1    # Presión de salida en atm (vacío ideal)
o_f_ratios = [2.0 + 0.1*i for i in range(20)]  # Ratios oxígeno/combustible

isp_values = []
temp_values = []

for of in o_f_ratios:
    isp = isp_calculator.get_Isp(pc=pc, MR=of, eps=40, Pexit=pe, frozen=0)
    temp = isp_calculator.get_Tcomb(pc=pc, MR=of)
    isp_values.append(isp)
    temp_values.append(temp)

# --- GRAFICAR resultados ---
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(o_f_ratios, isp_values, label="Isp (s)", color='blue')
plt.xlabel("O/F ratio")
plt.ylabel("Impulso específico (s)")
plt.title("Isp vs Mezcla O/F")
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(o_f_ratios, temp_values, label="Temperatura (K)", color='red')
plt.xlabel("O/F ratio")
plt.ylabel("Temperatura de combustión (K)")
plt.title("Temperatura vs Mezcla O/F")
plt.grid(True)

plt.tight_layout()
plt.show()

gas = ct.Solution('gri30.yaml')
gas.set_equivalence_ratio(phi=1.8, fuel='C7H16', oxidizer='O2:1.0, N2:3.76')
gas.TP = 300, 101325  # Temperatura y presión inicial
gas.equilibrate('HP')  # Estado en equilibrio

print(f"Temperatura de combustión: {gas.T:.1f} K")
print(f"Presión final: {gas.P/1e5:.2f} bar")
print(f"Entalpía: {gas.enthalpy_mass:.1f} J/kg")
