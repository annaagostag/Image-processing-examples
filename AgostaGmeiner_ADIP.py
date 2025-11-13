###############################################################################
# Course: Advanced Digital Image Processing, REMS6023                         #
# Instructor: Rob Hodder                                                      #
# Author: Anna Agosta G'meiner                                                #
# Date: January 31, 2024                                                      #
#                                                                             #
# Assignment 2: Image Mosaicking in Catalyst & Automation using Python        #
#                                                                             #
# This assignment will use python code to perform a haze removal and          #
# atmospheric correction on Landast scenes. The code will then use the        #
# corrected scenes to create a mosaic of the three Landsat scenes. First,     #
# folders will be created and file paths that will allow the code to be       #
# rerunnbale on any drive or directory. Second, a haze correction will be     #
# applied, then an atmospheric correction, and finally three modules will be  #
# used to create a mosaic. A final mosaic, with a cutline polygon exported as #
# a shapefile, will be produced for the final output.                         #
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
from pci.mosprep import mosprep
from pci.mosdef import mosdef
from pci.mosrun import mosrun
from pci.line2poly import line2poly

print ("\nAssignment 2- Mosaic building in python \n")

#time module
start_time = datetime.datetime.now()
print (f"The start time is {start_time}\n")

"""The os and shutil modules run such that if the pathname exists, it will
delete the folder and create new ones. It allows scripts to be rerunnable."""

print("Creating new folders and deleting any preexisting folders and files.")

root = os.getcwd() #Root allows script to run on any drive/directory

# Creating folders for each step of image correction processing and mosaicking
if os.path.exists(root + '\\' + 'hazerem'):
   shutil.rmtree(root + '\\' + 'hazerem')
if os.path.exists(root + '\\' + 'atcor'):
    shutil.rmtree(root + '\\' + 'atcor')
if os.path.exists(root + '\\' + 'mosaic'):
    shutil.rmtree(root + '\\' + 'mosaic')
 
os.mkdir(root + '\\' + 'hazerem')
os.mkdir(root + '\\' + 'atcor')
os.mkdir(root + '\\' + 'mosaic')

print("New data folders created.\n")

print ("Starting haze removal on three Landsat scenes...")
""" HAZERAM module generates a haze corrected image by correcting radiometric
variability."""

# Perform haze removal using hazerem
hazerem(fili= root + "/Landsat8_France/LC08_L1TP_197028_20200708_20200912_02_T1_MTL.txt-MS_Thermal", 
    filo= root + "/hazerem/Hazerem_France_1.pix")   # output file location/name
hazerem(fili= root + "/Landsat8_France/LC08_L1TP_198028_20200917_20201005_02_T1_MTL.txt-MS_Thermal", 
    filo= root + "/hazerem/Hazerem_France_2.pix")
hazerem(fili= root + "/Landsat8_France/LC08_L1TP_199028_20200908_20200919_02_T1_MTL.txt-MS_Thermal", 
    filo= root + "/hazerem/Hazerem_France_3.pix")

print("Haze removal complete.\n")

print ("Starting atmospheric correction on three Landsat scenes...")
""" ATCOR module recieves a haze-free image and generates a ground-reflectance
image corrected for atmospheric effects."""

#Perform atmospheric correction using atcor
atcor(fili= root + "/hazerem/Hazerem_France_1.pix",
    filo= root + "/atcor/Atcor_France_1.pix")   # output file location/name
atcor(fili= root + "/hazerem/Hazerem_France_2.pix",
    filo= root + "/atcor/Atcor_France_2.pix")
atcor(fili= root + "/hazerem/Hazerem_France_3.pix",
    filo= root + "/atcor/Atcor_France_3.pix")

print("Atmospheric correction complete. \n")

print("Starting mosprep preprocessing on corrected Landsat scenes... \n")

"""MOSPREP module preprocesses scenes to include in a mosaic. A reduced
resolution file is created, normalization coefficients are determined,
colour balancing is performed, and cutlines computed."""
#Run mosprep
mosprep(mfile= root + "/atcor/*.pix", 
    silfile= root + "/mosaic/FranceMosaic_prep.mos")

print("Mosprep preprocessing complete. Preparing second part of preprocessing, mosdef module. \n")

"""MOSDEF module generates an XML definition file for the mosaic which
contains all information necessary to define the output mosaic."""
#Run mosdef
mosdef(silfile= root + "/mosaic/FranceMosaic_prep.mos", 
        mdfile= root + "/mosaic/FranceMosaic_def.xml", dbic= [4,3,2])

print("\nMosdef preprocessing complete. Preparing final part for mosaic creation, the mosrun module.")

"""The MOSRUN module creates a continuous mosaic using the inputs from mosprep
and mosdef. """
#Run mosrun
mosrun(silfile= root + "/mosaic/FranceMosaic_prep.mos",  # mosaic project created by mosprep
    mdfile= root + "/mosaic/FranceMosaic_def.xml",       # mosaic definition file created by mosdef      
    outdir= root + "/mosaic")                # output folder

print("Mosaic proccessing complete. \n")

""" The Line2poly tool is used to create a polygon layer from a vector line layer."""
print("Running line2poly tool...")
#Running Line2Poly tool
line2poly(fili= root + "/mosaic/FranceMosaic_prep/misc/FranceMosaic_prep_cutline_topology.pix", 
          dbvs= [2] , filo= "Cutline_Polygon.shp", ftype= "SHP")

print("Line2poly complete, shapefile created. \n")

stop_time = datetime.datetime.now()
print (f"The stop time is {stop_time - start_time}\n")