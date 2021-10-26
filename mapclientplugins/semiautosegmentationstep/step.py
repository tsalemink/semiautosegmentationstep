"""
MAP Client, a program to generate detailed musculoskeletal models for OpenSim.
    Copyright (C) 2012  University of Auckland

This file is part of MAP Client. (http://launchpad.net/mapclient)

    MAP Client is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    MAP Client is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with MAP Client.  If not, see <http://www.gnu.org/licenses/>..
"""
import os

from PySide2 import QtGui, QtWidgets

from mapclient.mountpoints.workflowstep import WorkflowStepMountPoint

from mapclientplugins.semiautosegmentationstep.model.master import SegmentationModel
from mapclientplugins.semiautosegmentationstep.widgets.segmentationwidget import SegmentationWidget

STEP_SERIALISATION_FILENAME = 'step.conf'


class SegmentationStep(WorkflowStepMountPoint):
    """
    A step that acts like the step plugin duck
    """

    def __init__(self, location):
        """
        Constructor
        """
        super(SegmentationStep, self).__init__('Segmentation', location)
        self._identifier = ''
        # self._icon = QtGui.QImage(':/segmentation/icons/seg.gif')
        self._icon = QtGui.QImage(':/segmentation/icons/segmentationicon.png')
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#uses',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#images'))
        self.addPort(('http://physiomeproject.org/workflow/1.0/rdf-schema#port',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#provides',
                      'http://physiomeproject.org/workflow/1.0/rdf-schema#pointcloud'))
        self._model = SegmentationModel()
        self._category = 'Segmentation'
        self._view = None
        self._dataIn = None
        self._configured = True

    def configure(self):
        pass

    def getIdentifier(self):
        return self._identifier

    def setIdentifier(self, identifier):
        self._identifier = identifier

    def serialize(self):
        pass

    def deserialize(self, string):
        pass

    def setPortData(self, portId, dataIn):
        self._dataIn = dataIn

    def getPortData(self, portId):
        return self._model.getPointCloud()

    def execute(self):
        if self._view is None:
            self._model.loadImages(self._dataIn)
            self._model.initialize()
            self._view = SegmentationWidget(self._model)
            self._view.setSerializationLocation(os.path.join(self._location, self.getIdentifier()))
            self._view.registerDoneExecution(self._doneExecution)

        self._setCurrentUndoRedoStack(self._model.getUndoRedoStack())
        self._setCurrentWidget(self._view)
