import numpy as np

# Define the inputs
molec_per_cm2 = 3.9e23   # atmospheric total column methane in molec/cm2

# Convert molec/cm2 to molec/m2
molec_per_m2 = molec_per_cm2 * 1e4

# Calculate the total number of methane molecules in the atmosphere
pressure_hPa = 1013.25   # atmospheric pressure in hPa (STP)
temperature_K = 273.15   # temperature in Kelvin (STP)
gas_constant = 8.31   # gas constant in J/(mol*K)
molecules_per_m3 = 2.69e19   # number of molecules per m3 at STP
total_molecules = (pressure_hPa * 100.0 * molecules_per_m3) / (gas_constant * temperature_K)

# Convert the total number of molecules per unit area to ppmv
ppmv = (molec_per_m2 / 1e6) * (16.04 / 28.97) / (total_molecules / 1e6)

# Print the result
print("Atmospheric total column methane in ppmv: {:.2f}".format(ppmv))
print((ppmv))
