from Qt import QtCore, QtWidgets

from qspectrumanalyzer.ui_qspectrumanalyzer_smoothing_temporal import Ui_QSpectrumAnalyzerSmoothingTemporal


class QSpectrumAnalyzerSmoothingTemporal(QtWidgets.QDialog, Ui_QSpectrumAnalyzerSmoothingTemporal):
    """QSpectrumAnalyzer temporal smoothing dialog"""
    def __init__(self, parent=None):
        # Initialize UI
        super().__init__(parent)
        self.setupUi(self)

        # Load settings
        settings = QtCore.QSettings()
        self.windowLengthSpinBox.setValue(settings.value("temporal_smooth_length", 11, int))

        window_function = settings.value("temporal_smooth_window", "hanning")
        i = self.windowFunctionComboBox.findText(window_function)
        if i == -1:
            self.windowFunctionComboBox.setCurrentIndex(0)
        else:
            self.windowFunctionComboBox.setCurrentIndex(i)

    def accept(self):
        """Save settings when dialog is accepted"""
        settings = QtCore.QSettings()
        settings.setValue("temporal_smooth_length", self.windowLengthSpinBox.value())
        settings.setValue("temporal_smooth_window", self.windowFunctionComboBox.currentText())
        QtWidgets.QDialog.accept(self)
