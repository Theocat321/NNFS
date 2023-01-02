#---------------------------------------------------------------------#
# File: c:\Adam\coding\1. VC Coding projects\NNFS\Chapters\Two\dotproduct.py
# Project: c:\Adam\coding\1. VC Coding projects\NNFS\Chapters\Two
# Created Date: Monday, January 2nd 2023, 10:44:07 pm
# Description: 
# Author: Adam O'Neill
# Copyright (c) 2023 Adam O'Neill
# -----
# Last Modified: Mon Jan 02 2023
# Modified By: Adam O'Neill
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	---------------------------------------------------------
#---------------------------------------------------------------------#

# Calculating dot product of two vectors

a = [1,2,3] # This could be inputs
b = [2,3,4] # This could be weights
bias = 3
dot_product = a[0]*b[0] + a[1]*b[1] + a[2]*b[2]
print(dot_product +bias)

# Completeing using numPy
import numpy as np

ouputs = np.dot(a,b) + bias

print(ouputs)