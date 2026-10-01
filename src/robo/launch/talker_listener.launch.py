# ~/ros2_ws/src/my_py_pkg/launch/talker_listener.launch.py

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='demo_nodes_py',
            executable='talker',
            name='talker'
        ),
        Node(
            package='demo_nodes_py',
            executable='listener',
            name='listener'
        )
    ])