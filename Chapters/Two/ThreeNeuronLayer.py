#---------------------------------------------------------------------#
# File: c:\Adam\coding\1. VC Coding projects\NNFS\FourNeuronLayer.py
# Project: c:\Adam\coding\1. VC Coding projects\NNFS
# Created Date: Monday, January 2nd 2023, 10:14:26 pm
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

# This is a simulation of a layer of 3 neurons taking input from a layer of 4 neurons
# An example of a fully connected network, each neuron is connected to every other neuron in previous layer

inputs = [1,2,3,2.5]

weights1 = [0.2,0.8,-0.5,1]
weights2 = [0.5,-0.91,0.26,-0.5]
weights3 = [-0.26,-0.27,0.17,0.87]

bias1 = 2
bias2 = 3
bias3 = 0.5

outputs = [ inputs[0]*weights1[0]+
            inputs[1]*weights1[1]+
            inputs[2]*weights1[2]+
            inputs[3]*weights1[3]+ bias1,

            inputs[0]*weights2[0]+
            inputs[1]*weights2[1]+
            inputs[2]*weights2[2]+
            inputs[3]*weights2[3]+ bias2,

            
            inputs[0]*weights3[0]+
            inputs[1]*weights3[1]+
            inputs[2]*weights3[2]+
            inputs[3]*weights3[3]+ bias3]
print(outputs)

# This method can also be completed using loops

# zip() function is useful in python

# All of this maths is a dot product, numpy can be used to do this
