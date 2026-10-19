import rasterio
import matplotlib.pyplot as plt

ndvi_file = "../data/raw/NDVI_HomaBay.tif"

with rasterio.open(ndvi_file) as src:
    ndvi = src.read(1)

plt.figure(figsize=(10, 8))

plt.imshow(
    ndvi,
    cmap='RdYlGn',
    vmin=-1,
    vmax=1
)

plt.colorbar(label='NDVI')

plt.title(
    'Vegetation Condition Map - Homa Bay County'
)

plt.axis('off')

plt.savefig(
    "../outputs/vegetation_condition_map.png",
    dpi=300,
    bbox_inches='tight'
)

plt.show()

print("Map exported successfully")
