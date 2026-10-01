#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from my_service.srv import MoveTurtle
import time


class MoveTurtleService(Node):

    def __init__(self):
        super().__init__('move_turtle_server')

        # Create service
        self.srv = self.create_service(
            MoveTurtle,
            'move_turtle',
            self.move_turtle_callback
        )

        # Publisher for turtle velocity
        self.publisher = self.create_publisher(
            Twist,
            '/turtle1/cmd_vel',
            10
        )

        self.get_logger().info(
            'MoveTurtle service is ready.'
        )

    def move_turtle_callback(self, request, response):

        self.get_logger().info(
            f"Received request: x={request.x}, "
            f"y={request.y}, "
            f"theta={request.theta}, "
            f"duration={request.duration}"
        )

        start_time = time.time()

        while (time.time() - start_time) < request.duration:

            # Calculate elapsed time
            elapsed_time = time.time() - start_time

            # Gradually increase linear velocity
            linear_velocity = request.x * (
                1 + elapsed_time / request.duration
            )

            # Create Twist message
            twist = Twist()

            twist.linear.x = linear_velocity
            twist.linear.y = request.y
            twist.angular.z = request.theta

            # Publish velocity
            self.publisher.publish(twist)

            # Publish every 0.1 seconds
            time.sleep(0.1)

        # Stop turtle after completing spiral
        stop_twist = Twist()
        self.publisher.publish(stop_twist)

        response.success = True

        self.get_logger().info(
            'Spiral movement completed successfully.'
        )

        return response


def main(args=None):

    rclpy.init(args=args)

    node = MoveTurtleService()

    try:
        rclpy.spin(node)

    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()