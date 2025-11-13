# PCA and Tasseled-Cap Transformation on Landsat Scenes using Python & PCI Catalyst

This project automates a **Landsat image processing workflow** using **Python** and **PCI Catalyst**.  
The script performs **haze removal**, **atmospheric correction**, **clipping**, **Principal Component Analysis (PCA)**, and **Tasseled-Cap Transformation (TCT)** on a Landsat scene, producing a PCA report and an RGB composite of the top PCA bands.

---
## Overview

The workflow is fully automated and rerunnable, and it creates clean working directories on each run and processes the Landsat scene in sequence.  
Steps include:

1. **Haze removal** (`hazerem`) – corrects radiometric variability.  
2. **Atmospheric correction** (`atcor`) – generates ground-reflectance images corrected for atmospheric effects.  
3. **Clipping** (`clip`) – reduces the image extent to a defined shapefile area.  
4. **Channel modification** (`pcimod`) – adds or deletes image channels for PCA and TCT.  
5. **Principal Component Analysis** (`pca`) – linear transformation to rotate image along lines of maximum variance.  
6. **Tasseled-Cap Transformation** (`tassel`) – creates TCT for various sensors.  
7. **File export** (`fexport`) – exports PCA results as a PIX file for visualization.

---
## Requirements

- **PCI Geomatics Catalyst** (with Python API access)  
- **Python 3.x**  
- Standard Python libraries: `os`, `shutil`, `datetime`, `pci`

---
## How to Run

1. Place your Landsat scene folder inside the project directory.  
2. Run the script in a PCI Catalyst–enabled Python environment:

   ```bash
   python pca_tct.py

/hazerem   - Haze-corrected image  
/atcor     - Atmospherically corrected image  
/Halifax_PCA_Clip - Clipped and modified Landsat image for PCA/TCT

## Outputs

Halifax_PCA-report.txt - text report of the PCA matrix  
Halifax_TCT.pix - Tasseled-Cap Transformation output  
Halifax_Final_PCA.pix - RGB composite using the top 3 PCA bands

## Author
Anna Agosta G’meiner  
Advanced Digital Image Processing  
Instructor: Rob Hodder  
Date: March 3, 2024 

## Disclaimer  
This code was developed as part of the course REMS6023 – Advanced Digital Image Processing and is intended for educational and demonstration purposes only.
