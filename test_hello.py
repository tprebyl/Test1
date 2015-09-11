#-------------------------------------------------------------
# Name:       maximize_subnet.py
# Purpose:    Identifies barriers for removal that will maximize the length of a connected subnetwork
# Authors:      Thomas J. Prebyl, Evan Collins, Duncan Elkins, Nathan Nibbelink, Warnell School of Forestry and Natural Resources
# Created:    08/12/2014
# ArcGIS Version:   10.2.2 (with 64 bit background geoprocessing enabled)
# Python Version:   2.7.5 (64 bit)
# Contact: tprebyl at gmail dot com
#-------------------------------------------------------------

#-----Import Compiled Cython functions to calc DCI barrier removal
import os
import sys
sys.path.append("C:\\Data\\Viivo\\Projects\\StreamConn\\Working\\Tool\\Stream_Network_Tools_64\\Scripts")
#sys.path.append(os.path.dirname(__file__))
from barr_remove5 import my_arr_fun as bremove
from cy_strm_len3 import sum_strm_len
from strm_len_2strms import sum_strm_len as sum_2strms

#-----import Arcpy, check out any needed extensions,set environment
print "importing libraries..."
import pandas as pd    #created using version 0.13.1 64 bit
import numpy as np     #created using version 1.7.1 64 bit (distributed with ArcGIS 10.2.2)
import igraph as ig   #created using version 0.7.0 64 bit
import itertools
import arcpy
from arcpy import env

def hello():
    print 'hi there'

print 'finished'
print 'finished again'
