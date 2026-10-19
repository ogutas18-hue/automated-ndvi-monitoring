import rasterio
import numpy as np
import pandas as pd

# Path to NDVI raster
ndvi_file = "../data/raw/NDVI_HomaBay.tif"

# Read raster
with rasterio.open(ndvi_file) as src:
    ndvi = src.read(1)

# Remove nodata values
ndvi = np.where(np.isfinite(ndvi), ndvi, np.nan)

# Calculate statistics
stats = {
    "Minimum NDVI": round(np.nanmin(ndvi), 3),
    "Maximum NDVI": round(np.nanmax(ndvi), 3),
    "Mean NDVI": round(np.nanmean(ndvi), 3),
    "Standard Deviation": round(np.nanstd(ndvi), 3)
}

# Print results
print("\nNDVI Statistics")
print("----------------")

for key, value in stats.items():
    print(f"{key}: {value}")

# Save CSV
df = pd.DataFrame([stats])
df.to_csv("../outputs/ndvi_statistics.csv", index=False)

print("\nStatistics exported successfully.")
