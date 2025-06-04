class MerlinEngine:
    def __init__(self, version, thrust_sea_level, thrust_vacuum, isp_sea_level, isp_vacuum, chamber_pressure, dry_mass):
        self.version = version
        self.thrust_sea_level = thrust_sea_level  # Newtons
        self.thrust_vacuum = thrust_vacuum        # Newtons
        self.isp_sea_level = isp_sea_level          # seconds
        self.isp_vacuum = isp_vacuum                # seconds
        self.chamber_pressure = chamber_pressure    # Pascals
        self.dry_mass = dry_mass                    # kg

    def specific_impulse_difference(self):
        return self.isp_vacuum - self.isp_sea_level

    def thrust_to_weight_ratio(self):
        g0 = 9.80665  # gravity m/s^2
        return self.thrust_sea_level / (self.dry_mass * g0)

# Ejemplo de motor Merlin 1C
merlin_1c = MerlinEngine(
    version="Merlin 1C",
    thrust_sea_level=420e3,    # 420 kN
    thrust_vacuum=480e3,       # 480 kN
    isp_sea_level=275,         # s
    isp_vacuum=304.8,          # s
    chamber_pressure=6.77e6,   # Pa
    dry_mass=630               # kg
)

print(f"Thrust-to-weight ratio: {merlin_1c.thrust_to_weight_ratio():.2f}")
print(f"ISP difference (vacuum - sea-level): {merlin_1c.specific_impulse_difference():.2f} s")
