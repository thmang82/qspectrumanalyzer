# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'qspectrumanalyzer_settings.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QSpectrumAnalyzerSettings(object):
    def setupUi(self, QSpectrumAnalyzerSettings):
        QSpectrumAnalyzerSettings.setObjectName("QSpectrumAnalyzerSettings")
        QSpectrumAnalyzerSettings.resize(600, 388)
        self.verticalLayout = QtWidgets.QVBoxLayout(QSpectrumAnalyzerSettings)
        self.verticalLayout.setObjectName("verticalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label_3 = QtWidgets.QLabel(QSpectrumAnalyzerSettings)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.backendComboBox = QtWidgets.QComboBox(QSpectrumAnalyzerSettings)
        self.backendComboBox.setObjectName("backendComboBox")
        self.backendComboBox.addItem("")
        self.backendComboBox.addItem("")
        self.backendComboBox.addItem("")
        self.backendComboBox.addItem("")
        self.backendComboBox.addItem("")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.backendComboBox)
        self.label = QtWidgets.QLabel(QSpectrumAnalyzerSettings)
        self.label.setObjectName("label")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.executableEdit = QtWidgets.QLineEdit(QSpectrumAnalyzerSettings)
        self.executableEdit.setObjectName("executableEdit")
        self.horizontalLayout.addWidget(self.executableEdit)
        self.executableButton = QtWidgets.QToolButton(QSpectrumAnalyzerSettings)
        self.executableButton.setMinimumSize(QtCore.QSize(50, 0))
        self.executableButton.setObjectName("executableButton")
        self.horizontalLayout.addWidget(self.executableButton)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.label_5 = QtWidgets.QLabel(QSpectrumAnalyzerSettings)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_4 = QtWidgets.QLabel(QSpectrumAnalyzerSettings)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_2 = QtWidgets.QLabel(QSpectrumAnalyzerSettings)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.waterfallHistorySizeSpinBox = QtWidgets.QSpinBox(QSpectrumAnalyzerSettings)
        self.waterfallHistorySizeSpinBox.setMinimum(1)
        self.waterfallHistorySizeSpinBox.setMaximum(10000000)
        self.waterfallHistorySizeSpinBox.setProperty("value", 100)
        self.waterfallHistorySizeSpinBox.setObjectName("waterfallHistorySizeSpinBox")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.FieldRole, self.waterfallHistorySizeSpinBox)
        self.label_7 = QtWidgets.QLabel(QSpectrumAnalyzerSettings)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(QSpectrumAnalyzerSettings)
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.label_6 = QtWidgets.QLabel(QSpectrumAnalyzerSettings)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.paramsEdit = QtWidgets.QLineEdit(QSpectrumAnalyzerSettings)
        self.paramsEdit.setObjectName("paramsEdit")
        self.horizontalLayout_2.addWidget(self.paramsEdit)
        self.paramsHelpButton = QtWidgets.QToolButton(QSpectrumAnalyzerSettings)
        self.paramsHelpButton.setMinimumSize(QtCore.QSize(50, 0))
        self.paramsHelpButton.setObjectName("paramsHelpButton")
        self.horizontalLayout_2.addWidget(self.paramsHelpButton)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.deviceEdit = QtWidgets.QLineEdit(QSpectrumAnalyzerSettings)
        self.deviceEdit.setObjectName("deviceEdit")
        self.horizontalLayout_3.addWidget(self.deviceEdit)
        self.deviceHelpButton = QtWidgets.QToolButton(QSpectrumAnalyzerSettings)
        self.deviceHelpButton.setMinimumSize(QtCore.QSize(50, 0))
        self.deviceHelpButton.setObjectName("deviceHelpButton")
        self.horizontalLayout_3.addWidget(self.deviceHelpButton)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        self.sampleRateSpinBox = QtWidgets.QDoubleSpinBox(QSpectrumAnalyzerSettings)
        self.sampleRateSpinBox.setProperty("showGroupSeparator", True)
        self.sampleRateSpinBox.setDecimals(3)
        self.sampleRateSpinBox.setMinimum(0.0)
        self.sampleRateSpinBox.setMaximum(999999.99)
        self.sampleRateSpinBox.setSingleStep(0.01)
        self.sampleRateSpinBox.setProperty("value", 61.44)
        self.sampleRateSpinBox.setObjectName("sampleRateSpinBox")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.sampleRateSpinBox)
        self.bandwidthSpinBox = QtWidgets.QDoubleSpinBox(QSpectrumAnalyzerSettings)
        self.bandwidthSpinBox.setProperty("showGroupSeparator", True)
        self.bandwidthSpinBox.setDecimals(3)
        self.bandwidthSpinBox.setMinimum(0.0)
        self.bandwidthSpinBox.setMaximum(999999.99)
        self.bandwidthSpinBox.setSingleStep(0.01)
        self.bandwidthSpinBox.setProperty("value", 0.0)
        self.bandwidthSpinBox.setObjectName("bandwidthSpinBox")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.bandwidthSpinBox)
        self.lnbSpinBox = QtWidgets.QDoubleSpinBox(QSpectrumAnalyzerSettings)
        self.lnbSpinBox.setProperty("showGroupSeparator", True)
        self.lnbSpinBox.setDecimals(3)
        self.lnbSpinBox.setMinimum(-999999.999)
        self.lnbSpinBox.setMaximum(999999.999)
        self.lnbSpinBox.setSingleStep(0.01)
        self.lnbSpinBox.setProperty("value", 0.0)
        self.lnbSpinBox.setObjectName("lnbSpinBox")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.lnbSpinBox)
        self.verticalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 21, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtWidgets.QDialogButtonBox(QSpectrumAnalyzerSettings)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)
        self.label_3.setBuddy(self.backendComboBox)
        self.label.setBuddy(self.executableEdit)
        self.label_5.setBuddy(self.deviceEdit)
        self.label_4.setBuddy(self.sampleRateSpinBox)
        self.label_2.setBuddy(self.waterfallHistorySizeSpinBox)
        self.label_7.setBuddy(self.bandwidthSpinBox)
        self.label_8.setBuddy(self.lnbSpinBox)
        self.label_6.setBuddy(self.paramsEdit)

        self.retranslateUi(QSpectrumAnalyzerSettings)
        self.buttonBox.accepted.connect(QSpectrumAnalyzerSettings.accept) # type: ignore
        self.buttonBox.rejected.connect(QSpectrumAnalyzerSettings.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(QSpectrumAnalyzerSettings)
        QSpectrumAnalyzerSettings.setTabOrder(self.backendComboBox, self.executableEdit)
        QSpectrumAnalyzerSettings.setTabOrder(self.executableEdit, self.executableButton)
        QSpectrumAnalyzerSettings.setTabOrder(self.executableButton, self.paramsEdit)
        QSpectrumAnalyzerSettings.setTabOrder(self.paramsEdit, self.paramsHelpButton)
        QSpectrumAnalyzerSettings.setTabOrder(self.paramsHelpButton, self.deviceEdit)
        QSpectrumAnalyzerSettings.setTabOrder(self.deviceEdit, self.deviceHelpButton)
        QSpectrumAnalyzerSettings.setTabOrder(self.deviceHelpButton, self.sampleRateSpinBox)
        QSpectrumAnalyzerSettings.setTabOrder(self.sampleRateSpinBox, self.bandwidthSpinBox)
        QSpectrumAnalyzerSettings.setTabOrder(self.bandwidthSpinBox, self.lnbSpinBox)
        QSpectrumAnalyzerSettings.setTabOrder(self.lnbSpinBox, self.waterfallHistorySizeSpinBox)

    def retranslateUi(self, QSpectrumAnalyzerSettings):
        _translate = QtCore.QCoreApplication.translate
        QSpectrumAnalyzerSettings.setWindowTitle(_translate("QSpectrumAnalyzerSettings", "Settings - QSpectrumAnalyzer"))
        self.label_3.setText(_translate("QSpectrumAnalyzerSettings", "&Backend:"))
        self.backendComboBox.setItemText(0, _translate("QSpectrumAnalyzerSettings", "soapy_power"))
        self.backendComboBox.setItemText(1, _translate("QSpectrumAnalyzerSettings", "rx_power"))
        self.backendComboBox.setItemText(2, _translate("QSpectrumAnalyzerSettings", "rtl_power_fftw"))
        self.backendComboBox.setItemText(3, _translate("QSpectrumAnalyzerSettings", "rtl_power"))
        self.backendComboBox.setItemText(4, _translate("QSpectrumAnalyzerSettings", "hackrf_sweep"))
        self.label.setText(_translate("QSpectrumAnalyzerSettings", "E&xecutable:"))
        self.executableEdit.setText(_translate("QSpectrumAnalyzerSettings", "soapy_power"))
        self.executableButton.setText(_translate("QSpectrumAnalyzerSettings", "..."))
        self.label_5.setText(_translate("QSpectrumAnalyzerSettings", "&Device:"))
        self.label_4.setText(_translate("QSpectrumAnalyzerSettings", "Sa&mple rate:"))
        self.label_2.setText(_translate("QSpectrumAnalyzerSettings", "&Waterfall history size:"))
        self.label_7.setText(_translate("QSpectrumAnalyzerSettings", "Bandwidt&h:"))
        self.label_8.setToolTip(_translate("QSpectrumAnalyzerSettings", "Negative frequency for upconverters, positive frequency for downconverters."))
        self.label_8.setText(_translate("QSpectrumAnalyzerSettings", "&LNB LO:"))
        self.label_6.setText(_translate("QSpectrumAnalyzerSettings", "Add&itional parameters:"))
        self.paramsHelpButton.setText(_translate("QSpectrumAnalyzerSettings", " ? "))
        self.deviceHelpButton.setText(_translate("QSpectrumAnalyzerSettings", " ? "))
        self.sampleRateSpinBox.setSuffix(_translate("QSpectrumAnalyzerSettings", " MHz"))
        self.bandwidthSpinBox.setSuffix(_translate("QSpectrumAnalyzerSettings", " MHz"))
        self.lnbSpinBox.setToolTip(_translate("QSpectrumAnalyzerSettings", "Negative frequency for upconverters, positive frequency for downconverters."))
        self.lnbSpinBox.setSuffix(_translate("QSpectrumAnalyzerSettings", " MHz"))
