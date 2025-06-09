# this line makes figures interactive in Jupyter notebooks
#%matplotlib inline
from matplotlib import pyplot as plt

import numpy as np
import cantera as ct

from pint import UnitRegistry
ureg = UnitRegistry()
Q_ = ureg.Quantity

# for convenience:
def to_si(quant):
    '''Converts a Pint Quantity to magnitude at base SI units.
    '''
    return quant.to_base_units().magnitude

# extract all species in the NASA database
full_species = {S.name: S for S in ct.Species.list_from_file('nasa_gas.yaml')}

# extract only the relevant species
species = [full_species[S] for S in (
    'N2H4', 'N2', 'H2', 'H', 'N', 'NH'
    )]
gas = ct.Solution(thermo='ideal-gas', species=species)

temperature = Q_(5000, 'K')
pressure = Q_(50, 'psi')

gas.TPX = to_si(temperature), to_si(pressure), 'N2H4:1.0'
gas.equilibrate('TP')
gas()

gamma_ct = gas.cp_mole / gas.cv_mole
print(f'Cantera specific heat ratio: {gamma_ct: .4f}')


def get_thermo_derivatives(gas):
    '''Gets thermo derivatives based on shifting equilibrium.
    '''
    # unknowns for system with no condensed species:
    # dpi_i_dlogT_P (# elements)
    # dlogn_dlogT_P
    # dpi_i_dlogP_T (# elements)
    # dlogn_dlogP_T
    # total unknowns: 2*n_elements + 2

    num_var = 2 * gas.n_elements + 2

    coeff_matrix = np.zeros((num_var, num_var))
    right_hand_side = np.zeros(num_var)

    tot_moles = 1.0 / gas.mean_molecular_weight
    moles = gas.X * tot_moles

    condensed = False

    # indices
    idx_dpi_dlogT_P = 0
    idx_dlogn_dlogT_P = idx_dpi_dlogT_P + gas.n_elements
    idx_dpi_dlogP_T = idx_dlogn_dlogT_P + 1
    idx_dlogn_dlogP_T = idx_dpi_dlogP_T + gas.n_elements

    # construct matrix of elemental stoichiometric coefficients
    stoich_coeffs = np.zeros((gas.n_elements, gas.n_species))
    for i, elem in enumerate(gas.element_names):
        for j, sp in enumerate(gas.species_names):
            stoich_coeffs[i, j] = gas.n_atoms(sp, elem)

    # equations for derivatives with respect to temperature
    # first n_elements equations
    for k in range(gas.n_elements):
        for i in range(gas.n_elements):
            coeff_matrix[k, i] = np.sum(stoich_coeffs[k, :] * stoich_coeffs[i, :] * moles)
        coeff_matrix[k, gas.n_elements] = np.sum(stoich_coeffs[k, :] * moles)
        right_hand_side[k] = -np.sum(stoich_coeffs[k, :] * moles * gas.standard_enthalpies_RT)

    # skip equation relevant to condensed species

    for i in range(gas.n_elements):
        coeff_matrix[gas.n_elements, i] = np.sum(stoich_coeffs[i, :] * moles)
    right_hand_side[gas.n_elements] = -np.sum(moles * gas.standard_enthalpies_RT)

    # equations for derivatives with respect to pressure

    for k in range(gas.n_elements):
        for i in range(gas.n_elements):
            coeff_matrix[gas.n_elements + 1 + k, gas.n_elements + 1 + i] = np.sum(
                stoich_coeffs[k, :] * stoich_coeffs[i, :] * moles)
        coeff_matrix[gas.n_elements + 1 + k, 2 * gas.n_elements + 1] = np.sum(stoich_coeffs[k, :] * moles)
        right_hand_side[gas.n_elements + 1 + k] = np.sum(stoich_coeffs[k, :] * moles)

    for i in range(gas.n_elements):
        coeff_matrix[2 * gas.n_elements + 1, gas.n_elements + 1 + i] = np.sum(stoich_coeffs[i, :] * moles)
    right_hand_side[2 * gas.n_elements + 1] = np.sum(moles)

    derivs = np.linalg.solve(coeff_matrix, right_hand_side)

    dpi_dlogT_P = derivs[idx_dpi_dlogT_P: idx_dpi_dlogT_P + gas.n_elements]
    dlogn_dlogT_P = derivs[idx_dlogn_dlogT_P]
    dpi_dlogP_T = derivs[idx_dpi_dlogP_T]
    dlogn_dlogP_T = derivs[idx_dlogn_dlogP_T]

    # dpi_dlogP_T is not used

    return dpi_dlogT_P, dlogn_dlogT_P, dlogn_dlogP_T


def get_thermo_properties(gas, dpi_dlogT_P, dlogn_dlogT_P, dlogn_dlogP_T):
    '''Calculates specific heats, volume derivatives, and specific heat ratio.

    Based on shifting equilibrium for mixtures.
    '''

    tot_moles = 1.0 / gas.mean_molecular_weight
    moles = gas.X * tot_moles

    # construct matrix of elemental stoichiometric coefficients
    stoich_coeffs = np.zeros((gas.n_elements, gas.n_species))
    for i, elem in enumerate(gas.element_names):
        for j, sp in enumerate(gas.species_names):
            stoich_coeffs[i, j] = gas.n_atoms(sp, elem)

    spec_heat_p = ct.gas_constant * (
            np.sum([dpi_dlogT_P[i] *
                    np.sum(stoich_coeffs[i, :] * moles * gas.standard_enthalpies_RT)
                    for i in range(gas.n_elements)
                    ]) +
            np.sum(moles * gas.standard_enthalpies_RT) * dlogn_dlogT_P +
            np.sum(moles * gas.standard_cp_R) +
            np.sum(moles * gas.standard_enthalpies_RT ** 2)
    )

    dlogV_dlogT_P = 1 + dlogn_dlogT_P
    dlogV_dlogP_T = -1 + dlogn_dlogP_T

    spec_heat_v = (
            spec_heat_p + gas.P * gas.v / gas.T * dlogV_dlogT_P ** 2 / dlogV_dlogP_T
    )

    gamma = spec_heat_p / spec_heat_v
    gamma_s = -gamma / dlogV_dlogP_T

    return dlogV_dlogT_P, dlogV_dlogP_T, spec_heat_p, gamma_s

o_f_ratio = 6.0
temperature_h2 = Q_(20.270, 'K')
temperature_o2 = Q_(90.170, 'K')
pressure_chamber = Q_(3000, 'psi')

h2 = ct.Solution(h2o2_filename, 'liquid_hydrogen')
h2.TP = to_si(temperature_h2), to_si(pressure_chamber)

o2 = ct.Solution(h2o2_filename, 'liquid_oxygen')
o2.TP = to_si(temperature_o2), to_si(pressure_chamber)

molar_ratio = o_f_ratio / (o2.mean_molecular_weight / h2.mean_molecular_weight)
moles_ox = molar_ratio / (1 + molar_ratio)
moles_f = 1 - moles_ox

gas2 = ct.Solution('nasa_h2o2.yaml', 'gas')

# create a mixture of the liquid phases with the gas-phase model,
# with the number of moles for fuel and oxidizer based on
# the O/F ratio
mix = ct.Mixture([(h2, moles_f), (o2, moles_ox), (gas2, 0)])

# Solve for the equilibrium state, at constant enthalpy and pressure
mix.equilibrate('HP')

gas2()

derivs = get_thermo_derivatives(gas2)

dlogV_dlogT_P, dlogV_dlogP_T, cp, gamma_s = get_thermo_properties(
    gas2, derivs[0], derivs[1], derivs[2]
    )

print(f'Cp = {cp: .2f} J/(K kg)')

print(f'(d log V/d log P)_T = {dlogV_dlogP_T: .4f}')
print(f'(d log V/d log T)_P = {dlogV_dlogT_P: .4f}')

print(f'gamma_s = {gamma_s: .4f}')

speed_sound = np.sqrt(ct.gas_constant * gas2.T * gamma_s / gas2.mean_molecular_weight)
print(f'Speed of sound = {speed_sound: .1f} m/s')

def calculate_c_star(gamma, temperature, molecular_weight):
    return (
        np.sqrt(ct.gas_constant * temperature / (molecular_weight * gamma)) *
        np.power(2 / (gamma + 1), -(gamma + 1) / (2*(gamma - 1)))
        )

entropy_chamber = gas2.s
enthalpy_chamber = gas2.enthalpy_mass
mole_fractions_chamber = gas2.X
gamma_chamber = gamma_s

c_star = calculate_c_star(gamma_chamber, gas2.T, gas2.mean_molecular_weight)
print(f'c-star: {c_star: .1f} m/s')
print('Error in c-star: '
      f'{100*np.abs(c_star - c_star_cea)/c_star_cea: .3e} %'
      )

gas_throat = ct.Solution('nasa_h2o2.yaml', 'gas')

pressure_throat = pressure_chamber / np.power(
    (gamma_chamber + 1) / 2., gamma_chamber / (gamma_chamber - 1)
)

# based on CEA defaults
max_iter_throat = 5
tolerance_throat = 0.4e-4

print('Throat iterations:')
mach = 1.0
num_iter = 0
residual = 1
while residual > tolerance_throat:
    num_iter += 1
    if num_iter == max_iter_throat:
        break
        print(f'Error: more than {max_iter_throat} iterations required for throat calculation')
    pressure_throat = pressure_throat * (1 + gamma_s * mach ** 2) / (1 + gamma_s)

    gas_throat.SPX = entropy_chamber, to_si(pressure_throat), mole_fractions_chamber
    gas_throat.equilibrate('SP')

    derivs = get_thermo_derivatives(gas_throat)
    dlogV_dlogT_P, dlogV_dlogP_T, cp, gamma_s = get_thermo_properties(
        gas_throat, derivs[0], derivs[1], derivs[2]
    )

    velocity = np.sqrt(2 * (enthalpy_chamber - gas_throat.enthalpy_mass))
    speed_sound = np.sqrt(
        ct.gas_constant * gas_throat.T * gamma_s / gas_throat.mean_molecular_weight
    )
    mach = velocity / speed_sound

    residual = np.abs(1.0 - 1 / mach ** 2)
    print(f'{num_iter}  {residual: .3e}')

temperature_throat = gas_throat.T
pressure_throat = Q_(gas_throat.P, 'Pa')
gamma_s_throat = gamma_s

print('Error in throat temperature: '
      f'{100 * np.abs(temperature_throat - temperature_throat_cea) / temperature_throat_cea: .3e} %'
      )
print('Error in throat pressure: '
      f'{100 * np.abs(pressure_throat - pressure_throat_cea) / pressure_throat_cea: .3e~P} %'
      )