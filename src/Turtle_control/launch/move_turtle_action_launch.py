from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([

        # Launch turtlesim
        Node(
            package="turtlesim",
            executable="turtlesim_node",
            name="turtlesim",
            output="screen"
        ),

        # Launch MoveTurtle Action Server
        Node(
            package="Turtle_control",
            executable="move_turtle_action_server",
            name="move_turtle_action_server",
            output="screen"
),  

        Node(
            package="Turtle_control",
            executable="move_turtle_action_client",
            name="move_turtle_action_client",
            output="screen"
),
    ])