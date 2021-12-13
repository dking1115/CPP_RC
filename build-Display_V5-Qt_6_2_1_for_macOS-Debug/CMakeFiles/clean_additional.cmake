# Additional clean files
cmake_minimum_required(VERSION 3.16)

if("${CONFIG}" STREQUAL "" OR "${CONFIG}" STREQUAL "Debug")
  file(REMOVE_RECURSE
  "CMakeFiles/Display_V5_autogen.dir/AutogenUsed.txt"
  "CMakeFiles/Display_V5_autogen.dir/ParseCache.txt"
  "Display_V5_autogen"
  )
endif()
