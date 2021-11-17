import sys
import json
from pathlib import Path
from PySide6.QtQuick import QQuickView
from PySide6.QtCore import QStringListModel, QUrl
from PySide6.QtGui import QGuiApplication
import time

if __name__ == '__main__':

    #Set up the application window
    app = QGuiApplication(sys.argv)
    view = QQuickView()
    view.setResizeMode(QQuickView.SizeRootObjectToView)

    #Load the QML file
    qml_file = Path(__file__).parent / "Screen01.ui.qml"
    view.setSource(QUrl.fromLocalFile(qml_file.resolve()))

    #Show the window
    if view.status() == QQuickView.Error:
        sys.exit(-1)
    view.show()
    
    #execute and cleanup
    app.exec_()
    time.sleep(10)
    del view
