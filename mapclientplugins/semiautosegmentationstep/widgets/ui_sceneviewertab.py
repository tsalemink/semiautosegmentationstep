# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sceneviewertab.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from mapclientplugins.semiautosegmentationstep.widgets.tabtoolbar import TabToolBar
from mapclientplugins.semiautosegmentationstep.widgets.zincwidgetstate import ZincWidgetState


class Ui_SceneviewerTab(object):
    def setupUi(self, SceneviewerTab):
        if not SceneviewerTab.objectName():
            SceneviewerTab.setObjectName(u"SceneviewerTab")
        SceneviewerTab.resize(400, 300)
        self.verticalLayout = QVBoxLayout(SceneviewerTab)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self._tabToolBar = TabToolBar(SceneviewerTab)
        self._tabToolBar.setObjectName(u"_tabToolBar")
        self._tabToolBar.setMinimumSize(QSize(0, 15))

        self.verticalLayout.addWidget(self._tabToolBar)

        self._zincwidget = ZincWidgetState(SceneviewerTab)
        self._zincwidget.setObjectName(u"_zincwidget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(10)
        sizePolicy.setHeightForWidth(self._zincwidget.sizePolicy().hasHeightForWidth())
        self._zincwidget.setSizePolicy(sizePolicy)
        self._zincwidget.setMinimumSize(QSize(100, 200))

        self.verticalLayout.addWidget(self._zincwidget)


        self.retranslateUi(SceneviewerTab)

        QMetaObject.connectSlotsByName(SceneviewerTab)
    # setupUi

    def retranslateUi(self, SceneviewerTab):
        SceneviewerTab.setWindowTitle(QCoreApplication.translate("SceneviewerTab", u"Form", None))
    # retranslateUi

