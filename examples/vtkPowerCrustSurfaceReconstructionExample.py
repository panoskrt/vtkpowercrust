'''
    An example for vtkPowerCrustSurfaceReconstruction algorithm in Python.
    Copyright (C) 2015 Panagiotis Kritikakos

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

# This is based on the example code of Arash Akbarinia as published on GitHub:
# https://github.com/timhutton/vtkpowercrust/blob/master/examples/vtkPowerCrustSurfaceReconstructionExample.cxx

import sys
import os
import vtk

if( (len(sys.argv)<2) or (len(sys.argv)>2) ):
	print("Usage: python powercrust.py <path_to_.ply_files>")
	exit(1)

path = sys.argv[1]

if (os.path.exists(path)):
	for plyfile in os.listdir(path):
		if (plyfile.endswith(".ply")):
			reader = vtk.vtkPLYReader()
			reader.SetFileName(plyfile)
			reader.Update()

			print("File: {0}".format(plyfile))
			print("Number of points: {0}".format(reader.GetOutput().GetPoints().GetNumberOfPoints()));

			pcr = vtk.vtkPowerCrustSurfaceReconstruction()
			pcr.SetInput(reader.GetOutput())
			pcr.Update()

			writer = vtk.vtkPLYWriter()
			writer.SetInput(pcr.GetOutput())
			writer.SetFileName("powercrust_{0}".format(plyfile))
			writer.Write()
	exit(0)
else:
	print("The provided path does not exist!")
	exit(1)
