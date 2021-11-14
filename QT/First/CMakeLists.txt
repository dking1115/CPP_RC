cmake_minimum_required (VERSION 3.15)

project(First VERSION 0.0.1 LANGUAGES C CXX ASM)

find_package(Qul)

if (Qul_VERSION VERSION_GREATER_EQUAL "1.7")
    qul_add_target(First)
    set_property(TARGET First APPEND PROPERTY QUL_FONTS_DIR "${CMAKE_CURRENT_SOURCE_DIR}/fonts")
else()
    add_executable(First)
    set(QUL_FONTS_DIR "${CMAKE_CURRENT_SOURCE_DIR}/fonts,${QUL_FONTS_DIR}")
    target_link_libraries(First
        Qul::QuickUltralite
        Qul::QuickUltralitePlatform)
endif()

# Using recurse search to find image files in project directory
# Excluding MCUDefaultStyle because it exists for compatibility purposes with QDS
file(GLOB_RECURSE imgSources "*.png" "*.svg" "*.jpg" "*.jpeg")
list(FILTER imgSources EXCLUDE REGEX ".*/MCUDefaultStyle/.*")

if(imgSources)
    qul_add_resource(First FILES ${imgSources})
endif()

# Registering singletons as qml module
qul_add_qml_module(ConstantsModule
    URI Constants
    QML_FILES
        imports/Constants/Constants.qml
)

# Using recurse search to find all qml files in project directory
# Excluding Constants folder because it is part of another qml module
# Excluding MCUDefaultStyle because it exists for compatibility purposes with QDS
file(GLOB_RECURSE qmlSources "*.qml")
list(FILTER qmlSources EXCLUDE REGEX ".*/imports/Constants/.*")
list(FILTER qmlSources EXCLUDE REGEX ".*/MCUDefaultStyle/.*")
qul_target_qml_sources(First ${qmlSources})

target_link_libraries(First
    Qul::QuickUltraliteTimeline
    Qul::QuickUltraliteControlsStyleDefault
    ConstantsModule)

if (Qul_VERSION VERSION_GREATER_EQUAL "1.8")
    target_link_libraries(First
        Qul::QuickUltraliteShapes)
endif()

app_target_setup_os(First)

if (Qul_VERSION VERSION_GREATER_EQUAL "1.7")
    app_target_default_entrypoint(First First)
else()
    app_target_default_main(First First)
endif()
