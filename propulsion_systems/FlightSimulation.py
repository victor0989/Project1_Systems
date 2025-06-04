from scipy.integrate import solve_ivp

# Parámetros del motor tipo MERLIN
Isp = 282  # segundos (al nivel del mar)
thrust = 845000  # Newtons
mass_flow = thrust / (Isp * 9.81)  # kg/s

# Masa inicial del cohete
m0 = 30000  # kg (con combustible)
mf = 2500   # kg (masa seca)
burn_time = (m0 - mf) / mass_flow

# Ecuaciones de movimiento
def rocket_dynamics(t, y):
    h, v, m = y
    if m > mf:
        dm_dt = -mass_flow
        a = (thrust - m * 9.81) / m
    else:
        dm_dt = 0
        a = -9.81
    return [v, a, dm_dt]

# Condiciones iniciales: altura, velocidad, masa
y0 = [0, 0, m0]
t_span = (0, 200)
sol = solve_ivp(rocket_dynamics, t_span, y0, max_step=0.5)

# Extraer datos
altitude = sol.y[0]
velocity = sol.y[1]
mass = sol.y[2]

# Gráficas
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(sol.t, altitude, label="Altura (m)")
plt.ylabel("Altura (m)")
plt.grid(True)

plt.subplot(2, 1, 2)
plt.plot(sol.t, velocity, label="Velocidad (m/s)", color='red')
plt.xlabel("Tiempo (s)")
plt.ylabel("Velocidad (m/s)")
plt.grid(True)

plt.tight_layout()
plt.show()
