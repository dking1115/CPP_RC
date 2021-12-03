import QtQuick
import QtQuick.Controls

Page {
    width: 600
    height: 400

    title: qsTr("Home")

    Label {
        text: qsTr("You are on the home page.")
        anchors.centerIn: parent
    }
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
