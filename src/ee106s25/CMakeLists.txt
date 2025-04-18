cmake_minimum_required(VERSION 3.8)
project(ee106s25)

# Enable Python
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)

# ROS 2 core packages
find_package(rclpy REQUIRED)
find_package(std_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)

# Message file generation
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/EE106lab_custom.msg"
  "msg/EE106lab_custom_new.msg"
  DEPENDENCIES std_msgs
)

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

# Export interfaces
ament_export_dependencies(rosidl_default_runtime)

# Install Python scripts
install(PROGRAMS
  ee106s25/publisher.py
  ee106s25/subscriber.py
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()