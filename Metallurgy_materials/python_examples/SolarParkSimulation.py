from calculations.compressor_stage import temp_rise
from thermal_control.system_config import thermal_ranges

def main():
    print("== Solar Parker Probe Simulation ==")
    ΔT0 = temp_rise(U2=350, C_theta2=150, U1=200, C_theta1=250)
    print(f"ΔT₀ (Stage Temp Rise): {ΔT0:.2f} K")

    print(f"Thermal Operational Range: {thermal_ranges['operative']} °C")

if __name__ == "__main__":
    main()
