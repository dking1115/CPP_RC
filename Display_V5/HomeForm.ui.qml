import QtQuick
import QtQuick.Controls

Page {
    width: 600
    height: 400

    title: qsTr("Home")

    Image {
        id: home_Screen
        x: 219
        y: 200
        width: 314
        height: 183
        source: "Home_Screen.png"
        fillMode: Image.PreserveAspectFit
    }
}
