###############################################################################
# LiDAR point cloud processing script                                         #
# Author: Anna Agosta G'meiner                                                #
# Date: November 2023                                                         #
#                                                                             #
# This script reads a LiDAR point cloud from a .las or .laz file and          #
# processes it using a hexbin filter to calculate the approximate coverage    #
# area of the point cloud. It then extracts the boundary polygon representing # 
# this coverage and saves it to a GeoPackage file.                            #
#                                                                             #
# Disclaimer: This code is created for personal use and is for educational    #
# purposes only.                                                              #
#                                                                             #
###############################################################################

"""Calculate the approximate coverage of the point cloud

Process the LAS file and use the PDAL hexbin filter to
determine the approximate coverage of the point cloud data.

The extent dataset is loaded in a GeoPackage file.
"""

import fiona
import pdal 
import shapely


# input LAS/LAZ filename
filename = 'C:/filepath/*.laz'

# Build PDAL pipeline
pipeline = (
    pdal.Reader.las(filename)
    | pdal.Filter.hexbin(
        edge_size=5
    )
)

# Run pipeline
count = pipeline.execute()
arrays = pipeline.arrays 
metadata = pipeline.metadata
wkt_boundary = metadata['metadata']['filters.hexbin']['boundary']

# Write output polygon to GeoPackage
with fiona.open('C:/filepath/ns-lidar.gpkg',
                mode='w',
                driver='GPKG',
                crs=fiona.crs.CRS.from_epsg(2961), # Adjust EPSG code if needed
                layer='328_4972_201901',
                schema={
                    'geometry': 'Polygon',
                    'properties': {
                        'filename': 'str'
                    }
                }) as gpkg:
    gpkg.write({
        'geometry': shapely.geometry.mapping(shapely.from_wkt(wkt_boundary)),
        'properties': {
            'filename': filename
        }
    })
    
print(f"Coverage polygon written to {output_gpkg} (layer: {layer_name})")