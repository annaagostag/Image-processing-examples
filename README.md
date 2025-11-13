# Image Mosaicking and Atmospheric Correction using Python & PCI Catalyst
This project automates a **Landsat image processing workflow** using **Python** and **PCI Catalyst**.  
The script performs **haze removal**, **atmospheric correction**, and **mosaicking** of multiple Landsat scenes, producing a final mosaic image and a shapefile cutline.

---
## Overview

The workflow is fully automated and rerunnable and will create clean working directories on each run and processes all scenes in sequence.  
Steps include:
1. Haze removal (`hazerem`)
2. Atmospheric correction (`atcor`)
3. Mosaic preparation, definition, and execution (`mosprep`, `mosdef`, `mosrun`)
4. Export of the final mosaic and cutline shapefile (`line2poly`)

---
## Requirements

- **PCI Geomatics Catalyst** (with Python API access)
- **Python 3.x**
- Standard Python libraries: `os`, `shutil`, `datetime`, `pci`

---
## How to Run

1. Place your Landsat scene folders inside the project directory.  
2. Run the script in a PCI Catalyst enabled Python environment:

   ```bash
   python mosaicking.py

/hazerem   - Haze-corrected images  
/atcor     - Atmospherically corrected images  
/mosaic    - Final mosaic and shapefile outputs

## Outputs
FranceMosaic.tif - final mosaicked image

Cutline_Polygon.shp - shapefile polygon of the mosaic cutline

## Author
**Anna Agosta G’meiner**
*Advanced Digital Image Processing*
*Instructor: Rob Hodder*
*Date: January 31, 2024*
