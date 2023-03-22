import numpy as np

# Define the inputs
molec_per_cm2 = 1e17   # atmospheric total column methane in molec/cm2
molec_per_cm2 = 38e23
# Convert molec/cm2 to molec/m2
molec_per_m2 = molec_per_cm2 * 1e4

# Calculate the total number of methane molecules per unit area
pressure = 1   # atmospheric pressure in atm
temperature = 273   # temperature in Kelvin (STP)
gas_constant = 8.31   # gas constant in J/(mol*K)
surface_area = 5.1e14   # surface area of the Earth in m2
molecules_per_m3 = 2.69e19   # number of molecules per m3 at STP
total_molecules = (pressure * molecules_per_m3 * surface_area) / (gas_constant * temperature)

# Convert the total number of molecules per unit area to ppmv
ppmv = (molec_per_m2 / 1e6) * (16.04 / 28.97) / (total_molecules / surface_area)
print(ppmv)
# Print the result
print("Atmospheric total column methane in ppmv: {:.2f}".format(ppmv))
