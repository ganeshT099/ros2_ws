import os

from launch import LaunchDescription
from launch.actions import ExecuteProcess, TimerAction
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    # Get the package share directory
    pkg_share = get_package_share_directory('my_robot_description')

    # Path to the robot URDF
    urdf_file = os.path.join(
        pkg_share,
        'urdf',
        'mobile_robot2.urdf'
    )

    # Start Gazebo Fortress with an empty world
    gazebo = ExecuteProcess(
        cmd=[
            'ign',
            'gazebo',
            '-r',
            '-v',
            '4',
            'empty.sdf'
        ],
        output='screen'
    )

    # Spawn the robot into the Gazebo world
    spawn_entity = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-world', 'empty',
            '-name', 'tortoisebot',
            '-file', urdf_file,
            '-x', '0',
            '-y', '0',
            '-z', '0.05',
        ],
        output='screen'
    )

    # ROS 2 <-> Gazebo Fortress bridge
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist]ignition.msgs.Twist',
            '/odom@nav_msgs/msg/Odometry[ignition.msgs.Odometry',
            '/clock@rosgraph_msgs/msg/Clock[ignition.msgs.Clock',
        ],
        output='screen'
    )

    # Allow Gazebo to start before spawning the robot
    delayed_spawn = TimerAction(
        period=8.0,
        actions=[spawn_entity]
    )

    return LaunchDescription([
        gazebo,
        delayed_spawn,
        bridge,
    ])
