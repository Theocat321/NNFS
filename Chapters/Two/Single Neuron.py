#---------------------------------------------------------------------#
# File: c:\Adam\coding\1. VC Coding projects\NNFS\NeuralNet.py
# Project: c:\Adam\coding\1. VC Coding projects\NNFS
# Created Date: Monday, January 2nd 2023, 10:06:05 pm
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


# This network has 3 inputs, each input has a weight
# Each neuron has a bias
inputs = [1,2,3]
weights = [0.2,0.8,-0.5]
bias = 2

# Sums each inpuit * input weight
output = (inputs[0]*weights[0]+
        inputs[1]*weights[1]+
        inputs[2]*weights[2]
        + bias)
