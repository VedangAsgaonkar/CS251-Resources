cmake_minimum_required(VERSION 3.10.2)
project (helloworld)
include_directories(include)
add_executable(mygamestatic mygame.cpp)
target_link_libraries(mygamestatic PUBLIC MyEngineStatic)
add_executable(mygamedynamic mygame.cpp)
target_link_libraries(mygamedynamic PUBLIC MyEngineDynamic)
