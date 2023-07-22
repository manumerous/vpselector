__author__ = "Manuel Yves Galliker"
__maintainer__ = "Manuel Yves Galliker"
__license__ = "Apache-2.0"

from PyQt5 import QtCore
from PyQt5.QtWidgets import QVBoxLayout, QWidget, QDialog, QDialogButtonBox

class ConfirmSelectionWindow(QDialog):
    def __init__(self):
        super().__init__()

        buttonBox = QDialogButtonBox(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)

        buttonBox.accepted.connect(self.accept)
        buttonBox.rejected.connect(self.reject)

        layout = QVBoxLayout()

        layout.addWidget(buttonBox)

        # Set dialog layout
        self.setLayout(layout)
        self.setWindowTitle("Confirm selection")
        self.setWindowModality(QtCore.Qt.ApplicationModal)
