#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_service.srv import MoveTurtle


class MoveTurtleClient(Node):

    def __init__(self):
        super().__init__('move_turtle_client')

        # Create service client
        self.client = self.create_client(
            MoveTurtle,
            'move_turtle'
        )

        # Wait until service is available
        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info(
                'Service not available, waiting...'
            )

    def send_request(self, x, y, theta, duration):

        # Create request
        request = MoveTurtle.Request()

        request.x = x
        request.y = y
        request.theta = theta
        request.duration = duration

        # Send request
        future = self.client.call_async(request)

        # Wait for response
        rclpy.spin_until_future_complete(
            self,
            future
        )

        return future.result()


def main(args=None):

    rclpy.init(args=args)

    client = MoveTurtleClient()

    # Spiral parameters
    #
    # Starting velocity = 0.2 m/s
    # Sideways velocity = 0
    # Angular velocity = 0.5 rad/s
    # Duration = 30 seconds

    response = client.send_request(
        0.2,
        0.0,
        0.5,
        30.0
    )

    if response.success:

        client.get_logger().info(
            'Spiral movement was successful!'
        )

    else:

        client.get_logger().info(
            'Spiral movement failed.'
        )

    client.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()