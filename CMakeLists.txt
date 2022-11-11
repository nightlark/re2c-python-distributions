cmake_minimum_required(VERSION 3.18)

project(re2cPythonDistributions NONE)

include(re2c_version.cmake)
set(RE2C_DOWNLOAD_URL "https://github.com/skvadrik/re2c/releases/download/${RE2C_VERSION}/re2c-${RE2C_VERSION}.tar.xz")

include(ExternalProject)
# This is a bootstrapped executable, set RE2C_FOR_BUILD to a re2c executable to regenerate .re files
ExternalProject_add(build-re2c
  URL "${RE2C_DOWNLOAD_URL}"
  SOURCE_DIR ${CMAKE_BINARY_DIR}/re2c-src
  BINARY_DIR ${CMAKE_BINARY_DIR}/re2c-build
  UPDATE_COMMAND ""
  INSTALL_COMMAND ""
  USES_TERMINAL_DOWNLOAD 1
  USES_TERMINAL_CONFIGURE 1
  USES_TERMINAL_BUILD 1
  CMAKE_ARGS
    -DCMAKE_BUILD_TYPE=Release
    -DRE2C_BUILD_RE2GO=ON
    -DRE2C_BUILD_LIBS=OFF
    -DBUILD_SHARED_LIBS=OFF
    -DRE2C_BUILD_BENCHMARKS=OFF
    -DRE2C_REBUILD_DOCS=OFF
    -DRE2C_REBUILD_LEXERS=OFF
    -DRE2C_REGEN_BENCHMARKS=OFF
    -DCMAKE_INSTALL_PREFIX:PATH=${CMAKE_INSTALL_PREFIX}
  BUILD_COMMAND ${CMAKE_COMMAND} --build .
)
install(SCRIPT ${CMAKE_BINARY_DIR}/re2c-build/cmake_install.cmake)
set(re2c-executable ${CMAKE_BINARY_DIR}/re2c-build/re2c)
set(re2go-executable ${CMAKE_BINARY_DIR}/re2c-build/re2go)

find_program(STRIP_EXECUTABLE strip)
if(STRIP_EXECUTABLE)
  add_custom_target(
    strip-re2c
    ALL
    COMMAND ${STRIP_EXECUTABLE} ${re2c-executable} ${re2go-executable}
  )
  add_dependencies(strip-re2c build-re2c)
endif()

install(
  PROGRAMS
    ${re2c-executable}
    ${re2go-executable}
  DESTINATION re2c/data/bin
)
