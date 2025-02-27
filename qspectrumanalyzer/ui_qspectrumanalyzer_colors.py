# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qspectrumanalyzer_colors.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QSpectrumAnalyzerColors(object):
    def setupUi(self, QSpectrumAnalyzerColors):
        QSpectrumAnalyzerColors.setObjectName("QSpectrumAnalyzerColors")
        QSpectrumAnalyzerColors.resize(253, 266)
        self.verticalLayout = QtWidgets.QVBoxLayout(QSpectrumAnalyzerColors)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(QSpectrumAnalyzerColors)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.mainColorButton = ColorButton(QSpectrumAnalyzerColors)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.mainColorButton.sizePolicy().hasHeightForWidth())
        self.mainColorButton.setSizePolicy(sizePolicy)
        self.mainColorButton.setObjectName("mainColorButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.mainColorButton)
        self.label_4 = QtWidgets.QLabel(QSpectrumAnalyzerColors)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.peakHoldMaxColorButton = ColorButton(QSpectrumAnalyzerColors)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.peakHoldMaxColorButton.sizePolicy().hasHeightForWidth())
        self.peakHoldMaxColorButton.setSizePolicy(sizePolicy)
        self.peakHoldMaxColorButton.setObjectName("peakHoldMaxColorButton")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.peakHoldMaxColorButton)
        self.label_6 = QtWidgets.QLabel(QSpectrumAnalyzerColors)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.peakHoldMinColorButton = ColorButton(QSpectrumAnalyzerColors)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.peakHoldMinColorButton.sizePolicy().hasHeightForWidth())
        self.peakHoldMinColorButton.setSizePolicy(sizePolicy)
        self.peakHoldMinColorButton.setObjectName("peakHoldMinColorButton")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.peakHoldMinColorButton)
        self.label_5 = QtWidgets.QLabel(QSpectrumAnalyzerColors)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.averageColorButton = ColorButton(QSpectrumAnalyzerColors)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.averageColorButton.sizePolicy().hasHeightForWidth())
        self.averageColorButton.setSizePolicy(sizePolicy)
        self.averageColorButton.setObjectName("averageColorButton")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.averageColorButton)
        self.label_3 = QtWidgets.QLabel(QSpectrumAnalyzerColors)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.persistenceColorButton = ColorButton(QSpectrumAnalyzerColors)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.persistenceColorButton.sizePolicy().hasHeightForWidth())
        self.persistenceColorButton.setSizePolicy(sizePolicy)
        self.persistenceColorButton.setObjectName("persistenceColorButton")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.persistenceColorButton)
        self.label = QtWidgets.QLabel(QSpectrumAnalyzerColors)
        self.label.setObjectName("label")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label)
        self.baselineColorButton = ColorButton(QSpectrumAnalyzerColors)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.baselineColorButton.sizePolicy().hasHeightForWidth())
        self.baselineColorButton.setSizePolicy(sizePolicy)
        self.baselineColorButton.setObjectName("baselineColorButton")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.baselineColorButton)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 2, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(QSpectrumAnalyzerColors)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_2.setBuddy(self.mainColorButton)
        self.label_4.setBuddy(self.peakHoldMaxColorButton)
        self.label_6.setBuddy(self.peakHoldMinColorButton)
        self.label_5.setBuddy(self.averageColorButton)
        self.label_3.setBuddy(self.persistenceColorButton)
        self.label.setBuddy(self.baselineColorButton)

        self.retranslateUi(QSpectrumAnalyzerColors)
        self.buttonBox.accepted.connect(QSpectrumAnalyzerColors.accept) # type: ignore
        self.buttonBox.rejected.connect(QSpectrumAnalyzerColors.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(QSpectrumAnalyzerColors)
        QSpectrumAnalyzerColors.setTabOrder(self.mainColorButton, self.peakHoldMaxColorButton)
        QSpectrumAnalyzerColors.setTabOrder(self.peakHoldMaxColorButton, self.peakHoldMinColorButton)
        QSpectrumAnalyzerColors.setTabOrder(self.peakHoldMinColorButton, self.averageColorButton)
        QSpectrumAnalyzerColors.setTabOrder(self.averageColorButton, self.persistenceColorButton)
        QSpectrumAnalyzerColors.setTabOrder(self.persistenceColorButton, self.baselineColorButton)

    def retranslateUi(self, QSpectrumAnalyzerColors):
        _translate = QtCore.QCoreApplication.translate
        QSpectrumAnalyzerColors.setWindowTitle(_translate("QSpectrumAnalyzerColors", "Colors - QSpectrumAnalyzer"))
        self.label_2.setText(_translate("QSpectrumAnalyzerColors", "&Main curve color:"))
        self.mainColorButton.setText(_translate("QSpectrumAnalyzerColors", "..."))
        self.label_4.setText(_translate("QSpectrumAnalyzerColors", "Max. peak &hold color:"))
        self.peakHoldMaxColorButton.setText(_translate("QSpectrumAnalyzerColors", "..."))
        self.label_6.setText(_translate("QSpectrumAnalyzerColors", "M&in. peak hold color:"))
        self.peakHoldMinColorButton.setText(_translate("QSpectrumAnalyzerColors", "..."))
        self.label_5.setText(_translate("QSpectrumAnalyzerColors", "Average &color:"))
        self.averageColorButton.setText(_translate("QSpectrumAnalyzerColors", "..."))
        self.label_3.setText(_translate("QSpectrumAnalyzerColors", "Persistence co&lor:"))
        self.persistenceColorButton.setText(_translate("QSpectrumAnalyzerColors", "..."))
        self.label.setText(_translate("QSpectrumAnalyzerColors", "&Baseline color:"))
        self.baselineColorButton.setText(_translate("QSpectrumAnalyzerColors", "..."))
from pyqtgraph import ColorButton
