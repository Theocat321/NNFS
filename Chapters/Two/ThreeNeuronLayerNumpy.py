#---------------------------------------------------------------------#
# File: c:\Adam\coding\1. VC Coding projects\NNFS\Chapters\Two\UsingNPFourNeuronLayer.py
# Project: c:\Adam\coding\1. VC Coding projects\NNFS\Chapters\Two
# Created Date: Monday, January 2nd 2023, 10:50:33 pm
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


# Using numpy for a 3 neuron layer
import numpy as np

inputs = [1.0,2.0,3.0,2.5] # Single sample
weights = [ [0.2,0.8,-0.5,1],
            [0.5,-0.91,0.26,-0.5],
            [-0.26,-0.27,0.17,0.87]]
biases = [2.0,3.0,0.5]

layer_ouput = np.dot(weights, inputs) + biases
#             dot product:
#             dot(weights[0],inputs), dot(weights[1],inputs), ....
#             Vector addition to each part
print(layer_ouput)