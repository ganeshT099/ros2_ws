from setuptools import find_packages, setup

package_name = 'robo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/talker_listener.launch.py']),
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
            'hello_world = robo.hello_world:main',
            'my_first_node = robo.my_first_node:main',
            'publisher_oop = robo.oop_pub:main',
            'subscriber_oop = robo.oop_sub:main',
            'service_server = robo.service_server:main',
            'service_client = robo.service_client:main'
              ],
    },
)