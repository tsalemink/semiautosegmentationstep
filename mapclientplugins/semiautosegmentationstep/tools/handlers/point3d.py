'''
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
'''
from mapclientplugins.semiautosegmentationstep.tools.handlers.point import Point
from mapclientplugins.semiautosegmentationstep.definitions import POINT_CLOUD_GRAPHIC_NAME

class Point3D(Point):
    pass

    def _createScenepickerFilter(self):
        sceneviewer = self._zinc_view.getSceneviewer()
        scene = sceneviewer.getScene()
        filtermodule = scene.getScenefiltermodule()
        name_filter1 = filtermodule.createScenefilterGraphicsName(POINT_CLOUD_GRAPHIC_NAME)

        name_filter = filtermodule.createScenefilterOperatorOr()
        name_filter.appendOperand(name_filter1)

        return name_filter


