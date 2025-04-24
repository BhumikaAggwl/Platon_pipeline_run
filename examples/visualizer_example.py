import os
os.environ["PLATON_DATA_PATH"] = "/Users/Lenovo/projects/isro/data"

import numpy as np
import matplotlib.pyplot as plt
from platon.transit_depth_calculator import TransitDepthCalculator
from platon.constants import R_sun, R_jup, M_jup
from platon.visualizer import Visualizer

calculator = TransitDepthCalculator()
wavelengths, depths, info = calculator.compute_depths(
    1.16 * R_sun, 0.73 * M_jup, 1.4 * R_jup, 1200, full_output=True)

color_bins = 1e-6 * np.array([[4, 5], [3.2, 4], [1.1, 1.7]])
visualizer = Visualizer()
image, _ = visualizer.draw(info, color_bins, method="disk")

plt.imshow(image)
plt.title("Exoplanet Transit Visualizer Output")
plt.axis("off")
plt.savefig("outputs/visualizer_output.png")
plt.show()
