import QtQuick
import QtQuick.Window

Window {
    width: 640
    height: 480
    visible: true
    title: qsTr("Hello World")

    Image {
        id: image
        x: 185
        y: 194
        width: 100
        height: 100
        source: "Box.png"
        fillMode: Image.PreserveAspectFit
    }

}
