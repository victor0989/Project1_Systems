import math

# Step 1: Calculating solidification time for different shapes

def solidification_time(area, volume=1):
# Simplified example of the calculation based on area and volume
# t ~ (Volume/Area)^2 * constant (const = 1 for simplicity)
return (volume / area)**2

def sphere_area(volume=1):
# V = (4/3)*pi*r^3 => r = (3V/4pi)^(1/3)
r = (3 * volume / (4 * math.pi))**(1/3)
area = 4 * math.pi * r**2
return area

def cube_area(volume=1):
# V = a^3 => a = V^(1/3)
a = volume**(1/3)
area = 6 * a**2
return area

def cylinder_area(volume=1):
# Volume V = pi*r^2*h
# Height h = 2r (height equals diameter)
# V = pi*r^2 * 2r = 2*pi*r^3 => r = (V/(2*pi))^(1/3)
r = (volume / (2 * math.pi))**(1/3)
h = 2 * r
Area = 2 * math.pi * r * h + 2 * math.pi * r**2
return area

# Area Calculation
A_sphere = area_sphere()
A_cube = area_cube()
A_cylinder = area_cylinder()

# Relative Solidification Times
t_sphere = solidification_time(A_sphere)
t_cube = solidification_time(A_cube)
t_cylinder = solidification_time(A_cylinder)

print("Relative times of solidification:")
print(f"Sphere: {t_sphere:.4f}")
print(f"Cube: {t_cube:.4f}")
print(f"Cylinder: {t_cylinder:.4f}")

# Step 2: Volumetric shrinkage of metals (in %)

metal_shrinkage = {
"Aluminum": 7.1,
"Zinc": 6.5,
"Al-4.5% Cu": 6.3,
"Gold": 5.5,
"White iron": 4.75,
"Copper": 4.9,
"Bronze (70–30)": 4.5,
"Magnesium": 4.2,
"Carbon steels": 3.25,
"Al-12% Si": 3.8,
"Lead": 3.2,
"Bismuth": 3.3,
"Silicon": 2.9,
"Gray Iron": -2.5, # Note: Expansion, therefore negative
}

print("\nVolumetric Shrinkage of Metals (%):")
for metal, contr in metal_shrinkage.items():
state = "Expansion" if contr < 0 else "Shrinkage"
print(f"{metal}: ​​{abs(contr)}% ({state})")

# Step 3: Common Casting Defects

casting_defects = {
"A": "Metal projections (fins, burrs, blisters, rough surfaces).",
"B": "Internal or exposed cavities (blow holes, pin points, porosity).",
"C": "Discontinuities (cracks, cold or hot tears, cold spots).",
"D": "Defective surfaces (folds, overlaps, scars, sand layers, flakes).",
"E": "Incomplete casting (premature solidification, insufficient volume, leaks).",
"F": "Incorrect dimensions or shapes (irregular shrinkage, deformed model).",
"G": "Inclusions (trapped non-metallic particles, affecting strength)."
}

print("\