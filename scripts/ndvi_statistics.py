import rasterio
import numpy as np

# Open NDVI raster
with rasterio.open("../outputs/ndvi_map.tif") as src:
    ndvi = src.read(1)

# Replace invalid values with NaN
ndvi = np.where(np.isfinite(ndvi), ndvi, np.nan)

print("NDVI Statistics")
print("----------------")
print(f"Minimum NDVI: {np.nanmin(ndvi):.3f}")
print(f"Maximum NDVI: {np.nanmax(ndvi):.3f}")
print(f"Mean NDVI: {np.nanmean(ndvi):.3f}")