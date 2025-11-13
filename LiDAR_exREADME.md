# LiDAR Point Cloud Coverage Script

**Author:** Anna Agosta G'meiner  
**Date:** November 2023  

This Python script reads a LiDAR point cloud from a `.las` or `.laz` file and uses a hexbin filter to calculate the approximate coverage area of the point cloud. It extracts the boundary polygon of the coverage and saves it to a GeoPackage file for use in GIS software.  

**Requirements:**  
- Python 3.x  
- PDAL  
- Fiona  
- Shapely  

**Usage:**  
1. Update the `filename` variable with the path to your LAS/LAZ file.  
2. Update the GeoPackage output path and layer name if needed.  
3. Run the script to generate the coverage polygon.  

**Disclaimer:**  
This code is for personal and educational purposes only.
