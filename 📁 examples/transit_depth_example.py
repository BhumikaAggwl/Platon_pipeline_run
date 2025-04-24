import os
os.environ["PLATON_DATA_PATH"] = "/Users/Lenovo/projects/isro/data"

import numpy as np
import matplotlib.pyplot as plt
from platon.transit_depth_calculator import TransitDepthCalculator
from platon.constants import R_sun, R_jup, M_jup

Rs = 1.16 * R_sun
Mp = 0.73 * M_jup
Rp = 1.40 * R_jup
T = 1200

calculator = TransitDepthCalculator()
wavelengths, depths, _ = calculator.compute_depths(Rs, Mp, Rp, T, full_output=True)

plt.plot(1e6 * wavelengths, depths)
plt.xlabel("Wavelength (µm)")
plt.ylabel("Transit Depth")
plt.title("Simulated Transit Spectrum")
plt.savefig("outputs/transit_depth_plot.png")
plt.show()
