###############################################################################
# Course: Advanced Digital Image Processing, REMS6023                         #
# Instructor: Rob Hodder                                                      #
# Author: Anna Agosta G'meiner                                                #
# Date: March 3, 2024                                                         #
#                                                                             #
# Assignment 4: PCA and TCT using Python                                      #
#                                                                             #
# This assignment will use python code to perform a haze removal and          #
# atmospheric correction on a Landast scene. The code will then use the       #
# corrected  and clipped down scene to run Principal Component Analysis and   #
# Tasseled-cap transformation on the Landsat scene.                           #
# A final report with the PCA matrix will be created, along with a PIX file   #
# of an RGB composite showing the top 3 PCA bands used.                       #
#                                                                             #
# Disclaimer: This code is created as part of the requirements for the course #
# REMS6023 and is for educational purposes only.                              #
#                                                                             #
###############################################################################

""" Import modules to run pci catalyst specific code """

import pci
import os
import shutil
import datetime

from pci.hazerem import hazerem
from pci.atcor import atcor
from pci.clip import clip
from pci.pcimod import pcimod
from pci.nspio import Report, enableDefaultReport
from pci.exceptions import PCIException
from pci.pca import pca
from pci.tassel import tassel
from pci.fexport import fexport

print ("\nAssignment 4- Principal Component Analysis and Tasselelled Cap Transformations in Python \n")

#time module
start_time = datetime.datetime.now()
print(f"The start time is {start_time}\n")

"""The os and shutil modules run such that if the pathname exists, it will
delete the folder and create new ones. It allows scripts to be rerunnable."""

print("Creating new folders and deleting any preexisting folders and files.")

root = os.getcwd() #Root allows script to run on any drive/directory

# Creating folders for each step of image correction processing
if os.path.exists(root + '\\' + 'hazerem'):
   shutil.rmtree(root + '\\' + 'hazerem')
if os.path.exists(root + '\\' + 'atcor'):
    shutil.rmtree(root + '\\' + 'atcor')

os.mkdir(root + '\\' + 'hazerem')
os.mkdir(root + '\\' + 'atcor')

print("New data folders created.\n")

print("Starting haze removal on Landsat scene...")
""" HAZERAM module generates a haze corrected image by correcting radiometric
variability."""

# Perform haze removal using hazerem
hazerem(fili= root + "/LC08_L1TP_008029_20201016_20201104_01_T1_MTL.txt-MS_Thermal", 
    filo= root + "/hazerem/Hazerem_Halifax.pix")   # output file location/name

print("Haze removal complete.\n")

print("Starting atmospheric correction on Landsat scene...")
""" ATCOR module recieves a haze-free image and generates a ground-reflectance
image corrected for atmospheric effects."""

# Perform atmospheric correction using atcor
atcor(fili= root + "/hazerem/Hazerem_Halifax.pix",
    filo= root + "/atcor/Atcor_Halifax.pix")

print("Atmospheric correction complete. \n")

# Clipping down Landsat scene
print("Clipping Landsat scene.")
clip(fili= root + "/atcor/Atcor_Halifax.pix",
    dbic= [1,2,3,4,5,6,7], filo = root + "/Halifax_PCA_Clip", ftype= "PIX", clipfil= root + "/clip_file/Halifax_clip.shp")

print("Adding new channels to Landsat scene.\n")
""" PCIMOD module adds or deletes image channels."""

# Adding 7 new channels, each 32-bit unsigned
pcimod( file = root + "/Halifax_PCA_Clip",
       pciop = "ADD", pcival = [0,0,0,7,0,0])

print("Starting Principal Component Analysis on Landsat scene...")
""" PCA module is a linear transformation that rotates image along lines of maximum variance."""

report_pca = (root + "/Halifax_PCA-report.txt") # Creating PCA report
Report.clear()
enableDefaultReport(report_pca)

# Running PCA
pca(file= root + "/Halifax_PCA_Clip",
    dbic= [1,2,3,4,5,6,7],  # selecting bands for pca
    eign= [1,2,3,4,5,6,7], 
    dboc= [8,9,10,11,12,13,14],  # output channels
    rtype = "LONG")

print("PCA complete, report created. \n")

print("Starting Tasseled-Cap Transformation on Landsat scene...")
""" TCT module creates a tasseled-cap transformation for various sensors using a linear transformation."""

# Running TCT
tassel(fili= root + "/Halifax_PCA_Clip", visirchn= [2,3,4,5,6,7], filo= "Halifax_TCT", datatype= "32R")
print("TCT complete. \n")

# Exporting files
fexport(fili= root + "/Halifax_PCA_Clip", filo= "Halifax_Final_PCA.pix", dbic= [8,9,10])

print("PIX file created for PCA. \n")

stop_time = datetime.datetime.now()
print(f"The stop time is {stop_time - start_time}\n")