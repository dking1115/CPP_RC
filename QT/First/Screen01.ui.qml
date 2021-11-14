import QtQuick 2.15
import Constants 1.0

Rectangle {
    width: Constants.width
    height: Constants.height
    color: Constants.backgroundColor

    Text {
        text: "Hello"
        anchors.centerIn: parent
    }

    Rectangle {
        id: rectangle
        x: 142
        y: 326
        width: 200
        height: 200
        color: "#ff0000"
    }

    Text {
        id: text1
        x: 429
        y: 187
        text: Constants.objectName
        font.pixelSize: 12
    }
}
