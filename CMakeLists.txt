cmake_minimum_required(VERSION 3.16.3)
project(atlas_garden_joystick)

find_package(
    catkin
    REQUIRED
    COMPONENTS rospy
)

catkin_python_setup()

catkin_package(CATKIN_DEPENDS rospy)

include_directories(${catkin_INCLUDE_DIRS})
