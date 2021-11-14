import QtQuick
import QtQuick.Controls
import Display 1.0
import QtCore 6.2

Rectangle {
    id: root
    width: Constants.width
    height: Constants.height
    color: "#3c3c3c"
    state: "Normal"

    MouseArea {
        id: remote_Button
        x: 1
        y: 333
        width: 93
        height: 59

        Connections {
            target: remote_Button
            onClicked: root.state = "Remote"
        }
    }

    MouseArea {
        id: diagnostic_button
        x: 0
        y: 134
        width: 101
        height: 63

        Connections {
            target: diagnostic_button
            onClicked: root.state = "Diagnostic"
        }
    }

    Item {
        id: home_Button
        x: 0
        y: 0
        width: 94
        height: 68

        Connections {
            target: home_Button
            onClicked: root.state = ""
        }
    }

    Image {
        id: diagnostic
        x: 902
        y: 146
        width: 1030
        height: 665
        source: "Diagnostic.png"
        fillMode: Image.PreserveAspectFit
    }

    Image {
        id: expanded_Menu
        x: 0
        y: -37
        width: 300
        height: 473
        visible: false
        source: "Expanded_Menu.png"
        fillMode: Image.PreserveAspectFit
    }
    states: [
        State {
            name: "Remote"

            PropertyChanges {
                target: diagnostic
                x: 74
                y: 15
                width: 718
                height: 371
            }
        },
        State {
            name: "Trans"

            PropertyChanges {
                target: remote_Button
                x: 149
                y: -47
            }

            PropertyChanges {
                target: diagnostic
                x: 149
                y: -175
                width: 211
                height: 153
                visible: false
            }
        },
        State {
            name: "Normal"
            PropertyChanges {
                target: nav_Bar
                visible: true
            }
            PropertyChanges {
                target: expanded_Menu
                visible: false
            }

            PropertyChanges {
                target: mouseArea
                x: 90
                y: 186
                width: 44
                height: 27
            }
        },
        State {
            name: "expanded"
            PropertyChanges {
                target: expanded_Menu
                visible: true
            }
            PropertyChanges {
                target: nav_Bar
                visible: false
            }
        }
    ]
    Image {
        id: nav_Bar
        x: 0
        y: 0
        width: 127
        height: 400
        visible: nav_Bar.state = "Normal"
        source: "images/Nav_Bar.png"
        fillMode: Image.PreserveAspectFit
    }

    MouseArea {
        id: mouseArea
        x: 96
        y: 188
        width: 31
        height: 25

        Connections {
            target: mouseArea
            onClicked: root.state = "expanded"
        }
    }
}
