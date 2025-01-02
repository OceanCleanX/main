FROM ros:jazzy-ros-base

RUN apt-get update && apt-get install -y \
      ros-${ROS_DISTRO}-rmw-cyclonedds-cpp && \
    rm -rf /var/lib/apt/lists/*
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
