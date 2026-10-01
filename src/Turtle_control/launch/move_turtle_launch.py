from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='turtlesim',
            executable='turtlesim_node',
            name='turtlesim'
        ),
        Node(
            package='Turtle_control',
            executable='move_turtle_server',
            name='move_turtle_server',
            output='screen'
        )
    ])