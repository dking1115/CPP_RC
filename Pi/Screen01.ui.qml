import QtQuick 2.15
import Constants 1.0

Rectangle {
    id: rectangle
    width: Constants.width
    height: Constants.height
    color: Constants.backgroundColor

    Text {
        text: qsTr("Hello Pi")
        anchors.verticalCenterOffset: -133
        anchors.horizontalCenterOffset: -40
        anchors.centerIn: parent
    }

    Image {
        id: radiobuttoncheckedpressed
        x: 543
        y: 99
        source: "MCUDefaultStyle/images/radiobutton-checked-pressed.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: checkboxchecked
        x: 64
        y: 167
        source: "MCUDefaultStyle/images/checkbox-checked.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: checkboxchecked1
        x: 64
        y: 231
        source: "MCUDefaultStyle/images/checkbox-checked.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: progressbarbackground
        x: 353
        y: 243
        source: "MCUDefaultStyle/images/progressbar-background.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: dialprogress
        x: 261
        y: 167
        source: "MCUDefaultStyle/images/dial-progress.png"
        fillMode: Image.PreserveAspectFit
    }
}
