from setuptools import find_packages, setup

package_name = 'Turtle_control'

setup(
    name=package_name,
    version='0.0.0',

    packages=find_packages(exclude=['test']),

    data_files=[
        (
            'share/ament_index/resource_index/packages',
            ['resource/' + package_name]
        ),

        (
            'share/' + package_name,
            ['package.xml']
        ),

        (
            'share/' + package_name + '/launch',
            [
                'launch/move_turtle_launch.py',
                'launch/move_turtle_action_launch.py'
            ]
        ),
    ],

    install_requires=['setuptools'],

    zip_safe=True,

    maintainer='giri',
    maintainer_email='giri@todo.todo',

    description='TODO: Package description',
    license='TODO: License declaration',

    extras_require={
        'test': [
            'pytest',
        ],
    },

    entry_points={
        'console_scripts': [
            'move_turtle_server = Turtle_control.move_turtle_server:main',
            'move_turtle_client = Turtle_control.move_turtle_client:main',
            'move_turtle_action_server = Turtle_control.move_turtle_action_server:main',
            'move_turtle_action_client = Turtle_control.move_turtle_action_client:main',
        ],
    },
)