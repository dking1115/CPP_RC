import QtQuick
import QtQuick.Window

Rectangle {
    id: root
    width: 800
    height: 600
    color: "#3c3c3c"
    state: "Normal"

    Image {
        id: image
        x: 0
        y: -5
        width: 811
        height: 628
        source: "Diagnostic.png"
        fillMode: Image.PreserveAspectFit
    }

}
