import QtQuick
import QtQuick.Controls

Page {
    width: 600
    height: 400

    title: qsTr("Page 1")

    Label {
        text: qsTr("You are on Page 1.")
        anchors.centerIn: parent
    }
    Image {
        id: image
        x: 58
        y: 62
        width: 423
        height: 287
        opacity: 1
        source: "Diagnostic.png"
        layer.enabled: false
        sourceSize.width: 5
        fillMode: Image.PreserveAspectFit
    }
}
