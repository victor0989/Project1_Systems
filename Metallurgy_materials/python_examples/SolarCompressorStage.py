from math import radians, tan

cp = 1005  # J/kg·K (aire)
R = 287.05  # J/kg·K

def calc_beta2(U2, C2, angle_offset=5):
    beta2 = radians(angle_offset + (C2 / U2))  # simplificado
    return beta2

def slip_factor(C_theta2, U2):
    return 1 - (C_theta2 / U2)

def temp_rise(U2, C_theta2, U1, C_theta1, cp=1005):
    delta_T0 = (U2 * C_theta2 - U1 * C_theta1) / cp
    return delta_T0
